# Task 3 - Manual CSV Parser and Pandas Comparison

## Objective

Read a CSV using basic Python file handling, repeat the analysis with pandas, and compare the two summaries.

## Folder Structure

```text
task_3/
  data/submissions.csv
  src/manual_parser.py
  src/pandas_parser.py
  src/main.py
  output/manual_summary.json
  output/pandas_summary.json
  output/comparison_report.md
```

## Required Package

- pandas

## Setup

From the repository root, activate the virtual environment and run:

```bash
pip install -r requirements.txt
```

## Run Command

```bash
python task_3/src/main.py task_3/data/submissions.csv
```

## Expected Outputs

- `task_3/output/manual_summary.json`
- `task_3/output/pandas_summary.json`
- `task_3/output/comparison_report.md`

## Logic

The manual parser reads lines with `open()`, splits simple comma-separated values, builds one dictionary per row, and converts score and submission values. The pandas parser calculates the same nine metrics using a DataFrame. The main program writes both JSON summaries and checks each value in a comparison report.
