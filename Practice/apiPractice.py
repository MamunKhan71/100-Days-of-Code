import requests
from datetime import datetime
myLat = 23.900372
myLng = 90.327225
formatting = 0
parameter = {
    "lat": myLat,
    "lng": myLng,
    "formatted": formatting,
}
now = datetime.now()
sunStatus = requests.get(url="https://api.sunrise-sunset.org/json", params=parameter)
sunStatus.raise_for_status()
data = sunStatus.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise.split("T"))
print(sunset)
print(now)