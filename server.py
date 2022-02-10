from flask import Flask, url_for, request

app = Flask('Sus')

txt = '</br>'.join(['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
                    'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!',
                    'Присоединяйся!'])


@app.route('/')
def start():
    return '<h1>Миссия Колонизация Марса</h1>'


@app.route('/index')
def index():
    return '<h1>И на Марсе будут яблони цвести!</h1>'


@app.route('/promotion')
def promotion():
    return txt


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
                    <div class="promotion">{txt}</div>
                  </body>
                </html>"""


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1 class="form_name">Анкета претендента на участие в миссии</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="name" placeholder="Имя" name="name">
                                    <input type="text" class="form-control" id="surname" placeholder="Фамилия" name="surname">
                                    <br />
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <br />
                                    <div class="form-group">
                                        <label for="classSelect">Образование</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Такое себе</option>
                                          <option>Норм</option>
                                          <option>Выше норм</option>
                                          <option>Супер норм</option>
                                          <option>Мега гипер ультра норм</option>
                                        </select>
                                     </div>
                                    <br />
                                    <div class="form-group form-check">
                                        <label for="form-check">Ваши профессии</label>
                                        <br />
                                        <input type="checkbox" class="form-check-input" name="accept">
                                        <label class="form-check-label">Мемодел</label><br />
                                        <input type="checkbox" class="form-check-input" name="accept">
                                        <label class="form-check-label">Амогус</label><br />
                                        <input type="checkbox" class="form-check-input" name="accept">
                                        <label class="form-check-label">Бэкендер)</label><br />
                                        <input type="checkbox" class="form-check-input" name="accept">
                                        <label class="form-check-label">Фронтендер)</label><br />
                                        <input type="checkbox" class="form-check-input" name="accept">
                                        <label class="form-check-label">Преисполненный в познании</label><br />
                                    </div>
                                    <br />
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <br />
                                    <div class="form-group">
                                        <label for="about">Оно Вам надо?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <br />
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <br />
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <br />
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Выбор сделан</title>
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                  </head>
                  <body>
                    <h1 id="a">Моё предложение: {planet_name}</h1>
                    <h4 id="b">Эта планета далеко от Земли</h4>
                    <h3 id="c">На ней нет воды и атмосферы</h3>
                    <h2 id="d">У неё сильное магнитное поле</h2>
                    <h1 id="e">Планета мечты!)</h1>
                  </body>
                </html>"""


app.run(host='localhost', port=8080, debug=True)
