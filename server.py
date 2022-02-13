from flask import Flask, url_for, request
import os
import shutil

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


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Результаты</title>
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                  </head>
                  <body>
                    <h1 id="black">Результаты отбора</h1>
                    <h2 id="black">Претендента на участие в миссии {nickname}:</h2>
                    <h3 id="rating">Поздравляем! Ваш рейтинг после {level} этапа обора составляет {rating}!</h3>
                    <h1 id="gl">Желаем Вам никогда больше не возвращаться на Землю!</h1>
                  </body>
                </html>"""


@app.route('/carousel')
def carousel():
    return """<!doctype html>
                <html lang="ru">
                <head>
                    <!-- Required meta tags -->
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <meta http-equiv="X-UA-Compatible" content="ie=edge">
                
                    <!-- Bootstrap CSS -->
                    <link rel="stylesheet"
                     href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" 
                    integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" 
                    crossorigin="anonymous">
                    <!-- Google fonts -->
                    <link href="https://fonts.googleapis.com/css?family=Roboto:300,400,700&display=swap" 
                    rel="stylesheet">
                
                    <title>Пейзажи Марса))</title>
                </head>
                <body>
                    <!-- Carousel in a container -->
                <div class="container">
                        <div id="carousel-basic" class="carousel slide" data-ride="carousel">
                            <!-- Indicators -->
                            <ol class="carousel-indicators">
                                <li data-target="carousel-basic" data-slide-to="0" class="active"></li>
                                <li data-target="carousel-basic" data-slide-to="1"></li>
                                <li data-target="carousel-basic" data-slide-to="2"></li>
                                <li data-target="carousel-basic" data-slide-to="3"></li>
                                <li data-target="carousel-basic" data-slide-to="4"></li>
                                <li data-target="carousel-basic" data-slide-to="5"></li>
                                <li data-target="carousel-basic" data-slide-to="6"></li>
                            </ol>
                
                            <!-- Wrapper -->
                            <div class="carousel-inner" role="listbox">
                                <div class="carousel-item active">
                                    <img src="static/img/1.jpg" alt="" class="img-fluid">
                                    <div class="carousel-caption">
                                    </div>
                                </div>
                                <div class="carousel-item">
                                    <img src="static/img/2.jpg" alt="" class="img-fluid">
                                </div>
                                <div class="carousel-item">
                                    <img src="static/img/3.jpg" alt="" class="img-fluid">
                                </div>
                                <div class="carousel-item">
                                    <img src="static/img/4.jpg" alt="" class="img-fluid">
                                </div>
                                <div class="carousel-item">
                                    <img src="static/img/5.jpg" alt="" class="img-fluid">
                                </div>
                                <div class="carousel-item">
                                    <img src="static/img/6.jpg" alt="" class="img-fluid">
                                </div>
                            </div>
                
                            <!-- Controls -->
                            <a class="carousel-control-prev" href="#carousel-basic" role="button" data-slide="prev">
                                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                                <span class="sr-only">Назад</span>
                            </a>
                            <a class="carousel-control-next" href="#carousel-basic" role="button" data-slide="next">
                                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                                <span class="sr-only">Вперед</span>
                            </a>
                        </div>
                
                        <!-- Content -->
                
                    </div>
                
                    <!-- Optional JavaScript -->
                    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
                    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" 
                    integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" 
                    crossorigin="anonymous"></script>
                    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" 
                    integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" 
                    crossorigin="anonymous"></script>
                    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" 
                    integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" 
                    crossorigin="anonymous"></script>
                </body>
                </html>"""


@app.route('/load_img', methods=['POST', 'GET'])
def load_img():
    if request.method == 'GET':
        return """<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Загрузка изображения</title>
                      </head>
                      <body>
                        <div class="container">
                            <div class="row">
                                <label>Загрузить файл:</label>
                                <input type="file" id="file" name="file" />
                            </div>
                            <div class="row">
                                <span id="output"></span>
                            </div>
                        </div>
                        <script>
                            function handleFileSelect(evt) {
                                var file = evt.target.files; // FileList object
                                var f = file[0];
                                // Only process image files.
                                if (!f.type.match('image.*')) {
                                    alert("Image only please....");
                                }
                                var reader = new FileReader();
                                // Closure to capture the file information.
                                reader.onload = (function(theFile) {
                                    return function(e) {
                                        // Render thumbnail.
                                        var span = document.createElement('span');
                                        span.innerHTML = ['<img class="thumb" title="', escape(theFile.name), '" src="', e.target.result, '" />'].join('');
                                        document.getElementById('output').insertBefore(span, null);
                                    };
                                })(f);
                                // Read in the image file as a data URL.
                                reader.readAsDataURL(f);
                            }
                            document.getElementById('file').addEventListener('change', handleFileSelect, false);
                            </script>
                      </body>
                    </html>"""


app.run(host='localhost', port=8080, debug=True)
