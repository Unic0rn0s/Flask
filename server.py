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


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс))</h1>
                    <img src="{url_for("static", filename="img/mars.jpg")}">
                    </br>Вот она какая, красная планета)
                  </body>
                </html>"""


@app.route('/promotion_image')
def promotion_image():
    txt = '</br>'.join(['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
                        'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!',
                        'Присоединяйся!'])
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" 
                    href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс))</h1>
                    <img src="{url_for("static", filename="img/mars.jpg")}">
                    <div>{txt}</div>
                  </body>
                </html>"""


app.run(host='localhost', port=8080, debug=True)
