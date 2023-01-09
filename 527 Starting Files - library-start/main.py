from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

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
