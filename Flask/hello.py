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
def logging_decorator(fn):
    def wrapper(*args, **kwargs):
        print(f"You called {fn.__name__}{args}")
        result = fn(args[0], args[1], args[2])
        print(f"It returned: {result}")

    return wrapper


@logging_decorator
def a_function(a, b, c):
    return a * b * c


a_function(1, 2, 3)

if __name__ == "__main__":
    app.run(debug=True)
