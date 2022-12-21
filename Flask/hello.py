import time

from flask import Flask

app = Flask(__name__)


<<<<<<< HEAD
def decor(fn):
    def wrapper(*args, **kwargs):
        res = fn()
        return "Hello there, " + res + "."
=======
#
# def bold_maker(function):
#     def wrapper_f():
#         return "<b>" + function() + "</b>"
#
#     return wrapper_f
#
#
# def emphasis_maker(function):
#     def wrapper_f():
#         return "<em>" + function() + "</em>"
#
#     return wrapper_f
#
#
# def underline_maker(function):
#     def wrapper_f():
#         return "<u>" + function() + "</u>"
#     return wrapper_f
#
#
# @app.route("/hi")
# @bold_maker
# @underline_maker
# @emphasis_maker
# def say_hi():
#     return "Hello Hi!"

# -----------------------------
def print_dec(function):
    def wrapper(*args, **kwargs):
        name = args[0]
        return f"<p>Hello there </p><br><p>My name is {function}</p>"
>>>>>>> 87fa328bf8c82459659f25272257e054cd5081ab

    return wrapper


<<<<<<< HEAD
@app.route('/')
@decor
def sayHello():
    return "Mamun"


if __name__ == "__main__":
    app.run(debug=True)

# -----------------------------
=======
@app.route("/hi")
@print_dec
def prints(name):
    return name


prints("Mamun")

if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> 87fa328bf8c82459659f25272257e054cd5081ab
