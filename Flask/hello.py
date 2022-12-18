from flask import Flask

app = Flask(__name__)


def bold_maker(function):
    def wrapper_f(*args):
        return f"<b>{args[0]}</b>"

    return wrapper_f


@app.route("/")
def say_hi():
    return "Hello Hi!"


@app.route("/bye")
@bold_maker
def greet(users):
    return f"Hello Hi {users}"


if __name__ == "__main__":
    app.run(debug=True)
    say_hi()

greet("Mamun")