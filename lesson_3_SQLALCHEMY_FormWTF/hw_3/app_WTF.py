# Создать форму для регистрации пользователей на сайте.
# Форма должна содержать поля "Имя", "Фамилия", "Email",
# "Пароль" и кнопку "Зарегистрироваться".
# При отправке формы данные должны сохраняться в базе
# данных, а пароль должен быть зашифрован.
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect
from lesson_3_SQLALCHEMY_FormWTF.hw_3.reg_form import RegistrationForm
from lesson_3_SQLALCHEMY_FormWTF.hw_3.models_form import db, User

app = Flask(__name__)
app.config['SECRET_KEY'] = b'd6975365874d1f78a752e98c853c5388664958d8370b357af2a9292c91a2dfac'
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reg_DB.db'
db.init_app(app)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('OK')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']
        # print(firstname, lastname, email, password)
        print(form.data)
        # new_user = User(form.data)
        new_user = User(firstname, lastname, email, password)
        db.session.add(new_user)
        db.session.commit()
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
