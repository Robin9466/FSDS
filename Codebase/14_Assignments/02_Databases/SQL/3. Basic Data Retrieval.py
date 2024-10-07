"""#### **2. Basic Data Retrieval**
- **Objective:** Master the SELECT statement to fetch data.
- **Assignment:**
  - Write a query to select all records from the `students` table.
  - Write a query to select students with specific conditions (e.g., age > 18).
- **Deliverable:** SQL commands and results."""

import mysql.connector

def data_retrieval():
    # Establish a connection to the MySQL server
    with mysql.connector.connect(
        host="localhost",
        user="root",
        password="*M076@MySQL#",
        database="SchoolDB"
    ) as db_connection:
        # Create a cursor to execute SQL commands
        with db_connection.cursor() as cursor:
            # Execute SQL commands to retrieve all the records of students
            cursor.execute("SELECT * FROM student1")
            all_students = cursor.fetchall()
            print("All students:")
            for student in all_students:
                print(student)

            # Execute SQL commands to retrieve those students, whose age > 18
            cursor.execute("SELECT * FROM student1 WHERE age > 18")
            adult_students = cursor.fetchall()
            print("\nStudents older than 18:")
            for student in adult_students:
                print(student)

data_retrieval()