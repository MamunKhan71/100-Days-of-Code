import requests

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "bUytJ1jRokjDmn3rOjr8WVotDSwAGLjk"


class FlightSearch:

    def get_destination_code(self, cityName):
        tqEndPoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": cityName, "location_types": "city"}
        response = requests.get(url=tqEndPoint, headers=headers, params=query)
        iData = response.json()["locations"]
        code = iData[0]["code"]
        print(code)
