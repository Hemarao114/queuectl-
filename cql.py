# 1️⃣ Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate    # on Windows: venv\Scripts\activate

# 2️⃣ Install dependencies
pip install click

# 3️⃣ Run the CLI tool
python queuectl.py enqueue '{"id":"job1","command":"echo Hello"}'
python queuectl.py worker start --count 2
