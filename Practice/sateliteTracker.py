import requests
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data1 = response.json()["iss_position"]["longitude"]
data2 = response.json()["iss_position"]["latitude"]
issPos = (data1, data2)
print(issPos)