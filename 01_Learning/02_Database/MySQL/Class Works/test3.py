import mysql.connector as conn

mydb = conn.connect(host='localhost', user='root', passwd='*K37759@Others#')
cursor = mydb.cursor()

# Select specific columns from the 'kalee' table
cursor.execute("SELECT employee_id, emp_name FROM robin.kalee")
l = []

# Fetch and print the records
for i in cursor.fetchall():
    l.append(i)
print(l)
print(type(l[0]))

# Close the cursor and connection
cursor.close()
mydb.close()
