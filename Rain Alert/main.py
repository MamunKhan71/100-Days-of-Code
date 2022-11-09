import requests
from twilio.rest import Client
account_sid = "AC2376c41ec068151bf6a1db34ac98028c"
auth_token = "429ab6e089d790ba0592d3bbfd1ab771"
apiKey = "69f04e4613056b159c2761a9d9e664d2"

parameter = {
    "lat": 11.237490,
    "lon": 124.989166,
    "appid": apiKey,
    "exclude": "minutely,current,daily",
}

fetched = requests.get(url="https://api.openweathermap.org/data/2.5/onecall?", params=parameter)
fetched.raise_for_status()
fetchedData = fetched.json()["hourly"][:12]
umbrellaBringer = False
for num in fetchedData:
    if fetchedData[0]["weather"][0]["id"] < 700:
        umbrellaBringer = True
    else:
        continue
if umbrellaBringer:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Oh NO!! Seems Like It will Rain Today - Bring an Umbrella",
        from_="+18658003523",
        to="+12139156465",
    )
    print(message.status)
else:
    print("Umbrella not needed")
