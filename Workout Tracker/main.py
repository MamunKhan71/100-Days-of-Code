import requests
from datetime import datetime
applicantID = "724fd8aa"
gender = "Male"
weight = 58
height = 167
age = 23
date = datetime.now()
appKey = "0715a4a127c10cbff7bbf4477398b227"
sheetyApiEndPoint = "https://api.sheety.co/f3f2d6c9e76f4500056fda7540ff6199/myWorkouts/workouts"
apiEndPoint = "https://trackapi.nutritionix.com/v2/natural/nutrients"
exerciseEndPoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
userInput = input("Which exercise you did: ")
headers = {
    "x-app-id": applicantID,
    "x-app-key": appKey,
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

response = requests.post(url=exerciseEndPoint, json=exParameter, headers=headers)

sheetyParameter = {
    "Date": date.strftime("%d/%m/%Y"),
    "Time": date.strftime("%H%M%S"),
    "Exercise":
}