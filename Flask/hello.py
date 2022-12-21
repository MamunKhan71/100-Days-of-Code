from flask import Flask

app = Flask(__name__)


def decor(fn):
    def wrapper(*args, **kwargs):
        res = fn()
        return "Hello there, " + res + "."

    return wrapper


@app.route('/')
@decor
def sayHello():
    return "Mamun"


if __name__ == "__main__":
    app.run(debug=True)

# -----------------------------
