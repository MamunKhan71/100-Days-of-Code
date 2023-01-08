from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    coffee_rating = ["☕️", "☕️☕️", "☕️☕️☕️", "☕️☕️☕️☕️☕️", "☕️☕️☕️☕️☕️"]
    wifi_ratings = ["✘", "✘✘", "✘✘✘", "✘✘✘✘", "✘✘✘✘✘"]
    power_Socket_ratings = ["🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"]
    cafe_name = StringField('Cafe name', validators=[DataRequired()])
    cafe_google_maps = StringField('Cafe Location on Google Maps', validators=[DataRequired()])
    opening_time = StringField('Opening Time EG: 8:00 AM', validators=[DataRequired()])
    closing_time = StringField('Closing Time EG: 9:00 PM', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating', choices=coffee_rating)
    wifi_rating = SelectField('Wifi Strength Rating', choices=wifi_ratings)
    power_socket = SelectField('Power Socket Availability', choices=power_Socket_ratings)
    submit = SubmitField('Submit')


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with coffee_rating of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add')
def add_cafe():
    form = CafeForm()
    # if form.validate_on_submit():

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
        print(cafe_col_length)
    return render_template('cafes.html', cafes=list_of_rows, crLen=cafe_list_length, ccLen=cafe_col_length)


if __name__ == '__main__':
    app.run(debug=True)
