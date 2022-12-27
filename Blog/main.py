from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/guess/<name>")
def sayHi(name):
    parameter = {
        'name': {name}
    }
    web = requests.get(url=f"https://api.genderize.io/", params=parameter).json()
    gender = web['gender']
    ageWeb = requests.get(url="https://api.agify.io/", params=parameter).json()
    age = ageWeb['age']

    return render_template("index.html", name=name, gen=gender, age=age)


if __name__ == "__main__":
    app.run()
