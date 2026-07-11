import pandas as pd
import numpy as np
from pathlib import Path


def get_grade(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"


def main():
    data_file = Path("data") / "students.csv"
    output_file = Path("outputs") / "statistics_report.txt"

    output_file.parent.mkdir(exist_ok=True)

    df = pd.read_csv(data_file)

    df["Result"] = np.where(df["Score"] >= 50, "Pass", "Fail")
    df["Grade"] = df["Score"].apply(get_grade)

    mean_score = df["Score"].mean()
    median_score = df["Score"].median()
    min_score = df["Score"].min()
    max_score = df["Score"].max()
    score_range = max_score - min_score
    variance_score = df["Score"].var()
    std_score = df["Score"].std()

    pass_count = (df["Result"] == "Pass").sum()
    fail_count = (df["Result"] == "Fail").sum()
    total_students = len(df)
    pass_probability = pass_count / total_students

    correlation = df["StudyHours"].corr(df["Score"])

    grade_counts = df["Grade"].value_counts()

    report = f"""
Student Statistics Report
-------------------------

Dataset
-------
{df}

Score Statistics
----------------
Mean score: {mean_score:.2f}
Median score: {median_score:.2f}
Minimum score: {min_score}
Maximum score: {max_score}
Score range: {score_range}
Score variance: {variance_score:.2f}
Score standard deviation: {std_score:.2f}

Result Summary
--------------
Students passed: {pass_count}
Students failed: {fail_count}
Probability of passing: {pass_probability:.2f}
Passing rate: {pass_probability * 100:.2f}%

Correlation
-----------
Correlation between study hours and score: {correlation:.2f}

Grade Counts
------------
{grade_counts}
"""

    print(report)

    with open(output_file, "w") as file:
        file.write(report)

    print(f"Report saved to: {output_file}")


main()
