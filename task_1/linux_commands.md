# Linux Commands Reference — Task 1

## 1. pwd

**Purpose:** Prints the current working directory.

**Command**

```bash
pwd
```

**Output**

```text
/mnt/c/Users/niles/Downloads/Summer_School_2026/Synergy_Taskphase/Synergy_TP/Synergy_TP_Rutuj
```

## 2. ls

**Purpose:** Lists files and folders in the current directory.

**Command**

```bash
ls
```

**Output**

```text
task_1  .gitignore  README.md
```

## 3. ls -la

**Purpose:** Lists all files including hidden files, along with permissions, size, and timestamps.

**Command**

```bash
ls -la
```

**Output**

```text
total 0
drwxrwxrwx 1 root root 4096 Jun 25 02:15 .
drwxrwxrwx 1 root root 4096 Jun 25 02:08 ..
drwxrwxrwx 1 root root 4096 Jun 25 01:40 .git
-rwxrwxrwx 1 root root  204 Jun 25 02:18 .gitignore
drwxrwxrwx 1 root root 4096 Jun 25 01:51 task_1
```

## 4. cd

**Purpose:** Changes the current directory.

**Command**

```bash
cd task_1
```

**Output**

```text
No output (directory changed successfully)
```

## 5. mkdir

**Purpose:** Creates a new directory.

**Command**

```bash
mkdir task_1/testdir
```

**Output**

```text
No output (directory created successfully)
```

## 6. touch

**Purpose:** Creates an empty file or updates its timestamp.

**Command**

```bash
touch task_1/data/sample.txt
```

**Output**

```text
No output (file created/updated successfully)
```

## 7. cat

**Purpose:** Displays the contents of a file.

**Command**

```bash
cat task_1/data/sample.txt
```

**Output**

```text
Sample text file for Task 1.
```

## 8. echo

**Purpose:** Prints text to the terminal.

**Command**

```bash
echo "Hello from terminal"
```

**Output**

```text
Hello from terminal
```

## 9. cp

**Purpose:** Copies a file to another location.

**Command**

```bash
cp task_1/data/sample.txt task_1/data/sample_copy.txt
```

**Output**

```text
No output (file copied successfully)
```

## 10. mv

**Purpose:** Moves or renames a file.

**Command**

```bash
mv task_1/data/sample_copy.txt task_1/data/renamed.txt
```

**Output**

```text
No output (file renamed successfully)
```

## 11. rm

**Purpose:** Removes a file permanently.

**Command**

```bash
rm task_1/data/renamed.txt
```

**Output**

```text
No output (file deleted successfully)
```

## 12. grep

**Purpose:** Searches for lines containing a specific word or pattern.

**Command**

```bash
grep "sample" task_1/data/sample.txt
```

**Output**

```text
This is a sample text file for Task 1.
```

## 13. find

**Purpose:** Searches for files matching a given pattern.

**Command**

```bash
find task_1 -name "*.py"
```

**Output**

```text
task_1/src/hello.py
```

## 14. head

**Purpose:** Displays the first few lines of a file.

**Command**

```bash
head -2 task_1/data/sample.txt
```

**Output**

```text
This is a sample text file for Task 1.
Line 2: Linux commands are useful.
```

## 15. tail

**Purpose:** Displays the last few lines of a file.

**Command**

```bash
tail -1 task_1/data/sample.txt
```

**Output**

```text
Line 3: grep, head, tail, and wc work on this file.
```

## 16. wc

**Purpose:** Counts lines, words, and characters in a file.

**Command**

```bash
wc -l task_1/data/sample.txt
```

**Output**

```text
3 task_1/data/sample.txt
```

## 17. chmod

**Purpose:** Changes file permissions and makes the script executable.

**Command**

```bash
chmod +x task_1/src/hello.py
```

**Output**

```text
No output (permissions changed successfully)
```
