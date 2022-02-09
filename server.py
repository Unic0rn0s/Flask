from flask import Flask, url_for

app = Flask('Sus')


@app.route('/')
def start():
    return '<h1>Миссия Колонизация Марса</h1>'


@app.route('/index')
def index():
    return '<h1>И на Марсе будут яблони цвести!</h1>'


@app.route('/promotion')
def promotion():
    txt = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
           'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!',
           'Присоединяйся!']
    return '</br>'.join(txt)


@app.route('/user/<int:id>')
def func2(id):
    return str(id)


@app.route('/rianna')
def rianna():
    return f'<img src="{url_for("static", filename="rianna.jpeg")}">'


app.run(host='localhost', port=8080, debug=True)
