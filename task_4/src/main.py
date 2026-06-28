import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from clean_data import (
    load_data,
    generate_summary,
    remove_duplicates,
    standardize_domains,
    clean_attendance,
    clean_scores,
    clean_study_hours,
    clean_height,
    clean_weight,
    clean_submitted,
    handle_missing_values,
    save_cleaned_data,
    write_report,
)
from validate_data import validate_cleaned_data


if len(sys.argv) != 3:
    print("Usage: python task_4/src/main.py <input_csv> <output_csv>")
    sys.exit()

input_path = sys.argv[1]
output_path = sys.argv[2]
output_folder = "task_4/output"
os.makedirs(output_folder, exist_ok=True)

# Load the original file and save its summary.
df = load_data(input_path)
summary_before = generate_summary(df)

file = open("task_4/output/summary_before.json", "w", encoding="utf-8")
json.dump(summary_before, file, indent=2)
file.close()

# Clean one part of the data at a time.
df = remove_duplicates(df)
df = standardize_domains(df)
df = clean_attendance(df)
df = clean_scores(df)
df = clean_study_hours(df)
df = clean_height(df)
df = clean_weight(df)
df = clean_submitted(df)
df = handle_missing_values(df)

# Keep the columns in the order required by the task document.
required_columns = [
    "student_id",
    "name",
    "domain",
    "attendance_percent",
    "score",
    "study_hours",
    "height_cm",
    "weight_kg",
    "submitted",
]
df = df[required_columns]

# Save a summary of the cleaned data.
summary_after = generate_summary(df)

file = open("task_4/output/summary_after.json", "w", encoding="utf-8")
json.dump(summary_after, file, indent=2)
file.close()

# Only save the cleaned file when all checks pass.
is_valid = validate_cleaned_data(df)

if is_valid:
    save_cleaned_data(df, output_path)
    write_report("task_4/output/cleaning_report.md")
    print("Cleaned CSV saved to:", output_path)
else:
    print("The cleaned data did not pass validation.")
