# Task 1 — GitHub, Virtual Environment, and Linux Basics

## Description

This task demonstrates basic Git, Linux, and Python environment setup. It includes:

* Creating a project structure using Linux commands
* Setting up a Python virtual environment
* Installing dependencies using pip
* Running a simple Python script
* Documenting commonly used Linux commands

## Project Structure

```text
task_1/
├── README.md
├── requirements.txt
├── setup_log.md
├── linux_commands.md
├── src/
│   └── hello.py
└── data/
    └── sample.txt
```

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Synergy_TP.git
cd Synergy_TP
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv task_1/venv
source task_1/venv/bin/activate
```

**Windows PowerShell**

```powershell
task_1\venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r task_1/requirements.txt
```

### 4. Run the Python script

From the repository root directory:

```bash
python task_1/src/hello.py
```

## Expected Output

```text
Hello Synergy
```

## Files

| File              | Purpose                                     |
| ----------------- | ------------------------------------------- |
| README.md         | Project overview and setup instructions     |
| requirements.txt  | Python dependencies                         |
| setup_log.md      | Record of setup steps performed             |
| linux_commands.md | Documentation of Linux commands used        |
| src/hello.py      | Sample Python script                        |
| data/sample.txt   | Sample text file for command demonstrations |

