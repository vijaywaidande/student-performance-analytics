import mysql.connector
import pandas as pd

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vijay@14",
    database="student_performance"
)

print("MySQL connected successfully!")


# Retrieve students from MySQL
cursor = connection.cursor(dictionary=True)

cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

df = pd.DataFrame(students)

print("\nStudent Data:")
print(df)

print("\nAverage Marks:")

print("Maths:", df["maths"].mean())
print("Python:", df["python"].mean())
print("SQL:", df["sql_marks"].mean())

top_student = df.loc[df["python"].idxmax()]

print("\nTop Python Student:")
print(top_student["name"], "-", top_student["python"])

top_overall = df.loc[df[["maths", "python", "sql_marks"]].mean(axis=1).idxmax()]

print("\nTop Overall Student:")
print(top_overall["name"])

# Calculate total and average
for student in students:
    total = student["maths"] + student["python"] + student["sql_marks"]
    average = total / 3

    student["total"] = total
    student["average"] = average

    print(
        student["name"],
        "Total:", total,
        "Average:", round(average, 2)
    )


# Linear Search
search_id = int(input("\nEnter student ID to search: "))

found = False

for student in students:
    if student["id"] == search_id:
        print("Student Found:", student["name"])
        found = True
        break

if not found:
    print("Student Not Found")


# Sort students by average
students.sort(
    key=lambda student: student["average"],
    reverse=True
)


# Display ranking
print("\nStudent Ranking")

rank = 1

for student in students:
    print(
        rank,
        student["name"],
        "Average:",
        round(student["average"], 2)
    )
    rank += 1

    df["total"] = df["maths"] + df["python"] + df["sql_marks"]

    df["average"] = df["total"] / 3

    def get_result(average):
        if average >= 90:
          return "Excellent"
        elif average >= 80:
          return "Good"
        else:
          return "Needs Improvement"


df["result"] = df[["maths", "python", "sql_marks"]].mean(axis=1).apply(get_result)

print("\nStudent Results:")
print(
    df[["name", "total", "average", "result"]].round({"average": 2})
)

df = df.sort_values(by="average", ascending=False)

print("\nPandas Ranking:")
print(
    df[["name", "total", "average", "result"]].round({"average": 2})
)