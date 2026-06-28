import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from visualize import (
    load_cleaned_data,
    plot_domain_average_score,
    plot_attendance_vs_score,
    plot_submission_status_count,
    write_plot_summary,
)


if len(sys.argv) != 3:
    print("Usage: python task_5/src/main.py <cleaned_csv> <output_folder>")
    sys.exit()

input_path = sys.argv[1]
output_folder = sys.argv[2]

os.makedirs(output_folder, exist_ok=True)
df = load_cleaned_data(input_path)

domain_plot = os.path.join(output_folder, "domain_average_score.png")
attendance_plot = os.path.join(output_folder, "attendance_vs_score.png")
submission_plot = os.path.join(output_folder, "submission_status_count.png")
summary_file = os.path.join(output_folder, "plot_summary.md")

plot_domain_average_score(df, domain_plot)
plot_attendance_vs_score(df, attendance_plot)
plot_submission_status_count(df, submission_plot)
write_plot_summary(summary_file)
