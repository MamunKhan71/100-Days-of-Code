from flask import Flask, render_template, request, redirect, url_for
import sqlite3
app = Flask(__name__)
db = sqlite3.connect("D:/527 Starting Files - library-start/books-collection.db")
cursor = db.cursor()
cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
all_books = []


@app.route('/')
def home():
    length = len(all_books)
    return render_template("index.html", data=all_books, length=length)


@app.route("/add", methods=["GET", "POST"])
def add():
    return render_template('add.html')


@app.route('/add_data', methods=["POST"])
def received_data():
    name = request.form['book_name']
    auth = request.form['book_author']
    rating = request.form['book_rating']
    new_dictionary = {
        "title": name,
        "author": auth,
        "rating": rating,
    }
    all_books.append(new_dictionary)
    return redirect(url_for('success'))


@app.route('/success')
def success():
    return "<h1> Data Added Successfully! </h1>"


if __name__ == "__main__":
    app.run(debug=True)
