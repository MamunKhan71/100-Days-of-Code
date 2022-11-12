import requests
from pprint import pprint

SHEETY_PRICE_ENDPOINT = "https://api.sheety.co/f3f2d6c9e76f4500056fda7540ff6199/flightDeals/prices/"


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def getDestData(self):
        response = requests.get(url=SHEETY_PRICE_ENDPOINT)
        data = response.json()["prices"]
        # print(data)
        return data

    def updateDestData(self):
        for city in self.destination_data:
            newData = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            putReq = requests.put(url=f"{SHEETY_PRICE_ENDPOINT}/{city['id']}", json=newData)
            print(putReq.text)
