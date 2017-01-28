from bottle import route, run, template

import pymongo

 

@route('/')

def home():
    conn = pymongo.MongoClient()
    db = conn.artist
    col = db.c7_collection

    line = col.find_one()
    count = col.count()

    return template('<b>{{line}}</b>!<br/><br/>--- Access count ---<br/>{{count}}', line=line,count=count)

run(host='localhost', port=9999)


