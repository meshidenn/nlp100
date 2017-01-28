from bottle import route, run, template
from pymongo import MongoClient

conn = MongoClient('localhost', 27017)
db = conn.artist
coll = db.c7_collection


def find_by_name(name):
    result = []
    for doc in coll.find({'name': name}):
        result.append(doc)
    return result


@route('/artist/<name>')
def index(name):
    return template('<b>{{data}}</b>!', data=find_by_name(name))

run(host='localhost', port=9999)
