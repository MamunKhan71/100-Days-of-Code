import re
from webbrowser import get


def coinProcessor(quate, dim, nickle, pennie):
    quater = quate * 0.25
    dimes = dim * 0.10
    nickles = nickle * 0.05
    pennies = 0.01
    total_money = quater + dimes + nickles + pennies


def reportGen():
    global resourcesDirectory
    firstReD = resourcesDirectory[0]
    for key, value in firstReD.items():
        if key != "money":
            print(f"{key} : {value}")
        else:
            print(f"{key} : ${value}")


def resources(userCh):
    global resourcesDirectory
    oldRsDct = resourcesDirectory[0]
    newRsDct = resourcesDirectory[userCh]
    # print(resourcesDirectory[0].get("water") - resourcesDirectory[1].get("water"))
    for keys in newRsDct:
        if oldRsDct.get(keys) > newRsDct.get(keys):
            print("Available")
        else:
            if newRsDct.get("water") > oldRsDct.get("water"):
                print("Not Enough Water")
            if newRsDct.get("milk") > oldRsDct.get("milk"):
                print("Not Enough milk")
            if newRsDct.get("coffee") > oldRsDct.get("coffee"):
                print("Not Enough coffee")


userChoice = input("What would you like? (espresso/latte/cappuccino) : ")
resourcesDirectory = [
    {
        "water": 250,
        "milk": 250,
        "coffee": 100,
        "money": 10,
    },
    {
        "water": 350,
        "milk": 350,
        "coffee": 30,
        "money": 3.5,
    },
    {
        "water": 200,
        "milk": 50,
        "coffee": 20,
        "money": 2.50,
    },
    {
        "water": 150,
        "milk": 80,
        "coffee": 30,
        "money": 2.80,
    }

]
match userChoice:
    case "espresso":
        resources(userCh=int(1))
    case "latte":
        resources(userCh=int(2))
    case "cappuccino":
        resources(userCh=int(3))
    case "off":
        print("Machine is in maintenance mode. Turning off!")
        exit(0)
    case "report":
        reportGen()
