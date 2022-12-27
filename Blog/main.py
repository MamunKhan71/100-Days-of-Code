from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)


@app.route("/")
def sayHi():
    year_now = datetime.now().year
    return render_template("index.html", num=year_now)


if __name__ == "__main__":
    app.run()
