import mysql.connector

try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='*M076@MySQL',
        database='School'  # Replace with your database name
    )
    print("Connection successful")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if conn.is_connected():
        conn.close()
