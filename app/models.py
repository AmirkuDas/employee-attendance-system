from sqlalchemy import Column, Integer, String, Date, ForeignKey
from .database import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)
    department = Column(String)
    joining_date = Column(Date)


class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    attendance_date = Column(Date)
    status = Column(String)