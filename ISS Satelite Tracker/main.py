import requests

my_lat = 23.810331
my_lng = 90.412521


def issIsOverhead(iss_lt, iss_lg):
    if (iss_lg - 5) <= my_lng <= (iss_lg + 5) and (iss_lt - 5) <= my_lat <= (iss_lt + 5) :
        print("True")
    else:
        print("False")


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
issData = response.json()
iss_lat = float(issData["iss_position"]["latitude"])

iss_lng = float(issData["iss_position"]["longitude"])
issIsOverhead(iss_lat, iss_lng)
