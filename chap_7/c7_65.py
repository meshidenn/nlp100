import pymongo
import json

def set_mongo(json_datas):
    client = pymongo.MongoClient()
    artist = client.artist
    collection = artist.c7_collection
    for json_data in json_datas:
        collection.insert_one(json_data)

    print(collection.find_one())

def set_index(collection_name):
    client = pymongo.MongoClient()
    db = client.artist
    collection = db.c7_collection
    print(collection.find_one())
    collection.create_index([('aliases.name',1)])
    collection.create_index([('rating.value',1)])


def main():
    json_datas = []
    kv_data = {}
    
#    with open('artist.json','r') as f:
#        for line in f:
#            json_data = json.loads(line)
#            json_datas.append(json_data)

#    set_mongo(json_datas)

    name = 'artist'

    set_index(name)

    return(json_datas)

if __name__ == '__main__':
    json_datas = main()
