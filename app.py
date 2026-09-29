import streamlit as st
import mysql.connector
import pandas as pd


st.set_page_config(
    page_title="Student Performance Analytics",
    layout="wide"
)

st.title("Student Performance Analytics & Ranking System")


# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vijay@14",
    database="student_performance"
)

cursor = connection.cursor(dictionary=True)

cursor.execute("SELECT * FROM students")

students = cursor.fetchall()


# Convert MySQL data to Pandas DataFrame
df = pd.DataFrame(students)


# Calculate Total and Average
df["total"] = df["maths"] + df["python"] + df["sql_marks"]
df["average"] = df["total"] / 3


# Performance classification
def get_result(average):
    if average >= 90:
        return "Excellent"
    elif average >= 80:
        return "Good"
    else:
        return "Needs Improvement"


df["result"] = df["average"].apply(get_result)


# KPI Section
st.subheader("Performance Summary")

col1, col2, col3 = st.columns(3)

col1.metric("Total Students", len(df))
col2.metric("Average Marks", round(df["average"].mean(), 2))
col3.metric("Highest Average", round(df["average"].max(), 2))


# Student Performance
st.subheader("Student Performance")

display_df = df[
    ["id", "name", "maths", "python", "sql_marks", "total", "average"]
].copy()

display_df["average"] = display_df["average"].round(2)

st.dataframe(display_df, use_container_width=True)


# Ranking
st.subheader("Student Ranking")

ranking_df = df.sort_values(
    by="average",
    ascending=False
).copy()

ranking_df["Rank"] = range(1, len(ranking_df) + 1)

ranking_df["average"] = ranking_df["average"].round(2)

st.dataframe(
    ranking_df[
        ["Rank", "name", "total", "average"]
    ],
    use_container_width=True
)


# Subject Average Chart
st.subheader("Average Marks by Subject")

subject_average = pd.DataFrame({
    "Subject": ["Maths", "Python", "SQL"],
    "Average": [
        df["maths"].mean(),
        df["python"].mean(),
        df["sql_marks"].mean()
    ]
})

st.bar_chart(
    subject_average,
    x="Subject",
    y="Average"
)


# Performance Result
st.subheader("Performance Result")

result_df = df[
    ["name", "average", "result"]
].copy()

result_df["average"] = result_df["average"].round(2)

st.dataframe(
    result_df,
    use_container_width=True
)


# Search Student
st.subheader("Search Student")

search_id = st.number_input(
    "Enter Student ID",
    min_value=1,
    step=1
)

search_result = df[df["id"] == search_id]

if not search_result.empty:
    search_display = search_result[
        ["id", "name", "maths", "python", "sql_marks",
         "total", "average", "result"]
    ].copy()

    search_display["average"] = search_display["average"].round(2)

    st.dataframe(
        search_display,
        use_container_width=True
    )
else:
    st.info("Student not found.")


# Close database connection
cursor.close()
connection.close()