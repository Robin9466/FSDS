import mysql.connector

# Establish connection
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='*M076@MySQL#',
    database='School'
    )

print(f"Connection is successful{connection}")