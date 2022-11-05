import requests
from datetime import datetime

my_lat = 23.810331
my_lng = 90.412521
time = datetime.now().hour

parameters = {
    "lat": my_lat,
    "lng": my_lng,
}


def issIsOverhead(iss_lt, iss_lg):
    if (iss_lg - 5) <= my_lng <= (iss_lg + 5) and (iss_lt - 5) <= my_lat <= (iss_lt + 5):
        if isNightCheck():
            print("Can be seen")
        else:
            print("Can't be seen")
    else:
        print("False")


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
