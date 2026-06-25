# Task 2 — Python Recap Assignment

## Description

This task reads student submission data from a CSV file, analyzes the records, and generates a summary report in JSON format. It demonstrates the use of Python functions, file handling, loops, lists, dictionaries, and basic data processing.

## Project Structure

```text
task_2/
├── data/
│   └── submissions.csv
├── output/
    └── summary.json
├── src/
│   ├── analyzer.py
│   └── main.py
├── README.md
└── requirements.txt
```

## Prerequisites

Install the required Python packages:

```bash
pip install -r task_2/requirements.txt
```

## Run Instructions

From the **Synergy_TP** root directory, run:

```bash
python task_2/src/main.py task_2/data/submissions.csv task_2/output/summary.json
```

## Expected Output

The program displays:

* Total number of students
* Number of submitted and missing submissions
* Average score
* Highest scorer
* Lowest scorer
* Students who scored below 5
* List of missing submissions

It also creates a JSON summary file at:

```text
task_2/output/summary.json
```

## Functions in `analyzer.py`

| Function                    | Description                                         |
| --------------------------- | --------------------------------------------------- |
| `read_submissions()`        | Reads student data from the CSV file.               |
| `get_submitted_students()`  | Returns only students who submitted their work.     |
| `calculate_average_score()` | Calculates the average score of submitted students. |
| `get_domain_wise_average()` | Calculates the average score for each domain.       |
| `get_missing_submissions()` | Returns the names of students who did not submit.   |
| `write_summary()`           | Writes the generated summary to a JSON file.        |

#

