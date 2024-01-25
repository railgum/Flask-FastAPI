from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    book = db.relationship('Book', backref='author', lazy=True)

    # def __repr__(self):
    #     return f'Author({self.firstname}, {self.lastname})'


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    year_public = db.Column(db.Integer, nullable=False)
    number_copies = db.Column(db.Integer)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)

    # def __repr__(self):
    #     return f'Book({self.name}, {self.year_public})'



