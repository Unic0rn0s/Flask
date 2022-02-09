from flask import Flask

app = Flask('Sus')


@app.route('/')
def index():
    return '<h1>Миссия Колонизация Марса</h1>'


@app.route('/index')
def func1():
    return '<h1>И на Марсе будут яблони цвести!</h1>'


app.run(host='localhost', port=8080, debug=True)
