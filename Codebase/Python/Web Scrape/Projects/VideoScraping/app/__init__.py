from flask import Flask
from flask_mysqldb import MySQL
from pymongo import MongoClient

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '*K37759@Others#'
app.config['MYSQL_DB'] = 'your_mysql_db'

# MongoDB Configuration
client = MongoClient('mongodb://localhost:27017/')
db = client['your_mongo_db']
