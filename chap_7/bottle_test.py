from bottle import route, run

@route('/')
def home():
    return "It isn't fancy, but it's my hove page"

run(host='localhost', port=9999)

