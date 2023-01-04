from flask import Flask, render_template, request
import smtplib
import os
user_email = os.getenv("userEmail")
user_pass = os.getenv("userPass")
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
       mess = f"Subject: Email From {request.form['name']}\n\nName: {request.form['name']}\nEmail:{request.form['email']}\nPhone: {request.form['phone']}\nMessage: {request.form['message']}"
       with smtplib.SMTP("smtp.gmail.com") as connection:
           connection.starttls()
           connection.login(user=user_email, password=user_pass)
           connection.sendmail(from_addr=request.form["email"], to_addrs=user_email, msg=mess)
           print("SMS Sending Successful")
       return render_template("contact.html", sms_sent=True)
   else:
       return render_template("contact.html", sms_sent=False)

if __name__ == "__main__":
    app.run(debug=True)