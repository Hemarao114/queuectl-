# ⚙️ Queue Control CLI — Python Job Queue Assignment

> 🧠 **A lightweight Command-Line Interface (CLI) for managing job queues** — built entirely in Python using `click` and `colorama`.

This project demonstrates how to enqueue background jobs, process them with multiple workers, track progress, and manage failures via a Dead Letter Queue (DLQ).  
It simulates a small-scale job queue system — ideal for learning about concurrent job execution and process orchestration.

---

## 🧩 Features

✅ Add jobs to a queue dynamically  
👷 Start multiple workers to process jobs in parallel  
📊 Monitor job statuses (pending, running, success, failed)  
♻️ Manage and retry failed jobs using a Dead Letter Queue  
💾 Stores job states persistently in a JSON file  

---

## 🧰 Tech Stack

| Component | Purpose |
|------------|----------|
| 🐍 Python 3.8+ | Core language |
| ⚡ Click | CLI command management |
| 🌈 Colorama | Colorized terminal output |
| 📁 JSON | Lightweight data storage |

---

## 🚀 Getting Started

### 1️⃣ Clone or Download the Script

Place the provided file `queuectl_assign.py` in your working directory.

### 2️⃣ Open Command Prompt

```bash
cd "C:\Users\bammi\Downloads"
```

### 3️⃣ Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate.bat
```

### 4️⃣ Install Dependencies

```bash
pip install click colorama
```

---

## 🧠 CLI Commands

Run help at any time:
```bash
python queuectl_assign.py --help
```

You’ll see available commands:
```
Commands:
  enqueue  Add a new job to the queue
  status   Show summary of all jobs
  worker   Manage workers
```

---

## 💡 Usage Examples

### 🧱 Enqueue Jobs

```bash
python queuectl_assign.py enqueue "{\"id\":\"job1\",\"command\":\"echo Hello from job1\"}"
python queuectl_assign.py enqueue "{\"id\":\"job2\",\"command\":\"cmd /c exit 1\"}"
```

➡️ Output:
```
✅ Job 'job1' added to the queue.
✅ Job 'job2' added to the queue.
```

---

### ⚙️ Start Worker(s)

```bash
python queuectl_assign.py worker start --count 2
```

➡️ Expected output:
```
👷 Starting 2 workers...
[Worker 1] Running job job1: echo Hello from job1
Hello from job1
✅ Job job1 completed successfully.

[Worker 2] Running job job2: cmd /c exit 1
❌ Job job2 failed. Moving to DLQ.
```

---

### 📊 Check Job Status

```bash
python queuectl_assign.py status
```

➡️ Output Example:
```
📋 Job Summary:
✔️ Completed: 1
❌ Failed: 1
🕓 Pending: 0
```

---

### 💀 View or Retry Dead Letter Queue (DLQ)

List failed jobs:
```bash
python queuectl_assign.py dlq list
```

Retry failed jobs (if implemented):
```bash
python queuectl_assign.py dlq retry
```

---

## 📂 Folder Structure

```
C:\Users\bammi\Downloads\
│
├── queuectl_assign.py     # Main Python CLI script
├── queue_data.json        # Auto-generated queue storage
├── venv/                  # Virtual environment
└── README.md              # Documentation file
```

---

## 🧾 Example Session (Full Run)

```bash
> python queuectl_assign.py enqueue "{\"id\":\"job1\",\"command\":\"echo Hello\"}"
✅ Job 'job1' added to the queue.

> python queuectl_assign.py enqueue "{\"id\":\"job2\",\"command\":\"cmd /c exit 1\"}"
✅ Job 'job2' added to the queue.

> python queuectl_assign.py worker start --count 2
👷 Worker 1 started
👷 Worker 2 started
[Worker 1] Running job job1: echo Hello
Hello
✅ Job job1 completed successfully.
[Worker 2] Running job job2: cmd /c exit 1
❌ Job job2 failed. Moving to DLQ.

> python queuectl_assign.py status
✔️ 1 succeeded, ❌ 1 failed, 🕓 0 pending
```

---

## 🧑‍💻 Author & Submission

**👤 Name:** Bammidi Hemarao  
**🏫 Institution:** NIT Raipur  
**📘 Project:** Python CLI for Job Queue Simulation  
 

---

## ⭐ Key Learning Outcomes

- Working with CLI tools using `click`  
- Managing asynchronous or queued tasks  
- Implementing persistent state tracking via JSON  
- Handling and retrying failed jobs  
- Structuring maintainable Python command-line projects  

---

💡 *“Automation doesn’t replace effort — it amplifies efficiency.”*  
Made with ❤️ in Python.
