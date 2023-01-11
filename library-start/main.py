from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from sqlalchemy import create_engine, Integer, Float, String, CHAR, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from wtforms import StringField, SubmitField


class form(FlaskForm):
    book_name = StringField('Book Name')
    submit = SubmitField("Search")


Base = declarative_base()


class book_information(Base):
    __tablename__ = "book_info"
    book_id = Column("book_id", Integer, primary_key=True)
    book_name = Column("book_name", String, nullable=False)
    book_author = Column("book_author", String, nullable=False)
    book_rating = Column("book_rating", Float, nullable=False)

    def __init__(self, book_id, book_name, book_author, book_rating):
        self.book_id = book_id
        self.book_name = book_name
        self.book_author = book_author
        self.book_rating = book_rating

    def __repr__(self):
        return f"{self.book_name}"


engine = create_engine(url="sqlite:///D:\Starting Files\mydb.db", echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/')
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        bookID = int(request.form['book_id'])
        bookName = request.form['book_name']
        bookAuthor = request.form['book_author']
        bookRating = float(request.form['book_rating'])
        b1 = book_information(book_id=bookID, book_name=bookName, book_author=bookAuthor, book_rating=bookRating)
        session.add(b1)
        session.commit()
        return "<h1> Data Added Successfully! </h1>"
    return render_template("add.html")


@app.route("/query", methods=["GET", "POST"])
def query():
    newForm = form()
    if request.method == "POST":
        data = session.query(book_information).filter(book_information.book_name.like(newForm.book_name.data))
        return f"<hr><h2>Search Result: {data[0].book_author}</h2><hr>"
    return render_template("query.html", form=newForm)


if __name__ == "__main__":
    app.run(debug=True)
