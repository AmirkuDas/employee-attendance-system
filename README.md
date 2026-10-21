**Employee Attendance Management System**



A REST API-based Employee Attendance Management System built using FastAPI, SQLAlchemy, SQLite, Pandas, and NumPy. The application enables organizations to manage employee records, track attendance, and generate attendance analytics through RESTful APIs.



**Features**

Employee Management



Add new employees

View employee records

Manage employee information

Attendance Tracking



Mark daily attendance

Track employee attendance status

Store attendance records in a database

Analytics \& Reporting



Attendance summaries

Present vs Absent analysis

Data processing using Pandas and NumPy

REST API Architecture



FastAPI-powered endpoints

Interactive Swagger documentation

JSON-based API responses

Tech Stack

Backend

Python

FastAPI

Uvicorn

Database

SQLite

SQLAlchemy ORM

Data Analysis

Pandas

NumPy



**Project Structure**

employee-attendance-system/

│

├── app/

│   ├── main.py

│   ├── database.py

│   ├── models.py

│   ├── schemas.py

│   ├── crud.py

│   ├── analytics.py

│   └── inventory.py

│

├── check\_tables.py

├── requirements.txt

├── README.md

└── .gitignore



**Installation**



1\. Clone the Repository

git clone https://github.com/AmirkuDas/employee-attendance-system.git

2\. Navigate to Project Directory

cd employee-attendance-system

3\. Create Virtual Environment

python -m venv venv

4\. Activate Virtual Environment

Windows

venv\\Scripts\\activate

Linux / Mac

source venv/bin/activate

5\. Install Dependencies

pip install -r requirements.txt

Running the Application

Start the FastAPI server:



uvicorn app.main:app --reload

Server will start at:



**http://127.0.0.1:8000**

API Documentation

Interactive Swagger UI:



http://127.0.0.1:8000/docs

Alternative ReDoc documentation:



http://127.0.0.1:8000/redoc

Available API Endpoints

Employee APIs

Method	Endpoint	Description

POST	/employees	Create Employee

GET	/employees	Get All Employees

Attendance APIs

Method	Endpoint	Description

POST	/attendance	Mark Attendance

GET	/attendance	Get Attendance Records

Analytics APIs

Method	Endpoint	Description

GET	/analytics	Attendance Summary Report

Sample Technologies Used

FastAPI for REST API development

SQLite for lightweight data storage

SQLAlchemy for ORM operations

Pandas for attendance data analysis

NumPy for numerical computations

Future Enhancements

Employee authentication and authorization

Leave management module

Monthly attendance reports

Dashboard visualization

Export reports to Excel and PDF

Department-wise analytics

Learning Outcomes

This project demonstrates:



Backend API development using FastAPI

Database integration with SQLAlchemy

SQLite database design

RESTful API architecture

Data processing using Pandas

Numerical analysis using NumPy

CRUD operations

Version control using Git and GitHub



Author

Amit Das



GitHub: https://github.com/AmirkuDas

