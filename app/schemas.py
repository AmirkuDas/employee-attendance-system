from pydantic import BaseModel
from datetime import date


class EmployeeCreate(BaseModel):
    name: str
    email: str
    department: str
    joining_date: date


class EmployeeResponse(EmployeeCreate):
    id: int

    class Config:
        from_attributes = True


# Attendance Schemas

class AttendanceCreate(BaseModel):
    employee_id: int
    attendance_date: date
    status: str


class AttendanceResponse(AttendanceCreate):
    id: int

    class Config:
        from_attributes = True