import pymongo
import json

client = pymongo.MongoClient()
db = client.artist
collection = db.c7_collection

print(list(collection.find({'tags.value':'dance'}).sort('rating.count',-1).limit(10)))
