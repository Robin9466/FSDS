"""
#### **1. Database and Table Creation**
- **Objective:** Learn to create and structure a database for data storage.
- **Assignment:**
  - Create a database named `SchoolDB`.
  - Create a `students` table with columns: `id` (INT, PRIMARY KEY), `name` (VARCHAR), `age` (INT), and `grade` (VARCHAR).
- **Deliverable:** SQL script for creating the database and table.
"""

import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password):
    """Create a database connection to the MySQL server."""
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_query(connection, query):
    """Execute a single query."""
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

# Connection parameters
host = "localhost"  # Replace with your server IP if remote
user = "root"  # Replace with your MySQL username
password = "*M076@MySQL#"  # Replace with your MySQL password

# Create a connection
connection = create_connection(host, user, password)

# SQL commands to create database and table
create_database_query = "CREATE DATABASE IF NOT EXISTS SchoolDB;"
use_database_query = "USE SchoolDB;"
create_table_query = """
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT,
    grade VARCHAR(5)
);
"""

# Execute queries
execute_query(connection, create_database_query)
execute_query(connection, use_database_query)  # Note: This will not work directly via `execute_query` in MySQL
execute_query(connection, create_table_query)

# Close the connection
if connection:
    connection.close()


"""
Explanation of the Code:
Creating Connection:

The create_connection function establishes a connection to the MySQL server using the provided credentials.
Executing Queries:

The execute_query function executes any SQL command passed to it and commits the transaction.
Creating Database and Table:

The code first creates the database SchoolDB if it doesn't exist.
Note that using USE SchoolDB; within the Python function will not work because mysql-connector-python doesn't maintain a session for that purpose. You should specify the database when creating the connection instead.
Auto-increment ID:

The id column is defined as AUTO_INCREMENT, meaning it will automatically increment with each new record.
Summary
This Pythonic approach provides an easy way to create a database and tables programmatically. Make sure to replace the connection parameters (host, user, password) with your own credentials.
"""