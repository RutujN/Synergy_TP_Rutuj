import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from manual_parser import read_csv_manual, convert_types, calculate_summary, write_json
from pandas_parser import read_csv_pandas, calculate_summary_pandas


if len(sys.argv) != 2:
    print("Usage: python task_3/src/main.py <input_csv>")
    sys.exit()

input_path = sys.argv[1]

# Create the summary using the manual parser.
rows = read_csv_manual(input_path)
rows = convert_types(rows)
manual_summary = calculate_summary(rows)
write_json(manual_summary, "task_3/output/manual_summary.json")

# Create the same summary using pandas.
df = read_csv_pandas(input_path)
pandas_summary = calculate_summary_pandas(df)
write_json(pandas_summary, "task_3/output/pandas_summary.json")

# Compare both summaries one item at a time.
report_lines = ["# Comparison Report", "", "## Do both outputs match?", ""]
all_match = True

for key in manual_summary:
    if manual_summary[key] == pandas_summary[key]:
        report_lines.append("- " + key + ": MATCH")
    else:
        report_lines.append("- " + key + ": MISMATCH")
        report_lines.append("  - Manual: " + str(manual_summary[key]))
        report_lines.append("  - Pandas: " + str(pandas_summary[key]))
        all_match = False

if all_match:
    report_lines.append("")
    report_lines.append("Both summaries match completely.")
else:
    report_lines.append("")
    report_lines.append("Some values differ.")

os.makedirs("task_3/output", exist_ok=True)
file = open("task_3/output/comparison_report.md", "w", encoding="utf-8")
file.write("\n".join(report_lines))
file.close()

print("Manual summary, pandas summary, and comparison report written.")
