from flask import Flask, render_template
import requests

app = Flask(__name__)
data = 0


@app.route('/')
def home():
    global data
    web = requests.get(url="https://api.npoint.io/fb47f0cb31915fe52376")
    data = web.json()
    dataLen = len(data)
    return render_template("index.html", blog=data, count=dataLen)


@app.route('/post/<post_ids>')
def get_post(post_ids):
    return render_template("post.html", posts=data, pid=int(post_ids))


if __name__ == "__main__":
    app.run(debug=True)
