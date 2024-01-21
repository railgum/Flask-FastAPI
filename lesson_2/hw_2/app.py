from flask import Flask, flash, render_template, request, url_for, redirect, session, make_response
from pathlib import PurePath, Path
from werkzeug.utils import secure_filename

# Задание 9
# Создать страницу, на которой будет форма для ввода имени и электронной почты
# При отправке которой будет создан cookie файл с данными пользователя
# Также будет произведено перенаправление на страницу
# приветствия, где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка "Выйти"
# При нажатии на кнопку будет удален cookie файл с данными пользователя
# и произведено перенаправление на страницу ввода имени и электронной почты.\

app = Flask(__name__)
app.secret_key = '1522d03851d24a5c29371855db251fc384de2a21ed2de4af2d1d711e6d1b8dc3'


@app.route('/')
def index():
    if 'username' in session:
        context = {'username': session['username'],
                   'title': 'Приветствие'}
        return render_template('hello.html', **context)
    else:
        return redirect(url_for('login'))


@app.route('/login/', methods=['GET', 'POST'])
def login():
    context = {'title': 'Авторизация'}
    if request.method == 'POST':
        session['username'] = request.form.get('username') or 'NoName'
        return redirect(url_for('index'))
    return render_template('sign_in.html', **context)


@app.route('/logout/')
def logout():
    session.pop('username', None)
    session.pop('email', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
