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

if __name__ == '__main__':
    app.run(debug=True)
