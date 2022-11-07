import requests

apiKey = "69f04e4613056b159c2761a9d9e664d2"

parameter = {
    "lat": 23.900372,
    "lon": 90.327225,
    "appid": apiKey,
}

fetched = requests.get(url="https://api.openweathermap.org/data/2.5/onecall?", params=parameter)
fetched.raise_for_status()
fetchedData = fetched.json()
print(fetchedData)