from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route('/')
def sayhi():
    return render_template('index.html', urls=url)

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

# Request Section
url = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391").json()
















if __name__ == "__main__":
    app.run(debug=True)