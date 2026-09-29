# Student Performance Analytics & Ranking System

A Python-based student performance analytics project that stores student marks in MySQL, processes the data using Python and Pandas, applies basic searching and sorting algorithms for ranking, and displays the results through an interactive Streamlit dashboard.

The project was built to practice **Python, Data Structures & Algorithms, MySQL, Pandas, and Streamlit** together in one practical application.

---

## Project Overview

The system stores student academic records in a MySQL database.

Python retrieves the student data and performs:

* Total marks calculation
* Average marks calculation
* Linear search
* Student ranking using sorting
* Performance classification

Pandas is then used for data analysis, while Streamlit provides the interactive dashboard.

### Overall Project Flow

```text
                MySQL Database
                      |
                      v
               students table
                      |
                      v
                 main.py
                      |
          +-----------+-----------+
          |           |           |
          v           v           v
       Total       Average     Linear Search
          |           |           |
          +-----------+-----------+
                      |
                      v
                  Sorting
                      |
                      v
               Student Ranking
                      |
                      v
                  Pandas
                      |
          +-----------+-----------+
          |           |           |
          v           v           v
    Subject Avg   Top Student   Result Analysis
          |           |           |
          +-----------+-----------+
                      |
                      v
                  app.py
                      |
                      v
             Streamlit Dashboard
```

---

## Features

* Store student records in MySQL
* Retrieve student data using Python
* Calculate total marks
* Calculate average marks
* Search for a student using Linear Search
* Sort students based on average marks
* Generate student rankings
* Calculate subject-wise average marks
* Find the top-performing student
* Classify student performance
* Display student data using Pandas
* Interactive Streamlit dashboard
* Search students from the dashboard

---

## Technologies Used

| Technology             | Purpose                                |
| ---------------------- | -------------------------------------- |
| Python                 | Main programming language              |
| MySQL                  | Store student records                  |
| MySQL Workbench        | Create and manage the database         |
| mysql-connector-python | Connect Python with MySQL              |
| Pandas                 | Data analysis and DataFrame operations |
| Streamlit              | Build the interactive dashboard        |
| Lists & Dictionaries   | Store and process retrieved records    |
| Linear Search          | Search for a student                   |
| Sorting                | Generate student rankings              |
| Git                    | Version control                        |
| GitHub                 | Source code hosting                    |

---

## Project Structure

```text
student-performance-analytics/
│
├── main.py
│   └── Main Python program
│
├── app.py
│   └── Streamlit dashboard
│
├── README.md
│   └── Project documentation
│
└── .gitignore
    └── Files and folders excluded from Git
```

---

# File Flow

## 1. MySQL Database

The MySQL database is the main source of student data.

Database:

```text
student_performance
```

Table:

```text
students
```

Table structure:

```text
students
│
├── id
├── name
├── maths
├── python
└── sql_marks
```

Example:

```text
ID    Name       Maths    Python    SQL
1     Rahul       78       82       80
4     Vijay       96       98       95
```

The database stores the original marks.

---

# 2. `main.py`

`main.py` is the main Python processing program.

### Step 1 — Connect to MySQL

Python connects to the `student_performance` database using:

```python
mysql.connector
```

The connection allows Python to retrieve records from MySQL.

---

### Step 2 — Retrieve Students

The program executes:

```sql
SELECT * FROM students;
```

The records are retrieved as Python dictionaries.

Example:

```text
{
    "id": 4,
    "name": "Vijay",
    "maths": 96,
    "python": 98,
    "sql_marks": 95
}
```

---

### Step 3 — Calculate Total Marks

For every student:

```text
Total = Maths + Python + SQL
```

Example:

```text
Vijay

96 + 98 + 95 = 289
```

---

### Step 4 — Calculate Average

The average is calculated using:

```text
Average = Total / 3
```

For example:

```text
289 / 3 = 96.33
```

---

# 3. Linear Search

The project demonstrates **Linear Search** to find a student by ID.

The program checks students one by one:

