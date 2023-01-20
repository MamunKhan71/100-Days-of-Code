from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

## Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:/Python/100-Days-of-Code/cafe-api-start/cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

db = SQLAlchemy(app)


## Cafe TABLE Configuration
class Cafe(db.Model):
    __tablename__ = "cafe"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record
@app.route('/random')
def random_route():
    new_db = db.session.query(Cafe).all()
    random_cafe = random.choice(new_db)
    return jsonify(
        can_take_calls=random_cafe.can_take_calls,
        coffee_price=random_cafe.coffee_price,
        has_sockets=random_cafe.has_sockets,
        has_toilet=random_cafe.has_toilet,
        has_wifi=random_cafe.has_wifi,
        id=random_cafe.id,
        img_url=random_cafe.img_url,
        location=random_cafe.location,
        map_url=random_cafe.map_url,
        name=random_cafe.name,
        seats=random_cafe.seats,
    )


## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
