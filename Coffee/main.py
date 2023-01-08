import time

from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    coffee_rating = ["☕️", "☕️☕️", "☕️☕️☕️", "☕️☕️☕️☕️", "☕️☕️☕️☕️☕️"]
    wifi_ratings = ["✘", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"]
    power_Socket_ratings = ["✘", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"]
    cafe_name = StringField('Cafe name', validators=[DataRequired()])
    cafe_google_maps = StringField('Cafe Location on Google Maps', validators=[URL()])
    opening_time = StringField('Opening Time EG: 8:00 AM', validators=[DataRequired()])
    closing_time = StringField('Closing Time EG: 9:00 PM', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating', choices=coffee_rating)
    wifi_rating = SelectField('Wifi Strength Rating', choices=wifi_ratings)
    power_socket = SelectField('Power Socket Availability', choices=power_Socket_ratings)
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_list = f"\n{form.cafe_name.data}, {form.cafe_google_maps.data}, {form.opening_time.data}, {form.closing_time.data},{form.coffee_rating.data}, {form.wifi_rating.data}, {form.power_socket.data}"
        with open(file="D:/Coffee/datas.csv", mode="a+", encoding='utf8') as file:
            file.write(new_list)
            flash('Data Added Successfully!')

        time.sleep(1)
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('D:/Coffee/datas.csv', newline='', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        cafe_list_length = len(list_of_rows)
        cafe_col_length = len(list_of_rows[0])
    return render_template('cafes.html', cafes=list_of_rows, crLen=cafe_list_length, ccLen=cafe_col_length)


if __name__ == '__main__':
    app.run(debug=True)
