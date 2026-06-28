# Task 4 - Messy CSV Cleaning

## Objective

Clean a messy student dataset with pandas, validate the result, and document every cleaning decision.

## Folder Structure

```text
task_4/
  data/messy_students.csv
  src/clean_data.py
  src/validate_data.py
  src/main.py
  output/cleaned_students.csv
  output/summary_before.json
  output/summary_after.json
  output/cleaning_report.md
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
python task_4/src/main.py task_4/data/messy_students.csv task_4/output/cleaned_students.csv
```

## Expected Outputs

- `task_4/output/cleaned_students.csv`
- `task_4/output/summary_before.json`
- `task_4/output/summary_after.json`
- `task_4/output/cleaning_report.md`

## Logic

The program records the original data types, missing values, duplicates, and category values. It then removes duplicates, normalizes categories and units, converts numeric fields, handles missing or invalid values using documented rules, and validates the cleaned result before saving it.

## Report Generation

The cleaning report is generated automatically by the same run command. Its final path is `task_4/output/cleaning_report.md`; no manual export is required.
