import time

from flask import Flask

app = Flask(__name__)


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
    def wrapper(*args):
        return "Hello there"+args[0]+"."

    return wrapper


@app.route("/hi")
@print_dec
def prints(name):
    return name


prints("Mamun")

if __name__ == "__main__":
    app.run(debug=True)