```text
Student 1
   ↓
Student 2
   ↓
Student 3
   ↓
...
   ↓
Target Student
```

Example:

```text
Search ID: 4

ID 1 → Not Found
ID 2 → Not Found
ID 3 → Not Found
ID 4 → Found
```

This demonstrates the basic concept of searching through a list.

---

# 4. Sorting and Ranking

After calculating averages, the students are sorted by average marks in descending order.

```text
Highest Average
       ↓
       1
       ↓
       2
       ↓
       3
       ↓
Lowest Average
```

Example:

```text
Rank    Student      Average
1       Vijay        96.33
2       Pranav       94.33
3       Kunal        91.67
...
```

Python sorting is used here to demonstrate how student records can be ordered based on calculated performance.

---

# 5. Pandas Analysis

The retrieved student records are converted into a Pandas DataFrame.

```text
MySQL
  ↓
Python List of Dictionaries
  ↓
Pandas DataFrame
```

Pandas is then used for data analysis.

### Subject Average

The project calculates:

* Average Maths marks
* Average Python marks
* Average SQL marks

---

## Top Python Student

Pandas is used to find the student with the highest Python marks.

Example:

```text
Top Python Student
Pranav - 96
```

---

## Top Overall Student

The project identifies the student with the highest overall average.

Example:

```text
Top Overall Student
Vijay
```

---

# 6. Performance Classification

Students are classified according to their average marks.

```text
Average >= 90
       ↓
   Excellent

Average >= 80
       ↓
     Good

Average < 80
       ↓
Needs Improvement
```

This creates a simple performance category for every student.

---

# 7. `app.py`

`app.py` contains the Streamlit dashboard.

The dashboard connects directly to the same MySQL database.

### Dashboard Flow

```text
MySQL
  ↓
app.py
  ↓
Pandas DataFrame
  ↓
Calculations
  ↓
Streamlit
  ↓
Interactive Dashboard
```

---

## Dashboard Sections

### Performance Summary

The dashboard displays:

* Total Students
* Average Marks
* Highest Average

---

### Student Performance

Displays:

```text
ID
Name
Maths
Python
SQL
Total
Average
```

---

### Student Ranking

Displays students sorted by average marks:

```text
Rank
Student
Total
Average
```

---

### Average Marks by Subject

A bar chart displays the average marks for:

* Maths
* Python
* SQL

---

### Performance Result

Displays:

```text
Student
Average
Result
```

Possible results:

```text
Excellent
Good
Needs Improvement
```

---

### Search Student

The dashboard provides a Student ID input.

Example:

```text
Enter Student ID: 4
```

The dashboard displays the corresponding student's details.

---

# Database Design

## Database

```text
student_performance
```

## Table

```sql
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    maths INT,
    python INT,
    sql_marks INT
);
```

The project intentionally uses a simple database structure because the main focus is on learning Python, SQL connectivity, data processing, and basic DSA.

---

# Data Structures Used

## List

Retrieved student records are stored and processed as a Python list.

```text
students
   ↓
Student 1
Student 2
Student 3
...
```

---

## Dictionary

Each student record is represented as a dictionary.

Example:

```python
{
    "id": 1,
    "name": "Rahul",
    "maths": 78,
    "python": 82,
    "sql_marks": 80
}
```

---

## Linear Search

Used to search for a student by ID.

---

## Sorting

Used to arrange students according to their average marks and generate rankings.

---

# Sample Student Record

```text
Name: Vijay

Maths: 96
Python: 98
SQL: 95

Total: 289
Average: 96.33
Result: Excellent
```

---

# How to Run the Project

## Prerequisites

Install:

* Python
* MySQL
* MySQL Workbench
* Git

---

## 1. Clone the Repository

```bash
git clone https://github.com/vijaywaidande/student-performance-analytics.git
```

```bash
cd student-performance-analytics
```

---

## 2. Create the MySQL Database

Open MySQL Workbench and run:

```sql
CREATE DATABASE student_performance;

USE student_performance;
```

Create the table:

