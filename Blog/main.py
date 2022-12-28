from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def greet():
    return "Hello World"


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    web = requests.get(url="https://api.npoint.io/fb47f0cb31915fe52376")
    all_post = web.json()
    return render_template("index.html", blogPost=all_post)


if __name__ == "__main__":
    app.run()
