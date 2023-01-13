import time

from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from sqlalchemy import create_engine, Integer, Float, String, CHAR, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from wtforms import StringField, SubmitField, IntegerField
import os


class form_f(FlaskForm):
    book_id = IntegerField('Book Name')
    submit = SubmitField("Search")


Base = declarative_base()


class editForm(FlaskForm):
    book_edit = IntegerField("book_id")
    submit = SubmitField("update")


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

app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/', methods=["GET", "POST"])
def home():
    session = Session()
    if os.path.isfile("mydb.db"):
        all_books = session.query(book_information).all()
        session.close()
        return render_template("index.html", book_list=all_books, length=len(all_books))
    else:
        return render_template("index.html", book_list=[''], length=0)


@app.route("/add", methods=["GET", "POST"])
def add():
    session = Session()
    if request.method == "POST":
        bookID = int(request.form['book_id'])
        bookName = request.form['book_name']
        bookAuthor = request.form['book_author']
        bookRating = float(request.form['book_rating'])
        if session.query(book_information).filter_by(book_id=bookID).first() is None:
            b1 = book_information(book_id=bookID, book_name=bookName, book_author=bookAuthor, book_rating=bookRating)
            session.add(b1)
            session.commit()
            return redirect(url_for('home'))
        else:
            session.close()
            return "<h1>book_id already exists in the table!</h1>"
    return render_template("add.html")


# @app.route("/query", methods=["GET", "POST"])
# def query():
#     session = Session()
#     newForm = form_f()
#     if request.method == "POST":
#         book = session.query(book_information).filter(book_information.)
#         session.delete(book)
#         session.commit()
#     return render_template("query.html", form_f=newForm)


@app.route('/edit', methods=["GET", "POST"])
def edit():
    session = Session()
    edit_form = editForm()
    selected_book_id = request.args.get('ids')
    book_to_update = session.query(book_information).filter(book_information.book_id == selected_book_id)
    print(book_to_update.book_rating)
    # if request.method == "POST":
    #     print(book_to_update.book_rating)
    #     book_to_update.book_rating = edit_form.data['book_edit']
    #     print(book_to_update.book_rating)
    #     book_to_update = session.query(book_information).filter_by(book_id=selected_book_id)
    #     print(book_to_update)
    return render_template("edit.html", edit_form=edit_form)
    # edit_form = editForm()
    # return render_template("edit.html", edit_form=edit_form)

    # books = session.query(book_information).filter(book_information).first()
    # return render_template("edit.html", books=books, ids=int(ids))


if __name__ == "__main__":
    app.run(debug=True)
