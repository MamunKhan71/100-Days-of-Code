import os
import time

import flask, flash
import werkzeug.security
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user, login_manager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:/Python/100-Days-of-Code/Flask Authentication/users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/files'
db = SQLAlchemy(app)
login = LoginManager()
login.init_app(app)


@login.user_loader
def user_loader(user_id):
    try:
        return User.query.get(int(user_id))
    except ValueError:
        return None


class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        password = generate_password_hash(password=request.form.get('password'), method='pbkdf2:sha256', salt_length=8)
        dbQuery = db.session.query(User).filter_by(email=email).first()
        if dbQuery:
            flash("Email is already registered! Login Instead!")
            return redirect(url_for('register'))
        else:
            new_data = User(
                name=name,
                email=email,
                password=password
            )
            db.session.add(new_data)
            db.session.commit()
            login_user(new_data)
            return redirect(url_for('secrets'))

    return render_template("register.html")


@app.route('/login', methods=["POST", "GET"])
def login():
    error = None
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        user = db.session.query(User).filter_by(email=request.form.get('email')).first()
        if not user:
            flash("Email Doesn't Exist!")
            return redirect(url_for('login'))
        elif not check_password_hash(pwhash=user.password, password=request.form.get('password')):
            flash("Invalid Password!")
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('secrets'))

    return render_template('login.html')


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flask.flash('Logout successfully.')
    return redirect(url_for('home'))


@app.route('/download')
def download():
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'cheat_sheet.pdf')
    if os.path.exists(file_path):
        return send_from_directory(app.config['UPLOAD_FOLDER'], 'cheat_sheet.pdf')
    else:
        return "File Not Found"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
