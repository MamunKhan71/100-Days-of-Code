from flask import Flask, render_template, request
import requests
app = Flask(__name__)
url = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391").json()
total_news = len(url)
@app.route('/')
def sayhi():
    return render_template('index.html', urls=url, total_news=total_news)

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/post/<pid>")
def post(pid):
    return render_template("post.html", news=url, pd=int(pid))

@app.route("/contact", methods=["GET","POST"])
def contact():
   if request.method == "POST":
       print(
           f"Name: {request.form['name']}\nEmail:{request.form['email']}\nPhone: {request.form['phone']}\nMessage: {request.form['message']}")
       return render_template("contact.html", sms_sent=True)
   else:
       return render_template("contact.html", sms_sent=False)

if __name__ == "__main__":
    app.run(debug=True)