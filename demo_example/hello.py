from bottle import route, run


@route('/message')
def hello():
    return "Hello World!"

run(host='localhost', port=8080, debug=True)
#run(debug = True,host='localhost',port=8080)
