from flask import Flask

app = Flask(__name__)


@app.route("/")
def say_hi():
    return "Hello Hi!"


@app.route("/<users>")
def greet(users):
    return f"Hello Hi {users}"


if __name__ == "__main__":
    app.run(debug=True)
    say_hi()
