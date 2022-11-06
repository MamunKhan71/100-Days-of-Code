import requests


class QuestionData:
    def __init__(self):
        self.parameter = {
            "amount": 15,
            "category": 18,
            "type": "boolean",
        }
        self.questionFetcher()

    def questionFetcher(self):
        data = requests.get(url="https://opentdb.com/api.php", params=self.parameter)
        question = data.json()
        question_data = question["results"]
        return question_data
