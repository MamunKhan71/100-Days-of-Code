import requests
from datetime import datetime
import smtplib

my_lat = 23.810331
my_lng = 90.412521
time = datetime.now().hour

userEmail = "mamunkhan3523@gmail.com"
userPass = "aefgfgzizrctgrna"
parameters = {
    "lat": my_lat,
    "lng": my_lng,
}


def emailNotifier(message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=userEmail, password=userPass)
        connection.sendmail(from_addr=userEmail, to_addrs="mamunkhan3523@yahoo.com", msg=message)


def issIsOverhead(iss_lt, iss_lg):

    if (iss_lg - 5) <= my_lng <= (iss_lg + 5) and (iss_lt - 5) <= my_lat <= (iss_lt + 5):
        if isNightCheck():
            emailNotifier(message=f"Can Be Seen")
        else:
            emailNotifier(message=f"Can't Be Seen")
    else:
        emailNotifier(message=f"Can't Be Seen")


def isNightCheck():
    if time > sunset or time < sunrise:
        return True


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
issData = response.json()
iss_lat = float(issData["iss_position"]["latitude"])

iss_lng = float(issData["iss_position"]["longitude"])
issIsOverhead(iss_lat, iss_lng)

rspns = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
rspns.raise_for_status()
timeData = rspns.json()
sunset = timeData["results"]["sunset"]
sunrise = timeData["results"]["sunrise"]
