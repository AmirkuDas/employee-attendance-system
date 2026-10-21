from sqlalchemy.orm import Session
from . import models
from . import schemas


def create_employee(
    db: Session,
    employee: schemas.EmployeeCreate
):
    db_employee = models.Employee(
        name=employee.name,
        email=employee.email,
        department=employee.department,
        joining_date=employee.joining_date
    )

    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)

    return db_employee


def get_employees(db: Session):
    return db.query(
        models.Employee
    ).all()

def create_attendance(db, attendance):
    db_attendance = models.Attendance(
        employee_id=attendance.employee_id,
        attendance_date=attendance.attendance_date,
        status=attendance.status
    )

    db.add(db_attendance)
    db.commit()
    db.refresh(db_attendance)

    return db_attendance


def get_attendance(db):
    return db.query(
        models.Attendance
    ).all()

def get_all_attendance(db):
    return db.query(
        models.Attendance
    ).all()