from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    context = {'title': 'Эластико'}
    return render_template('main.html', **context)


@app.route('/catalog/')
def catalog():
    context = {'title': 'Каталог'}
    return render_template('catalog.html', **context)


@app.route('/products/')
def product():
    context = {'title': 'Порося'}
    return render_template('products.html', **context)


@app.route('/contacts/')
def contacts():
    context = {'title': 'Контакты'}
    return render_template('contacts.html', **context)


@app.route('/feedback/')
def feedback():
    context = {'title': 'Обратная связь'}
    return render_template('feedback.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
