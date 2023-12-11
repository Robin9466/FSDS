import mysql.connector as conn

mydb = conn.connect(host='localhost', user='root', passwd='*K37759@Others#')
cursor = mydb.cursor()

# Switch to the 'robin' database
cursor.execute('USE robin')

# Insert a record into the 'kalee' table
s = cursor.execute('INSERT INTO kalee VALUES (101, "robin kumar", "robinraj@gmail.com", 100)')
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)

# Commit the changes
mydb.commit()

# Select and fetch all records from the 'kalee' table
cursor.execute("SELECT * FROM kalee")
records = cursor.fetchall()

# Print the fetched records
for record in records:
    print(record)

# Close the cursor and connection
cursor.close()
mydb.close()
