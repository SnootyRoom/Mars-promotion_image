from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', title='Домашняя страница')


@app.route('/promotion')
def promotion():
    return render_template('promotion.html', title='Рекламная кампания')


@app.route('/image_mars')
def img_mars():
    return render_template('img_mars.html', title='Привет, Марс!')


@app.route('/promotion_image')
def bootstrap():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="/static/img/MARS.png">
                     <p class="one">Человечество вырастает из детства.</p>
     <p class="two" >Человечеству мала одна планета.</p>
     <p class="three" >Мы сделаем обитаемыми безжизненные пока планеты.</p>
     <p class="four" >И начнем с Марса!</p>
     <p class="five">Присоединяйся!</p>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
