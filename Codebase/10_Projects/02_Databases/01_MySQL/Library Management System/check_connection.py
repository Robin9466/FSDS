import mysql.connector
from datetime import date

# Connect to MySQL
conn = mysql.connector.connect(host='localhost', user='root', password='*M076@MySQL')
cursor = conn.cursor()

try:
    # 1. Create database and use it
    cursor.execute("CREATE DATABASE IF NOT EXISTS library_db")
    cursor.execute("USE library_db")

    # 2. Create tables
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255),
        author VARCHAR(255),
        available BOOLEAN DEFAULT TRUE
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS borrowers (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        contact VARCHAR(50)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INT AUTO_INCREMENT PRIMARY KEY,
        borrower_id INT,
        book_id INT,
        borrow_date DATE,
        return_date DATE,
        FOREIGN KEY (borrower_id) REFERENCES borrowers(id),
        FOREIGN KEY (book_id) REFERENCES books(id)
    )
    ''')

    # 3. Insert sample data (check for duplicates)
    cursor.execute("INSERT INTO books (id, title, author) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE title = VALUES(title)",
                   (1, 'Book A', 'Author A'))
    cursor.execute("INSERT INTO books (id, title, author) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE title = VALUES(title)",
                   (2, 'Book B', 'Author B'))
    cursor.execute("INSERT INTO borrowers (id, name, contact) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE name = VALUES(name)",
                   (1, 'John Doe', '1234567890'))

    # 4. Borrow a book
    cursor.execute("UPDATE books SET available = FALSE WHERE id = %s AND available = TRUE", (1,))
    cursor.execute("INSERT INTO transactions (borrower_id, book_id, borrow_date) VALUES (%s, %s, %s)",
                   (1, 1, date.today()))

    # Commit changes
    conn.commit()

except mysql.connector.Error as err:
    print(f"Error: {err}")
    conn.rollback()

finally:
    # Close connection
    cursor.close()
    conn.close()
