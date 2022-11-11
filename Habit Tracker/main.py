import requests
from datetime import datetime

USERNAME = "mamun3523"
TOKEN = "mamun3523khan"
date = datetime.now()
yesDate = datetime(month=11, day=10, year=2022)
pixelaEndpoint = "https://pixe.la/v1/users"
parameter = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
#
graphDefinitionEndPoint = f"{pixelaEndpoint}/{USERNAME}/graphs"
graphConfig = {
    "id": "graph1",
    "name": "100 Days of Python",
    "unit": "minute",
    "type": "int",
    "color": "sora",
    "timezone": "Asia/Dhaka",

}
postRequestEndPoint = f"{graphDefinitionEndPoint}/{graphConfig['id']}"
headers = {
    "X-USER-TOKEN": TOKEN
}
postRequest = {
    "date": yesDate.strftime("%Y%m%d"),
    "quantity": "10",
}
# response = requests.post(url=postRequestEndPoint, json=postRequest, headers=headers)
# print(response.text)
deleteEndPoint = f"{postRequestEndPoint}/{yesDate.strftime('%Y%m%d')}"
print(deleteEndPoint)
req = requests.delete(url=deleteEndPoint, headers=headers)
print(req.text)
# graphUpdate = {
#     "color": "ajisai",
# }
# graphDefinitionEndPointID = f"{pixelaEndpoint}/{USERNAME}/graphs/graph1"

# responseUpdate = requests.put(url=graphDefinitionEndPointID, json=graphUpdate, headers=headers)
# response = requests.post(url=graphDefinitionEndPoint, json=graphConfig, headers=headers)
# print(responseUpdate.text)
