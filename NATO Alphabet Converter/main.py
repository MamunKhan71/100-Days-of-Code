from flask import Flask

app = Flask(__name__)


def bold_maker(function):
    def wrapper_f():
        return "<b>" + function() + "</b>"

    return wrapper_f


def emphasis_maker(function):
    def wrapper_f():
        return "<em>" + function() + "</em>"

    return wrapper_f


def underline_maker(function):
    def wrapper_f():
        return "<u>" + function() + "</u>"

    return wrapper_f


#
# @app.route('/hi')
#
#
# def say_hi():
#     return "Hello Hi!"
#

@app.route('/')
@bold_maker
@underline_maker
@emphasis_maker
def hello_world():
    return 'Hello, World!'


app.run()
