from pprint import pprint

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

## Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:/Python/100-Days-of-Code/cafe-api-start/cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

db = SQLAlchemy(app)

db_all = []


## Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

    def __init__(self, name, map_url, img_url, location, seats, has_toilet, has_wifi, has_sockets, can_take_calls,
                 coffee_price):
        self.name = name
        self.map_url = map_url
        self.img_url = img_url
        self.location = location
        self.seats = seats
        self.has_toilet = has_toilet
        self.has_wifi = has_wifi
        self.has_sockets = has_sockets
        self.can_take_calls = can_take_calls
        self.coffee_price = coffee_price


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
    return jsonify(cafe=random_cafe.to_dict())


@app.route('/all')
def all_cafe():
    global db_all
    data = db.session.query(Cafe).all()
    for datas in data:
        new_data = datas.to_dict()
        db_all.append(new_data)
    return jsonify(cafes=db_all)


@app.route('/search', methods=["GET", "POST"])
def search():
    argument = request.args.get("loc")
    try:
        search_data = db.session.query(Cafe).filter_by(location=argument).first().to_dict()
        return jsonify(search_data)
    except:
        return jsonify(
            error={
                "Not Found": "Sorry, we don't have a cafe at that location."
            }
        )


## HTTP POST - Create Record
@app.route('/add', methods=["GET", "POST"])
def add():
    name = request.form.get("name")
    map_url = request.form.get("map_url")
    img_url = request.form.get("img_url")
    location = request.form.get("location")
    seats = request.form.get("seats")
    has_toilet = bool(request.form.get("has_toilet"))
    has_wifi = bool(request.form.get("has_wifi"))
    has_sockets = bool(request.form.get("has_sockets"))
    can_take_calls = bool(request.form.get("can_take_calls"))
    coffee_price = request.form.get("coffee_price")

    cafe = Cafe(name=name, map_url=map_url, img_url=img_url, location=location, seats=seats, has_toilet=has_toilet,
                has_wifi=has_wifi, has_sockets=has_sockets, can_take_calls=can_take_calls,
                coffee_price=coffee_price)

    try:
        db.session.add(cafe)
        db.session.commit()
        return jsonify(response={
            "Success": f"Successfully Added The Cafe {cafe}!"
        })
    except:
        return jsonify(response={
            "Error": "Something Went Wrong!"
        })


## HTTP PUT/PATCH - Update Record
@app.route('/update-price/<cafe_id>', methods=['PATCH'])
def update_price(cafe_id):
    try:
        new_value = db.session.query(Cafe).filter_by(id=cafe_id).first()
        new_value.coffee_price = request.args.get("new_price")
        db.session.commit()
        return jsonify(
            Success="Data updated successfully!"
        )
    except:
        return jsonify(error={
            "Not Found": "Sorry! The cafe with that id not found!"
        })


@app.route('/report-closed/<cafe_id>', methods=['DELETE'])
def delete(cafe_id):
    api_key = request.args.get("api-key")
    print(api_key)
    if api_key == "mkmamun031":
        try:
            data = db.session.query(Cafe).filter_by(id=cafe_id).first()
            print(data)
            db.session.delete(data)
            db.session.commit()
            return jsonify(Success="Data Deleted Successfully!")
        except:
            return jsonify(error={
                "Not Found": "Sorry! The cafe with that id not found!"
            })
    else:
        return jsonify(error="Sorry that method is not allowed. Make sure you have the right API-KEY!")


if __name__ == '__main__':
    app.run(debug=True)
