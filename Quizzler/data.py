import requests
parameter = {
    "amount": 15,
    "category": 18,
    "type": "boolean",
}
data = requests.get(url="https://opentdb.com/api.php", params=parameter)
question = data.json()
question_data = question["results"]