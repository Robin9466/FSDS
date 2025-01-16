"""
1 . Write a program to insert a record in sql table via api
2.  Write a program to update a record via api
3 . Write a program to delete a record via api
4 . Write a program to fetch a record via api
"""

# 1 . Write a program to insert a record in sql table via api

from flask import Flask, request, jsonify
import mysql.connector as conn
from bson import ObjectId

from api_pymongo_task import collection

app = Flask(__name__)

mydb = conn.connect(host="localhost", user="root",passwd = "*K37759@Others#")
cursor = mydb.cursor()
cursor.execute("create database if not exists taskdb")
cursor.execute("create table if not exists taskdb.tasktable(name varchar(30), number int)")

@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        name = request.json['name']
        number = request.json['number']
        cursor.execute("insert into taskdb.tasktable values(%s, %s)", (name, number))
        mydb.commit()
        return jsonify(str('successfully inserted'))

@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        get_name = request.json['get_name']
        try:
            # Print the SQL query for debugging
            print(f"Executing SQL: UPDATE taskdb.tasktable SET number = number + 100 WHERE name = {get_name}")

            # Execute the SQL query
            cursor.execute("UPDATE taskdb.tasktable SET number = number + 100 WHERE name = %s", (get_name,))
            mydb.commit()

            return jsonify(str('updated successfully'))
        except Exception as e:
            mydb.rollback()  # Rollback the transaction in case of an error
            return jsonify(str(f'Error: {e}'))


@app.route("/delete", methods=['POST'])
def delete():
    if request.method == 'POST':
        name_del = request.json['name_del']
        cursor.execute("delete from taskdb.tasktable where name = %s", (name_del,))
        mydb.commit()
        return jsonify(str("deleted successfully"))

@app.route("/fetch", methods=["GET", "POST"])
def fetch():
    cursor.execute("select * from taskdb.tasktable")
    list = []
    for i in cursor.fetchall():
        list.append(list)
    return jsonify(str(list))


if __name__ == '__main__':
    app.run()