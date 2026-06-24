# Setup Log — Task 1

## 1. Created project folders

```bash id="3c8n4d"
mkdir -p task_1/src
mkdir -p task_1/data
```

Creates the source and data directories for Task 1.

## 2. Created required files

```bash id="pccn4v"
touch task_1/README.md
touch task_1/requirements.txt
touch task_1/setup_log.md
touch task_1/linux_commands.md
touch task_1/src/hello.py
touch task_1/data/sample.txt
```

Creates the files required for Task 1.

## 3. Verified project structure

```bash id="bzwzvt"
find task_1 -type f
```

Lists all files inside the task_1 directory.

## 4. Checked Python installation

```bash id="9bwk4g"
python3 --version
```

Verifies that Python 3 is installed.

## 5. Installed virtual environment package

```bash id="huj8mq"
apt update
apt install python3.10-venv -y
```

Installs the venv package required to create virtual environments.

## 6. Created virtual environment

```bash id="7j7mzu"
python3 -m venv task_1/venv
```

Creates an isolated Python environment inside task_1/venv.

## 7. Activated virtual environment

```bash id="c0l4q8"
source task_1/venv/bin/activate
```

Activates the virtual environment for package installation.

## 8. Installed requests package

```bash id="axc7n8"
pip install requests
```

Installs the Requests HTTP library and its dependencies.

## 9. Generated requirements.txt

```bash id="u3e7z7"
pip freeze > task_1/requirements.txt
```

Stores all installed package versions in requirements.txt.

## 10. Tested hello.py

```bash id="ccw6gw"
python task_1/src/hello.py
```

Runs the Python script and verifies that it executes correctly.

## 11. Deactivated virtual environment

```bash id="qvfhqg"
deactivate
```

Exits the virtual environment.

## 12. Staged project files

```bash id="4yb0zt"
git add .
```

Adds all project files to Git staging.

## 13. Created commit

```bash id="m33q1x"
git commit -m "Completed Task 1"
```

Creates a Git commit containing Task 1 work.

## 14. Pushed to GitHub

```bash id="a1nm7g"
git push origin main
```

Uploads the commit to the remote GitHub repository.


