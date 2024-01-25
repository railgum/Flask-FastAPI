# Создать базу данных для хранения информации о книгах в библиотеке.
# База данных должна содержать две таблицы: "Книги" и "Авторы".
# В таблице "Книги" должны быть следующие поля: id, название, год издания,
# количество экземпляров и id автора.
# В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
# Необходимо создать связь между таблицами "Книги" и "Авторы".
# Написать функцию-обработчик, которая будет выводить список всех книг с
# указанием их авторов.

from flask import Flask, render_template, url_for
import random as rnd
import string
from random import randint as RI
from lesson_3_SQLALCHEMY_FormWTF.hw_3.models import db, Book, Author

# from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hw_DB.db'
db.init_app(app)
letter = string.ascii_lowercase
vowels = 'aeiouy'
MIN_NAME = 4
MAX_NAME = 7


@app.route('/')
def index():
    context = {'title': 'Кныжки'}
    return render_template('index.html', **context)


def generate_name():
    size = rnd.randint(MIN_NAME, MAX_NAME)
    name = rnd.sample(letter, size - 1)
    name.append(rnd.choice(vowels))
    rnd.shuffle(name)
    name = ''.join(name).title()
    return name


# Попытка исправить ошибку 'No such table'
# @app.before_request
# def create_tables():
#     db.create_all()
@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('OK')


@app.cli.command('fill-a')
def fill_authors():
    count = 5
    for author in range(1, count + 1):
        new_author = Author(firstname=f'{generate_name()}',
                            lastname=f'{generate_name()}')
        db.session.add(new_author)
    db.session.commit()
    print('Table authors OK')


@app.cli.command('fill-b')
def fill_books():
    count = 15
    for book in range(1, count + 1):
        author = Author.query.get(RI(1, 5))
        new_book = Book(name=f'Book-{book}', year_public=RI(1600, 2024), number_copies=RI(1, 100),
                        author=author)
        db.session.add(new_book)
    db.session.commit()
    print('Table books OK')


@app.route('/books/')
def show_books():
    books = Book.query.all()
    authors = Author.query.all()
    context = {'title': 'Books',
               'books': books,
               'authors': authors}
    print(books, authors)
    return render_template('show_books.html', **context)


if __name__ == '__main__':
    # Попытка исправить ошибку 'No such table'
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)
