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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
