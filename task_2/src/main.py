import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from analyzer import read_submissions, get_submitted_students, calculate_average_score, get_domain_wise_average, get_missing_submissions, write_summary

input_path = sys.argv[1]
output_path = sys.argv[2]

data = read_submissions(input_path)
submitted = get_submitted_students(data)
missing = get_missing_submissions(data)
avg = calculate_average_score(data)
domain_avg = get_domain_wise_average(data)

highest = submitted[0]
lowest = submitted[0]
for student in submitted:
    if float(student["score"]) > float(highest["score"]):
        highest = student
    if float(student["score"]) < float(lowest["score"]):
        lowest = student

below_5 = []
for student in submitted:
    if float(student["score"]) < 5:
        below_5.append(student["name"])

summary = {
    "total_students": len(data),
    "submitted_count": len(submitted),
    "missing_count": len(missing),
    "average_score": avg,
    "highest_scorer": highest["name"] + " (" + highest["score"] + ")",
    "lowest_scorer": lowest["name"] + " (" + lowest["score"] + ")",
    "domain_wise_average": domain_avg,
    "missing_submissions": missing,
    "students_below_5": below_5
}

print("Total students     :", len(data))
print("Submitted          :", len(submitted))
print("Missing            :", len(missing))
print("Average score      :", avg)
print("Highest scorer     :", highest["name"], highest["score"])
print("Lowest scorer      :", lowest["name"], lowest["score"])
print("Domain-wise avg    :", domain_avg)
print("Missing submissions:", missing)
print("Students below 5   :", below_5)

write_summary(summary, output_path)
print("Summary written to :", output_path)