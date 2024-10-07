"""
#### **1. Database and Table Creation**
- **Objective:** Learn to create and structure a database for data storage.
- **Assignment:**
  - Create a database named `SchoolDB`.
  - Create a `students` table with columns: `id` (INT, PRIMARY KEY), `name` (VARCHAR), `age` (INT), and `grade` (VARCHAR).
- **Deliverable:** SQL script for creating the database and table.
"""

import mysql.connector

# Step 1: Establish a connection to the MySQL server
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="*M076@MySQL#"
)

# Step 2: Create a cursor object to execute SQL commands
cursor = db_connection.cursor()

# Step 3: Create a new database (if it doesn't already exist)
cursor.execute("CREATE DATABASE IF NOT EXISTS SchoolDB")
print(f"Database 'SchoolDB' created successfully")

# Step 4: Select the newly created database to use it
cursor.execute("USE SchoolDB")

# Step 5: Create a new table in the selected database
table_creation_query = """
CREATE TABLE IF NOT EXISTS student1 (
id INT AUTO_INCREMENT PRIMARY KEY,  # Unique id for each of the student
name VARCHAR(255),  # Name of the students
age INT,    # Age of the students   
grade VARCHAR(255) # Grade of the students
);
"""
cursor.execute(table_creation_query)
print(f"Table 'student1' created successfully!")
# Step 6: Close the cursor and the connection
cursor.close()
db_connection.close()