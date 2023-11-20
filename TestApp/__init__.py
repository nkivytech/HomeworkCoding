from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(80), nullable=False)
    publisher = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"{self.book_name} , {self.author} , {self.publisher}"

@app.route('/')
def index():
    return 'Hello!'

@app.route('/books')
def returnBooks():

    books = Book.query.all()
    output = []
    for book in books:
        output.append({"id": book.id, "book_name": book.book_name, "author": book.author, "publisher": book.publisher})
    return {"books": output}

@app.route('/books/<id>')
def returnBook(id):

    book = Book.query.get_or_404(id)
    return {"book_name": book.book_name, "author": book.author, "publisher": book.publisher}

@app.route('/books', methods=['POST'])
def addBook():
    book = Book(id = request.json['id'], book_name = request.json['book_name'],author = request.json['author'], publisher = request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}

@app.route('/books/<id>', methods = ['DELETE'])
def deleteBook(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return {"message": "Book deleted "}
