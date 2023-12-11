import mysql.connector as conn

mydb = conn.connect(host='localhost', user='root', passwd='*K37759@Others#')
cursor = mydb.cursor()

# Uncomment the line below if you want to create the 'robin' database
# cursor.execute('CREATE DATABASE IF NOT EXISTS robin')

# Switch to the 'robin' database
cursor.execute('USE robin')

# Fix the syntax error in the CREATE TABLE statement
s = cursor.execute('CREATE TABLE kalee (employee_id int(10), emp_name varchar(80), emp_email varchar(80), emp_salary int(10))')

# Show the tables in the 'robin' database
#q1 = cursor.execute('s')
q2 = cursor.execute("select * from robin.kalee")
tables = cursor.fetchall()
print(q2)
print("Tables in 'robin' database:", tables)

# Commit the changes and close the cursor and connection
mydb.commit()
cursor.close()
mydb.close()
