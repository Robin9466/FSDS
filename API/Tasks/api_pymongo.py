from flask import Flask, request, jsonify
import pymongo
from urllib.parse import quote_plus
from bson import ObjectId

app = Flask(__name__)

# Escape username and password
username = "robinrajinfo"
password = "g@vrD!4R6hTF$FH"
escaped_username = quote_plus(username)
escaped_password = quote_plus(password)

# Construct the MongoDB connection URI
mongo_uri = f"mongodb+srv://{escaped_username}:{escaped_password}@cluster0.stbnerj.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(mongo_uri)
database = client['taskdb']
collection = database['taskcollection']

# 1 . Write a program to insert a record in mongodb table via api
@app.route("/insert", methods=['POST'])
def insert():
    if request.method == 'POST':
        name = request.json['name']
        number = request.json['number']
        collection.insert_one({name: number})
        return jsonify(str("successfully inserted"))

# 2.  Write a program to update a record via api
@app.route("/update", methods=['POST'])
def update():
    if request.method == 'POST':
        updated_name = request.json['name']
        print(f'updating record for name: {updated_name}')
        update_data = {'$set': {'number': 112}}
        result = collection.update_one({'name': updated_name}, update_data)
        if result.modified_count>0:
            return jsonify({"message": "successfully updated"})
        else:
            return jsonify({"message": "not modified"})


# 3 . Write a program to delete a record via api
@app.route("/delete", methods=['POST'])
def delete():
    if request.method == 'POST':
        # Assuming 'name' is a unique identifier for your records
        name_to_delete = request.json.get('name')

        # Check if 'name' is provided in the request
        if not name_to_delete:
            return jsonify({"message": "Error: 'name' is missing in the request"}), 400

        # Create a filter for the delete operation
        filter_query = {'name': name_to_delete}
        print(f"Deleting record for name: {name_to_delete}")
        result = collection.delete_one(filter_query)
        print(f"Deleted count: {result.deleted_count}")

        # Check if the deletion was successful
        if result.deleted_count > 0:
            return jsonify({"message": "successfully deleted"})
        else:
            return jsonify({"message": "record not found"})

# 4 . Write a program to fetch a record via api
@app.route("/fetch", methods=['POST'])
def fetch():
    if request.method == ['POST']:
        # Example: Fetch all documents from the collection
        documents = collection.find()

        for document in documents:
            print(document)


if __name__ == '__main__':
    app.run()
