import csv
import json
import os


def read_submissions(filepath: str) -> list:
    if not os.path.exists(filepath):
        raise FileNotFoundError("File not found: " + filepath)

    file = open(filepath, newline="")
    reader = csv.DictReader(file)
    data = []
    for row in reader:
        if row["score"].strip() == "" or not row["score"].strip().replace(".", "").isdigit():
            raise ValueError("Invalid score for: " + row["name"])
        data.append(row)
    file.close()

    if len(data) == 0:
        raise ValueError("CSV file is empty.")

    return data


def get_submitted_students(data: list) -> list:
    result = []
    for student in data:
        if student["submitted"] == "yes":
            result.append(student)
    return result


def calculate_average_score(data: list) -> float:
    submitted = get_submitted_students(data)
    total = 0
    for student in submitted:
        total += float(student["score"])
    return round(total / len(submitted), 2)


def get_domain_wise_average(data: list) -> dict:
    submitted = get_submitted_students(data)
    domain_scores = {}

    for student in submitted:
        domain = student["domain"]
        if domain not in domain_scores:
            domain_scores[domain] = []
        domain_scores[domain].append(float(student["score"]))

    domain_avg = {}
    for domain in domain_scores:
        total = sum(domain_scores[domain])
        domain_avg[domain] = round(total / len(domain_scores[domain]), 2)

    return domain_avg


def get_missing_submissions(data: list) -> list:
    result = []
    for student in data:
        if student["submitted"] == "no":
            result.append(student["name"])
    return result


def write_summary(summary: dict, output_path: str) -> None:
    os.makedirs("task_2/output", exist_ok=True)
    file = open(output_path, "w")
    json.dump(summary, file, indent=2)
    file.close()