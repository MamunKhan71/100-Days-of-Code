import requests


class QuestionBank:
    def __init__(self):
        self.questionFetcher()

    def questionFetcher(self):
        parameter = {
            "amount": 15,
            "category": 18,
            "type": "boolean",
        }
        data = requests.get(url="https://opentdb.com/api.php", params=parameter)
        data.raise_for_status()
        question = data.json()
        question_data = question["results"]
        return question_data

