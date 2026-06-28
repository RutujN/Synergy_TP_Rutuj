import json
import os


def read_csv_manual(file_path: str) -> list[dict]:
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    rows = []
    header = []

    for line_number in range(len(lines)):
        line = lines[line_number].strip()

        if line == "":
            continue

        parts = line.split(",")

        if len(header) == 0:
            header = parts
            continue

        if len(parts) != len(header):
            continue

        row = {}
        for column_number in range(len(header)):
            row[header[column_number]] = parts[column_number]

        rows.append(row)

    return rows


def convert_types(rows: list[dict]) -> list[dict]:
    for row in rows:
        try:
            row["score"] = int(row["score"])
        except ValueError:
            row["score"] = 0

        row["submitted"] = row["submitted"].strip().lower()

    return rows


def calculate_summary(rows: list[dict]) -> dict:
    submitted_students = []
    missing_students = []

    for student in rows:
        if student["submitted"] == "yes":
            submitted_students.append(student)
        else:
            missing_students.append(student["name"])

    total_score = 0
    for student in submitted_students:
        total_score = total_score + student["score"]

    if len(submitted_students) > 0:
        average_score = round(total_score / len(submitted_students), 2)
        highest = submitted_students[0]
        lowest = submitted_students[0]

        for student in submitted_students:
            if student["score"] > highest["score"]:
                highest = student
            if student["score"] < lowest["score"]:
                lowest = student

        highest_scorer = highest["name"] + " (" + str(highest["score"]) + ")"
        lowest_scorer = lowest["name"] + " (" + str(lowest["score"]) + ")"
    else:
        average_score = 0
        highest_scorer = None
        lowest_scorer = None

    domain_scores = {}
    for student in submitted_students:
        domain = student["domain"]
        if domain not in domain_scores:
            domain_scores[domain] = []
        domain_scores[domain].append(student["score"])

    domain_averages = {}
    for domain in domain_scores:
        scores = domain_scores[domain]
        domain_averages[domain] = round(sum(scores) / len(scores), 2)

    students_below_5 = []
    for student in submitted_students:
        if student["score"] < 5:
            students_below_5.append(student["name"])

    summary = {
        "total_students": len(rows),
        "submitted_count": len(submitted_students),
        "missing_count": len(missing_students),
        "average_score": average_score,
        "highest_scorer": highest_scorer,
        "lowest_scorer": lowest_scorer,
        "domain_wise_average": domain_averages,
        "missing_submissions": missing_students,
        "students_below_5": students_below_5,
    }

    return summary


def write_json(data: dict, output_path: str) -> None:
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)
