import os
import tempfile

# Store Matplotlib's temporary files in a folder that Python can write to.
os.environ["MPLCONFIGDIR"] = os.path.join(tempfile.gettempdir(), "synergy_matplotlib")

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd


def load_cleaned_data(file_path: str):
    return pd.read_csv(file_path)


def plot_domain_average_score(df, output_path: str) -> None:
    submitted_students = df[df["submitted"] == "yes"]
    domain_averages = submitted_students.groupby("domain")["score"].mean()

    plt.figure()
    plt.bar(domain_averages.index, domain_averages.values)
    plt.title("Average Score by Domain")
    plt.xlabel("Domain")
    plt.ylabel("Average Score")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

    print("Saved:", output_path)


def plot_attendance_vs_score(df, output_path: str) -> None:
    plt.figure()
    plt.scatter(df["attendance_percent"], df["score"])
    plt.title("Attendance vs Score")
    plt.xlabel("Attendance Percent")
    plt.ylabel("Score")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

    print("Saved:", output_path)


def plot_submission_status_count(df, output_path: str) -> None:
    submission_counts = df["submitted"].value_counts()

    plt.figure()
    plt.bar(submission_counts.index, submission_counts.values)
    plt.title("Submission Status Count")
    plt.xlabel("Submitted")
    plt.ylabel("Number of Students")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

    print("Saved:", output_path)


def write_plot_summary(output_path: str) -> None:
    text = """# Plot Summary

## domain_average_score.png

This bar chart compares the average score of submitted students in each domain.
Electronics has the highest submitted-student average in this dataset.
Mechanical is absent because its student did not submit the task.

## attendance_vs_score.png

This scatter plot compares attendance percentage with score for every student.
Higher attendance generally appears with a higher score in this small dataset.
The plot shows association only and does not prove that attendance caused the score.

## submission_status_count.png

This bar chart compares students who submitted with students who did not submit.
Seven students submitted the task and three students did not.
Most students therefore completed their submission.
"""

    file = open(output_path, "w", encoding="utf-8")
    file.write(text)
    file.close()
