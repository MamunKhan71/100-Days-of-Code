import requests
from datetime import datetime
import os
applicantID = "724fd8aa"
gender = "Male"
weight = 58
height = 167
age = 23
date = datetime.now()
SHETTY_AUTH = os.environ.get('SHETTY_AUTH')
print(SHETTY_AUTH)
API_KEY = os.environ.get("API_KEY")

sheetyApiEndPoint = "https://api.sheety.co/f3f2d6c9e76f4500056fda7540ff6199/myWorkouts/workouts"
apiEndPoint = "https://trackapi.nutritionix.com/v2/natural/nutrients"
exerciseEndPoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
userInput = input("Which exercise you did: ")
headers = {
    "x-app-id": applicantID,
    "x-app-key": os.environ.get("API_KEY"),
    "x-remote-user-id": "0",
}
parameter = {
    "query": userInput,
    "timezone": "Asia/Dhaka"
}
exParameter = {
    "query": userInput,
    "gender": gender,
    "weight_kg": weight,
    "height_cm": height,
    "age": age,

}
sheetyHeader = {
    "Authorization": os.environ.get("SHETTY_AUTH"),
}
response = requests.post(url=exerciseEndPoint, json=exParameter, headers=headers)
data = response.json()
print(data)
# today_date = datetime.now().strftime("%d/%m/%Y")
# now_time = datetime.now().strftime("%X")
# for dta in data["exercises"]:
#     sheetyParameter = {
#         "workout": {
#                 "date": today_date,
#                 "time": now_time,
#                 "exercise": dta["name"].title(),
#                 "duration": dta["duration_min"],
#                 "calories": dta["nf_calories"],
#             }
#         }
#     post = requests.post(url=sheetyApiEndPoint, json=sheetyParameter, headers=sheetyHeader)
#     post.raise_for_status()
#     print(post.text)
#
#
