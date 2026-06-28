def validate_cleaned_data(df) -> bool:
    valid = True

    if df["student_id"].duplicated().any():
        print("FAIL: Duplicate student_id found.")
        valid = False

    if not df["attendance_percent"].between(0, 100).all():
        print("FAIL: attendance_percent is out of range.")
        valid = False

    try:
        df["score"].astype(float)
    except ValueError:
        print("FAIL: score contains non-numeric values.")
        valid = False

    try:
        df["study_hours"].astype(float)
    except ValueError:
        print("FAIL: study_hours contains non-numeric values.")
        valid = False

    try:
        df["height_cm"].astype(float)
        df["weight_kg"].astype(float)
    except ValueError:
        print("FAIL: height or weight contains non-numeric values.")
        valid = False

    allowed_submitted_values = ["yes", "no"]
    if not df["submitted"].isin(allowed_submitted_values).all():
        print("FAIL: submitted contains an unexpected value.")
        valid = False

    allowed_domains = ["ML", "Web", "Electronics", "Mechanical"]
    if not df["domain"].isin(allowed_domains).all():
        print("FAIL: domain contains an unexpected value.")
        valid = False

    important_columns = ["student_id", "name", "domain", "score", "submitted"]
    for column in important_columns:
        if df[column].isnull().any():
            print("FAIL: Missing value in", column)
            valid = False

    if valid:
        print("All validation checks passed.")

    return valid
