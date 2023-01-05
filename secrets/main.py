from flask import Flask, render_template

from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)
app.secret_key = "any-string-you-want-just-keep-it-secret"


class LoginForm(FlaskForm):
    email = StringField(label='Email ', validators=[Email()])
    password = PasswordField(label='Password ', validators=[Length(min=8)])
    submit = SubmitField(label="Log In")


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@123.com" and login_form.password.data == "admin123":
            return render_template("success.html")
        else:
            return render_template("denied.html")

    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
