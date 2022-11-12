import requests

flightSearch = "https://api.tequila.kiwi.com/v2/search"


class FlightData:
    def __init__(self, price, org_city, org_airport, dest_city, dest_airport, out_date, return_date):
        self.price = price
        self.org_city = org_city
        self.org_airport = org_airport
        self.dest_city = dest_airport
        self.dest_airport = dest_airport
        self.out_date = out_date
        self.return_date = return_date
