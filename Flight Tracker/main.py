from pprint import pprint

from data_manager import DataManager
from flight_search import FlightSearch
data = DataManager()
flightSearch = FlightSearch()
cityData = data.getDestData()
for city in cityData:
    city["iataCode"] = flightSearch.get_destination_code(cityName=city['city'])
data.destination_data = cityData
data.updateDestData()
