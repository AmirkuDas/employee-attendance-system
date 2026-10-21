from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .database import Base
from .database import engine
from .database import get_db

from . import crud
from . import schemas
from . import models
from . import analytics

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Employee Attendance System"
)


@app.get("/")
def home():
    return {
        "message": "Application Running"
    }


# =====================================
# Employee APIs
# =====================================

@app.post("/employees")
def create_employee(
    employee: schemas.EmployeeCreate,
    db: Session = Depends(get_db)
):
    return crud.create_employee(
        db,
        employee
    )


@app.get("/employees")
def get_employees(
    db: Session = Depends(get_db)
):
    return crud.get_employees(db)


# =====================================
# Attendance APIs
# =====================================

@app.post("/attendance")
def create_attendance(
    attendance: schemas.AttendanceCreate,
    db: Session = Depends(get_db)
):
    return crud.create_attendance(
        db,
        attendance
    )


@app.get("/attendance")
def get_attendance(
    db: Session = Depends(get_db)
):
    return crud.get_attendance(db)


# =====================================
# Analytics API
# =====================================

@app.get("/analytics/summary")
def analytics_summary(
    db: Session = Depends(get_db)
):
    attendance_records = crud.get_all_attendance(db)

    return analytics.attendance_summary(
        attendance_records
    )