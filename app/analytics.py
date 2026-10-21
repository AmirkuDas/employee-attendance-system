# app/analytics.py

import pandas as pd
import numpy as np


def attendance_summary(attendance_records):

    if not attendance_records:
        return {
            "total_records": 0,
            "present": 0,
            "absent": 0,
            "leave": 0,
            "wfh": 0,
            "attendance_percentage": 0
        }

    data = []

    for record in attendance_records:
        data.append({
            "employee_id": record.employee_id,
            "status": record.status
        })

    # Pandas DataFrame
    df = pd.DataFrame(data)

    total_records = len(df)

    present_count = len(
        df[df["status"] == "Present"]
    )

    absent_count = len(
        df[df["status"] == "Absent"]
    )

    leave_count = len(
        df[df["status"] == "Leave"]
    )

    wfh_count = len(
        df[df["status"] == "WFH"]
    )

    # NumPy Calculation
    attendance_percentage = np.round(
        (present_count / total_records) * 100,
        2
    )

    return {
        "total_records": total_records,
        "present": present_count,
        "absent": absent_count,
        "leave": leave_count,
        "wfh": wfh_count,
        "attendance_percentage": float(
            attendance_percentage
        )
    }