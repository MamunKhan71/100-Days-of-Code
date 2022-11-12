from pprint import pprint

from data_manager import DataManager
from flight_search import FlightSearch
dtMg = DataManager()
flightSearch = FlightSearch()
cityData = dtMg.getDestData()
for city in cityData:
    cityCode = flightSearch.get_destination_code(cityName=city['city'])
    print(cityCode)
