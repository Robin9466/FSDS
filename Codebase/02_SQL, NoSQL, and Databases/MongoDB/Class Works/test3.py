from pymongo.mongo_client import MongoClient


uri = "mongodb+srv://robinrajinfo:QC1rWa7gfnBa22mC@cluster0.stbnerj.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

data = [
    {
        "item": "canvas",
        "qty": 100,
        "size": {"h": 28, "w": 35.5, "uom": "cm"},
        "status": "A"
    },
    {
        "item": "journal",
        "qty": 25,
        "size": {"h": 14, "w": 21, "uom": "cm"},
        "status": "A"
    },
    {
        "item": "mat",
        "qty": 85,
        "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
        "status": "A"
    },
    {
        "item": "mousepad",
        "qty": 25,
        "size": {"h": 19, "w": 22.85, "uom": "cm"},
        "status": "A"
    },
    {
        "item": "notebook",
        "qty": 50,
        "size": {"h": 8.5, "w": 11, "uom": "in"},
        "status": "P"
    },
    {
        "item": "paper",
        "qty": 100,
        "size": {"h": 8.5, "w": 11, "uom": "in"},
        "status": "D"
    },
    {
        "item": "planner",
        "qty": 75,
        "size": {"h": 22.85, "w": 30, "uom": "cm"},
        "status": "O"
    }
]
database = client['inventory']
collection = database['table']
#collection.insert_many(data)
#d = collection.find({'status': 'A'})
#d = collection.find({'status': {'$in' : ['A', 'P']}})
#d = collection.find({'status': {"$gt" : "C"}})
#d = collection.find({'qty': {"$gte" : 75}})
#d = collection.find({'item': 'sketch pad'}, {'qty': 85} )
#d = collection.find({'item': 'sketch pad', 'qty': {"$gte" : 75}})
#d = collection.find({'$or' : [{'item': 'sketch pad'}, {'qty': {"$gte" : 75}}]})
#collection.update_one({'item': 'canvas'}, {'$set' : {'item': 'robin'}})
collection.delete_one({'item': 'robin'})
d = collection.find({'item': 'robin'})
for i in d:
    print(i)
