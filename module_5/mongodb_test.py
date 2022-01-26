import pymongo
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.kd1i6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = MongoClient(url)
db =client.pytech
print("-- Pytech COllection List --")
print(db.list_collection_names())



