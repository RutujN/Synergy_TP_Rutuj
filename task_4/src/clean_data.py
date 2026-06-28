import os

import pandas as pd


def load_data(file_path: str):
    return pd.read_csv(file_path)


def generate_summary(df) -> dict:
    unique_values = {}
    unique_values["domain"] = df["domain"].dropna().unique().tolist()
    unique_values["submitted"] = df["submitted"].dropna().unique().tolist()

    summary = {
        "total_rows": len(df),
        "columns": list(df.columns),
        "data_types": df.dtypes.astype(str).to_dict(),
        "missing_values": df.isnull().sum().to_dict(),
        "duplicates": int(df.duplicated().sum()),
        "unique_categorical_values": unique_values,
    }
    return summary


def remove_duplicates(df):
    return df.drop_duplicates()


def standardize_domains(df):
    for row_number in df.index:
        domain = str(df.at[row_number, "domain"]).strip().lower()

        if domain == "ml" or domain == "machine learning":
            df.at[row_number, "domain"] = "ML"
        elif domain == "web" or domain == "web dev" or domain == "web development":
            df.at[row_number, "domain"] = "Web"
        elif domain == "electronics":
            df.at[row_number, "domain"] = "Electronics"
        elif domain == "mechanical":
            df.at[row_number, "domain"] = "Mechanical"

    return df


def clean_attendance(df):
    cleaned_values = []

    for value in df["attendance_percent"]:
        value = str(value).replace("%", "").strip()

        try:
            number = float(value)
            if number < 0 or number > 100:
                cleaned_values.append(None)
            else:
                cleaned_values.append(number)
        except ValueError:
            cleaned_values.append(None)

    df["attendance_percent"] = cleaned_values
    return df


def clean_scores(df):
    word_to_number = {"nine": 9, "two": 2, "one": 1, "zero": 0}
    cleaned_values = []

    for value in df["score"]:
        value = str(value).strip().lower()

        if value in word_to_number:
            cleaned_values.append(word_to_number[value])
        else:
            try:
                cleaned_values.append(float(value))
            except ValueError:
                cleaned_values.append(None)

    df["score"] = cleaned_values
    return df


def clean_study_hours(df):
    word_to_number = {"nine": 9, "two": 2, "one": 1, "zero": 0}
    cleaned_values = []

    for value in df["study_hours"]:
        value = str(value).strip().lower()

        if value in word_to_number:
            cleaned_values.append(word_to_number[value])
        else:
            try:
                cleaned_values.append(float(value))
            except ValueError:
                cleaned_values.append(None)

    df["study_hours"] = cleaned_values
    return df


def clean_height(df):
    cleaned_values = []

    for value in df["height"]:
        value = str(value).strip().lower()

        try:
            if "cm" in value:
                number = float(value.replace("cm", "").strip())
                cleaned_values.append(round(number, 1))
            elif "m" in value:
                number = float(value.replace("m", "").strip())
                cleaned_values.append(round(number * 100, 1))
            else:
                cleaned_values.append(float(value))
        except ValueError:
            cleaned_values.append(None)

    df["height_cm"] = cleaned_values
    df = df.drop(columns=["height"])
    return df


def clean_weight(df):
    cleaned_values = []

    for value in df["weight"]:
        value = str(value).lower().replace("kg", "").strip()

        try:
            cleaned_values.append(float(value))
        except ValueError:
            cleaned_values.append(None)

    df["weight_kg"] = cleaned_values
    df = df.drop(columns=["weight"])
    return df


def clean_submitted(df):
    cleaned_values = []

    for value in df["submitted"]:
        value = str(value).strip().lower()

        if value == "yes" or value == "y":
            cleaned_values.append("yes")
        elif value == "no" or value == "n":
            cleaned_values.append("no")
        else:
            cleaned_values.append(None)

    df["submitted"] = cleaned_values
    return df


def handle_missing_values(df):
    attendance_median = df["attendance_percent"].median()
    study_hours_median = df["study_hours"].median()
    weight_median = df["weight_kg"].median()

    df["attendance_percent"] = df["attendance_percent"].fillna(attendance_median)
    df["score"] = df["score"].fillna(0)
    df["study_hours"] = df["study_hours"].fillna(study_hours_median)
    df["weight_kg"] = df["weight_kg"].fillna(weight_median)

    return df


def save_cleaned_data(df, output_path: str) -> None:
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)


def write_report(report_path: str) -> None:
    report = """# Data Cleaning Report

## Changes Made

- Removed the second, identical S005 row so each student ID occurs once.
- Changed `ml` and `MACHINE LEARNING` to `ML`; changed `web`, `Web Dev`, and `web development` to `Web`; changed `electronics` to `Electronics`.
- Removed `%` from attendance and converted the column to numbers.
- Treated S007's `-10` and S008's `105%` attendance as invalid. Together with S003's missing attendance, these values were replaced by the valid-column median of 88.
- Converted Isha's score `nine` to 9 and Rohan's study hours `two` to 2.
- Filled S009's missing score with 0 because no recorded score is treated as not scored.
- Converted heights in metres and centimetres into `height_cm` (for example, `1.62 m` became 162).
- Removed `kg` from weights and stored them in `weight_kg`. S003's missing weight was replaced by the median of 58 kg.
- Changed `Yes`, `Y`, and `yes` to `yes`; changed `N`, `no`, and `No` to `no`.

## Why median for missing values?

The median is resistant to extreme values, making it suitable for this small dataset.
"""

    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    with open(report_path, "w", encoding="utf-8") as file:
        file.write(report)
