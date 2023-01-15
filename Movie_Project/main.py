from pprint import pprint

import pytest as pytest
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import create_engine
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests

data = []
app = Flask(__name__)

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

##CREATE DB
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:/100days/64 Day 64 - Advanced -My Top 10 Movies Website/Movie_Project/movie_db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CREATE TABLE
class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(250), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

    def __init__(self, title, year, description, rating, ranking, review, img_url):
        self.title = title
        self.year = year
        self.description = description
        self.rating = rating
        self.ranking = ranking
        self.review = review
        self.img_url = img_url

    def __repr__(self):
        return f"{self.id} {self.title} {self.year} {self.description} {self.rating} {self.ranking} {self.review} {self.img_url}"


class AddMovie(FlaskForm):
    new_movie_title = StringField("Movie Title")
    button = SubmitField("Add Movie")


with app.app_context():
    db.create_all()
    # new_movie = Movie(
    #     title="Phone Booth",
    #     year=2002,
    #     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's "
    #                 "sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to "
    #                 "a jaw-dropping climax.",
    #     rating=7.3,
    #     ranking=10,
    #     review="My favourite character was the caller.",
    #     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
    # )
    # existing_movie = Movie.query.filter_by(title=new_movie.title).first()
    # if not existing_movie:
    #     db.session.add(new_movie)
    #     db.session.commit()


class RateMovieForm(FlaskForm):
    rating = FloatField("Your Rating Out of 10 e.g 7.5")
    review = StringField("Your Review")
    done = SubmitField("Done")


@app.route('/')
def home():
    movie = db.session.query(Movie).all()
    return render_template("index.html", movie=movie)


@app.route('/edit', methods=["GET", "POST"])
def edit():
    form = RateMovieForm()
    movie_id = int(request.args.get("id"))
    movie_details = db.session.query(Movie).filter(movie_id == Movie.id).first()
    if request.args.get("delete") == "YES":
        movie_delete = Movie.query.get(movie_id)
        db.session.delete(movie_delete)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        if request.method == "POST":
            if form.validate_on_submit():
                movie_details.rating = form.rating.data
                movie_details.review = form.review.data
                db.session.commit()
                return redirect(url_for('home'))

    return render_template("edit.html", form=form, movie_id=movie_details)


@app.route('/add', methods=["GET", "POST"])
def fetch_movie():
    global data
    movie = AddMovie()
    if request.method == "POST":
        parameter = {
            "api_key": "d92afb5b1311f973b1e4d88ab1b1d9c7",
            "query": movie.new_movie_title.data,
            "year": 1,
        }
        data = requests.get(url="https://api.themoviedb.org/3/search/movie", params=parameter).json()["results"]
        return render_template("add.html", form=data, add="False")

    return render_template("add.html", add="True", form=movie)


@app.route('/movie_adder', methods=["GET", "POST"])
def movie_adder():
    form = RateMovieForm()
    global data
    fetch_id = int(request.args.get("m_id"))
    for dst in data:
        if dst["id"] == fetch_id:
            new_m = Movie(
                title=dst["original_title"],
                year=dst["release_date"],
                description=dst["overview"],
                rating=dst["vote_average"],
                ranking=" ",
                review=" ",
                img_url=f"https://www.themoviedb.org/t/p/original{dst['poster_path']}"
            )
            db.session.add(new_m)
            db.session.commit()
            movie_details = db.session.query(Movie).filter(fetch_id == Movie.id).first()
            if request.args.get("delete") == "YES":
                movie_delete = Movie.query.get(movie_id)
                db.session.delete(movie_delete)
                db.session.commit()
                return redirect(url_for('home'))
            else:
                if request.method == "POST":
                    if form.validate_on_submit():
                        movie_details.rating = form.rating.data
                        movie_details.review = form.review.data
                        db.session.commit()
                        return redirect(url_for('home'))

            return render_template("edit.html", form=form, movie_id=movie_details)


if __name__ == "__main__":
    app.run(debug=True)
