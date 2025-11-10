# 🧩 QueueCTL — A Simple Job Queue CLI

QueueCTL is a lightweight **Python-based job queue system** built using the `click` library.  
It lets you **enqueue jobs**, **start workers**, and **monitor job statuses** — all from your command line.

---

## 🚀 Features

✅ Enqueue jobs with custom shell commands  
✅ Run multiple workers concurrently  
✅ Persistent job tracking using `jobs.json`  
✅ Clean CLI design powered by `click`  
✅ Works seamlessly on Windows Command Prompt  

---

## ⚙️ Setup Instructions

### 1️⃣ Navigate to your working directory
```bash
cd C:\Users\bammi\Downloads
```

### 2️⃣ Rename file if needed
```bash
ren "queuecql assign.py" queuectl_assign.py
```

### 3️⃣ Create and activate a virtual environment
```bash
python -m venv venv
venv\Scripts\activate.bat
```

### 4️⃣ Install dependencies
```bash
pip install click
```

### 5️⃣ Verify installation
```bash
python queuectl_assign.py --help
```

Output:
```
Commands:
  enqueue  Add a new job to the queue
  status   Show summary of all jobs
  worker   Manage workers
```

---

## 💻 Usage Examples

### ➕ Add Jobs to Queue
```bash
python queuectl_assign.py enqueue "{\"id\":\"job1\",\"command\":\"echo Hello from job1\"}"
python queuectl_assign.py enqueue "{\"id\":\"job2\",\"command\":\"cmd /c exit 1\"}"
```

✅ Output:
```
Job 'job1' added to the queue.
Job 'job2' added to the queue.
```

---

### ⚙️ Start Workers
```bash
python queuectl_assign.py worker start --count 2
```

👷 Example Output:
```
Worker-1 started.
Worker-2 started.
✅ Worker-1: Job 'job1' completed successfully.
❌ Worker-2: Job 'job2' failed (exit code 1)
```

---

### 📊 Check Status
```bash
python queuectl_assign.py status
```

📋 Example Output:
```
Job Queue Summary:
- job1 : success
- job2 : failed
```

---

## 🧠 Architecture Overview

### 🌀 Job Lifecycle
```
queued → running → success / failed
```

### 💾 Data Persistence
All job data is stored in a local JSON file (`jobs.json`).  
This enables persistence across sessions without needing an external database.

### 🧵 Worker Logic
Each worker:
1. Fetches a queued job.
2. Runs it using `subprocess.run()`.
3. Updates status based on return code.
4. Waits briefly before checking for the next job.

### ⚡ Queue Management
- Thread-safe file access using a global lock.
- Multiple workers can process jobs concurrently.
- Workers terminate automatically when no queued jobs remain.

---

## ⚖️ Assumptions & Trade-offs

| Category | Decision / Assumption |
|-----------|------------------------|
| **Persistence** | Simple JSON storage (`jobs.json`) |
| **Concurrency** | Thread-based (lightweight) |
| **Error Handling** | Exit code-based success/failure detection |
| **Scalability** | Suitable for local/small batch execution |
| **Simplicity** | Focused on CLI clarity and local execution |

---

## 🧪 Testing Instructions

### 🧹 Step 1 — Clear Old Jobs
```bash
del jobs.json
```

### 🧩 Step 2 — Add Test Jobs
```bash
python queuectl_assign.py enqueue "{\"id\": \"test1\", \"command\": \"echo Test Job 1\"}"
python queuectl_assign.py enqueue "{\"id\": \"test2\", \"command\": \"cmd /c exit 1\"}"
```

### 🚀 Step 3 — Start Workers
```bash
python queuectl_assign.py worker start --count 2
```

### 📋 Step 4 — View Status
```bash
python queuectl_assign.py status
```

✅ Expected Output:
```
test1 → success  
test2 → failed
```

---

## 📁 Project Structure

```
queuectl_assign.py   # Main script
jobs.json            # Persistent job storage
venv/                # Virtual environment
README.md            # Documentation + code
```

---

## 🧑‍💻 Author

**Developed by:** Bammidi Hemarao  
**Language:** Python 3.10+  
**Library:** click  
**Environment:** Windows Command Prompt  



## 🌈 Summary

This project demonstrates:
- CLI design using `click`  
- Concurrency with threads  
- JSON-based queue persistence  
- Worker coordination  
- Error handling and logging  

✨ *"A simple queue, a powerful concept — built with Python."* ✨
