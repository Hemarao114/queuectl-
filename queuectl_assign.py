import json
import time
import uuid
import threading
import subprocess
import click
from pathlib import Path

QUEUE_FILE = Path("job_queue.json")
LOCK = threading.Lock()

# ------------------- Utility functions -------------------

def load_jobs():
    if not QUEUE_FILE.exists():
        return []
    with QUEUE_FILE.open("r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_jobs(jobs):
    with LOCK:
        with QUEUE_FILE.open("w") as f:
            json.dump(jobs, f, indent=2)

def update_job_status(job_id, status):
    jobs = load_jobs()
    for job in jobs:
        if job["id"] == job_id:
            job["status"] = status
            job["updated_at"] = time.strftime("%Y-%m-%d %H:%M:%S")
            break
    save_jobs(jobs)

# ------------------- CLI commands -------------------

@click.group()
def cli():
    """Simple Job Queue CLI"""
    pass

# ------------------- Enqueue -------------------
@cli.command()
@click.argument("job_json")
def enqueue(job_json):
    """Add a new job to the queue"""
    try:
        job = json.loads(job_json)
        job["id"] = job.get("id", str(uuid.uuid4()))
        job["status"] = "Pending"
        job["created_at"] = time.strftime("%Y-%m-%d %H:%M:%S")
        jobs = load_jobs()
        jobs.append(job)
        save_jobs(jobs)
        click.echo(f"✅ Job '{job['id']}' added to the queue.")
    except json.JSONDecodeError:
        click.echo("❌ Invalid JSON format. Use proper quotes and syntax.")

# ------------------- Status -------------------
@cli.command()
def status():
    """Show summary of all jobs"""
    jobs = load_jobs()
    if not jobs:
        click.echo("No jobs in queue.")
        return
    click.echo("\nJob ID\t\tStatus\t\tCommand")
    click.echo("-" * 50)
    for job in jobs:
        click.echo(f"{job['id']}\t{job['status']}\t{job['command']}")
    click.echo()

# ------------------- Worker -------------------
@cli.group()
def worker():
    """Manage workers"""
    pass

@worker.command("start")
@click.option("--count", default=1, help="Number of workers to start")
def start_worker(count):
    """Start worker(s)"""
    click.echo(f"🚀 Starting {count} worker(s)... Press Ctrl+C to stop.")
    threads = []
    for i in range(count):
        t = threading.Thread(target=worker_loop, args=(i+1,), daemon=True)
        t.start()
        threads.append(t)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        click.echo("\n🛑 Workers stopped manually.")

def worker_loop(worker_id):
    while True:
        jobs = load_jobs()
        pending_jobs = [j for j in jobs if j["status"] == "Pending"]
        if pending_jobs:
            job = pending_jobs[0]
            job_id = job["id"]
            update_job_status(job_id, "Running")
            click.echo(f"[Worker-{worker_id}] Running job {job_id}: {job['command']}")
            try:
                subprocess.run(job["command"], shell=True, check=True)
                update_job_status(job_id, "Completed")
                click.echo(f"[Worker-{worker_id}] ✅ Job {job_id} completed.")
            except subprocess.CalledProcessError:
                update_job_status(job_id, "Failed")
                click.echo(f"[Worker-{worker_id}] ❌ Job {job_id} failed.")
        time.sleep(2)

# ------------------- Run -------------------
if __name__ == "__main__":
    cli()
