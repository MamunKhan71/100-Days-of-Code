travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
]


def add_new_country(ctName, ctVisit, ttVisits):
    new_list = {"country": ctName,
                "cities_visited": ctVisit,
                "total_visits": ttVisits
                }

    travel_log.append(new_list)


add_new_country(ctName="Russia", ttVisits=2, ctVisit=["Moscow", "Saint Petersburg", "Bangla City"])
print(travel_log)
