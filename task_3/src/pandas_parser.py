import json
import os

import pandas as pd


def read_csv_pandas(file_path: str):
    return pd.read_csv(file_path)


def calculate_summary_pandas(df) -> dict:
    submitted_df = df[df["submitted"] == "yes"]
    missing_df = df[df["submitted"] == "no"]

    if len(submitted_df) > 0:
        average_score = round(submitted_df["score"].mean(), 2)
        highest = submitted_df.loc[submitted_df["score"].idxmax()]
        lowest = submitted_df.loc[submitted_df["score"].idxmin()]

        highest_scorer = highest["name"] + " (" + str(highest["score"]) + ")"
        lowest_scorer = lowest["name"] + " (" + str(lowest["score"]) + ")"
    else:
        average_score = 0
        highest_scorer = None
        lowest_scorer = None

    domain_averages = submitted_df.groupby("domain")["score"].mean()
    domain_averages = domain_averages.round(2).to_dict()

    summary = {
        "total_students": len(df),
        "submitted_count": len(submitted_df),
        "missing_count": len(missing_df),
        "average_score": average_score,
        "highest_scorer": highest_scorer,
        "lowest_scorer": lowest_scorer,
        "domain_wise_average": domain_averages,
        "missing_submissions": missing_df["name"].tolist(),
        "students_below_5": submitted_df[submitted_df["score"] < 5]["name"].tolist(),
    }

    return summary


def write_json(data: dict, output_path: str) -> None:
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)