```sql
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    maths INT,
    python INT,
    sql_marks INT
);
```

Add your student records to the table.

---

# 3. Install Python Libraries

Open the project terminal and run:

```bash
pip install mysql-connector-python pandas streamlit
```

---

# 4. Configure MySQL Connection

Both `main.py` and `app.py` require a MySQL connection.

The connection follows this structure:

```python
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_MYSQL_PASSWORD",
    database="student_performance"
)
```

Replace:

```text
YOUR_MYSQL_PASSWORD
```

with your local MySQL password.

**Do not upload your actual MySQL password to GitHub.**

---

# 5. Run the Python Program

Run:

```bash
python main.py
```

The program will:

```text
Connect to MySQL
      ↓
Retrieve students
      ↓
Calculate totals
      ↓
Calculate averages
      ↓
Search student
      ↓
Sort students
      ↓
Generate ranking
      ↓
Perform Pandas analysis
```

---

# 6. Run the Streamlit Dashboard

Run:

```bash
streamlit run app.py
```

Streamlit will start the local dashboard in your browser.

---

# Example Project Output

### Ranking

```text
Rank    Student      Average
1       Vijay        96.33
2       Pranav       94.33
3       Kunal        91.67
4       Sneha        89.67
...
```

### Performance Categories

```text
Excellent
Good
Needs Improvement
```

---

# What I Learned From This Project

This project helped me practice:

### Python

* Variables
* Lists
* Dictionaries
* Loops
* Functions
* Conditional statements
* Sorting
* Searching

### Data Structures & Algorithms

* Lists
* Dictionaries
* Linear Search
* Sorting
* Ranking logic

### SQL & MySQL

* Database creation
* Table creation
* INSERT
* SELECT
* Database connectivity
* Retrieving records from MySQL

### Pandas

* DataFrames
* Filtering data
* Calculating averages
* Finding maximum values
* Data analysis

### Streamlit

* Dashboard creation
* KPI metrics
* Tables
* Charts
* User input
* Interactive student search

### Git & GitHub

* Git repository initialization
* `.gitignore`
* Commits
* Branches
* Remote repositories
* Pushing code to GitHub

---

# Project Architecture

```text
                 ┌─────────────────────┐
                 │     MySQL Database  │
                 │  student_performance│
                 └──────────┬──────────┘
                            │
                            │ SQL
                            ▼
                 ┌─────────────────────┐
                 │       Python        │
                 │      main.py        │
                 └──────────┬──────────┘
                            │
              ┌─────────────┼─────────────┐
              │             │             │
              ▼             ▼             ▼
          Calculate      Search        Sorting
           Average       Student       Ranking
              │             │             │
              └─────────────┼─────────────┘
                            │
                            ▼
                     ┌────────────┐
                     │   Pandas   │
                     │  Analysis  │
                     └─────┬──────┘
                           │
                           ▼
                     ┌────────────┐
                     │  app.py    │
                     │ Streamlit  │
                     └─────┬──────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │    Dashboard     │
                  │                  │
                  │ KPIs             │
                  │ Student Table    │
                  │ Ranking          │
                  │ Subject Chart    │
                  │ Search           │
                  └──────────────────┘
```

---

# Future Improvements

Possible future improvements include:

* Add more subjects
* Add student attendance data
* Add semester-wise performance
* Add CSV export
* Add filters for departments or classes
* Add more dashboard visualizations
* Add automated tests

---

# Project Purpose

The main purpose of this project is to understand how a simple real-world data application can combine:

```text
Python
+
MySQL
+
Data Structures & Algorithms
+
Pandas
+
Streamlit
+
Git & GitHub
```

The project focuses on keeping the implementation simple while demonstrating the complete flow from **database storage → Python processing → DSA → data analysis → interactive dashboard**.

---

## Author

**Vijay Waidande**

GitHub: [vijaywaidande](https://github.com/vijaywaidande)

---

## Project Repository

[Student Performance Analytics & Ranking System](https://github.com/vijaywaidande/student-performance-analytics)
