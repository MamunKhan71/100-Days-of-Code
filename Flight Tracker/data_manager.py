import requests
from pprint import pprint


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def getDestData(self):
        response = requests.get(url="https://api.sheety.co/f3f2d6c9e76f4500056fda7540ff6199/flightDeals/prices")
        data = response.json()["prices"]
        return data
