import datetime as dt
import random
import smtplib

myEmail = "mamunkhan3523@gmail.com"
myPass = "uuaqwxdrkwovucdt"


def emailSender(myMsg, **subject):
    newSubject = str(subject['subject'])
    newMessage = ("Subject:" + newSubject + "\n\n" + myMsg)
    print(newMessage)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=myEmail, password=myPass)
        connection.sendmail(from_addr=myEmail,
                            to_addrs="mamunkhan3523@yahoo.com",
                            msg=newMessage
                            )


date = dt.datetime.now()
with open(file="quotes.txt", mode="r") as quote:
    randQuotes = random.choice(quote.readlines())
    if date.weekday() == 1:
        emailSender(randQuotes, subject="Tuesday Motivation")
    else:
        print("This is not Tuesday")
