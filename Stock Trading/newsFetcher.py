import requests


class NewsFetcher:
    def __init__(self):
        pass

    def top3newsFetcher(self, today):
        top3News = []
        parameter2 = {
            "q": "Tesla",
            "from": today,
            "sortBy": "popularity",
            "apiKey": "9e7fceafa0cd4b4c8837775a7ac9b3d4",
        }
        newsApi = requests.get(url="https://newsapi.org/v2/everything?", params=parameter2)
        newsApi.raise_for_status()
        for num in range(0, 3):
            newsDictionary = {
                "title": newsApi.json()["articles"][num]["title"],
                "description": newsApi.json()["articles"][num]["description"]
            }
        return newsDictionary
