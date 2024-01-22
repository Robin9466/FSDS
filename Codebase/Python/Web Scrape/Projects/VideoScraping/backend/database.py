# backend/database.py
import mysql.connector

def insert_mysql_data(data):
    # Your MySQL insertion logic here
    connection = mysql.connector.connect(
        host='your_mysql_host',
        user='your_mysql_user',
        password='your_mysql_password',
        database='your_mysql_database'
    )

    cursor = connection.cursor()
    # Execute your INSERT SQL statements here
    cursor.execute("INSERT INTO videos (video_link, likes, title) VALUES (%s, %s, %s)", (data['video_link'], data['likes'], data['title']))
    connection.commit()
    connection.close()


# backend/database.py
import pymongo


def insert_mongodb_data(data):
    # Your MongoDB insertion logic here
    client = pymongo.MongoClient('your_mongodb_connection_string')
    db = client['your_mongodb_database']
    collection = db['your_mongodb_collection']

    # Insert your data into the MongoDB collection
    collection.insert_one(data)
    client.close()
