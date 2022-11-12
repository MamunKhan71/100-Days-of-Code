from data_manager import DataManager
from flight_search import FlightSearch
dtMg = DataManager()
flightSearch = FlightSearch()
cityData = dtMg.getDestData()
flightSearch.get_destination_code(cityName="Paris")