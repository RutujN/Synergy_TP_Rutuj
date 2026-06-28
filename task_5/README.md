# Task 5 - Matplotlib Visualization

## Objective

Generate three labeled plots from the cleaned student dataset produced by Task 4.

## Folder Structure

```text
task_5/
  src/visualize.py
  src/main.py
  output/domain_average_score.png
  output/attendance_vs_score.png
  output/submission_status_count.png
  output/plot_summary.md
```

## Required Packages

- pandas
- matplotlib

## Setup

From the repository root, activate the virtual environment and run:

```bash
pip install -r requirements.txt
```

## Run Command

```bash
python task_5/src/main.py task_4/output/cleaned_students.csv task_5/output
```

## Expected Outputs

- `task_5/output/domain_average_score.png`
- `task_5/output/attendance_vs_score.png`
- `task_5/output/submission_status_count.png`
- `task_5/output/plot_summary.md`

## Logic

The program loads Task 4's cleaned CSV, groups submitted scores by domain for one bar chart, plots attendance against score in a scatter plot, and counts submission values for a second bar chart. Every plot has a title and axis labels and is saved without opening a window.
