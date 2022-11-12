import requests
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "bUytJ1jRokjDmn3rOjr8WVotDSwAGLjk"
class FlightSearch:

    def get_destination_code(self, cityName):
        tqEndPoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}

