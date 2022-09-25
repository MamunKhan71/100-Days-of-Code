import re
from webbrowser import get

resourcesDirectory = [
    {
        "water": 250,
        "milk": 250,
        "coffee": 100,
        "money": 0,
    },
    {
        "water": 100,
        "milk": 100,
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


def coinProcessor(usrDirectory, quate, dim, nickle, pennie):
    global resourcesDirectory
    newDir = resourcesDirectory[usrDirectory]
    quater = quate * 0.25
    dimes = dim * 0.10
    nickles = nickle * 0.05
    pennies = 0.01
    total_money = float(quater + dimes + nickles + pennies)
    req_money = newDir["money"]
    ttlWtr = int(resourcesDirectory[0].get("water")) - int(newDir.get("water"))
    ttlMlk = int(resourcesDirectory[0].get("milk")) - int(newDir.get("milk"))
    ttlCfe = int(resourcesDirectory[0].get("coffee")) - int(newDir.get("coffee"))
    if req_money < total_money:
        print(f"Access Granted : You have : {total_money:.2f}, Required: {req_money} ")
        print(f"Here is ${total_money - req_money:.2f} in change")
        resourcesDirectory[0].get("water") - newDir.get("water")
        resourcesDirectory[0].get("milk") - newDir.get("milk")
        resourcesDirectory[0].get("coffee") - newDir.get("coffee")
        up_dict = {"water": ttlWtr}
        up_dict2 = {"milk": ttlMlk}
        up_dict3 = {"coffee": ttlCfe}
        resourcesDirectory[0].update(up_dict)
        resourcesDirectory[0].update(up_dict2)
        resourcesDirectory[0].update(up_dict3)
        for key, value in resourcesDirectory[0].items():
            print(f"{key} : ${value}")
    else:
        print(f"Insufficient balance : You have : {total_money:.2f}, Required: {req_money} ")


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
    newRsDct = resourcesDirectory[userCh].copy()
    newRsDct.popitem()
    trig = 0
    for keys in newRsDct:
        if oldRsDct.get(keys) > newRsDct.get(keys):
            continue
        else:
            if newRsDct.get("water") > oldRsDct.get("water"):
                print("Not Enough Water")
                trig = 1
            if newRsDct.get("milk") > oldRsDct.get("milk"):
                print("Not Enough milk")
                trig = 1
            if newRsDct.get("coffee") > oldRsDct.get("coffee"):
                print("Not Enough coffee")
                trig = 1
    if trig == 0:
        quater = float(input("Quarter : "))
        dimes = float(input("Dimes : "))
        nickles = float(input("Nickles : "))
        pennies = float(input("Pennies : "))
        coinProcessor(int(userCh), quater, dimes, nickles, pennies)


while True:
    userChoice = input("What would you like? (espresso/latte/cappuccino) : ")
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
