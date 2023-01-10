from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy, ForeignKey

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///D:\library-start\project.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()
all_books = []


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'

    db.create_all()


new_book = Book(id=1, title="Harry Porter", author="J.K Rowling", rating=9.3)
db.session.add(new_book)
db.session.commit()
# @app.route('/')
# def home():
#     length = len(all_books)
#     return render_template("index.html", data=all_books, length=length)
#
#
# @app.route("/add", methods=["GET", "POST"])
# def add():
#     return render_template('add.html')
#
#
# @app.route('/add_data', methods=["POST"])
# def received_data():
#     name = request.form['book_name']
#     auth = request.form['book_author']
#     rating = request.form['book_rating']
#     new_dictionary = {
#         "title": name,
#         "author": auth,
#         "rating": rating,
#     }
#     all_books.append(new_dictionary)
#     return redirect(url_for('success'))
#
#
# @app.route('/success')
# def success():
#     return "<h1> Data Added Successfully! </h1>"
#
#
if __name__ == "__main__":
    app.run(debug=True)
