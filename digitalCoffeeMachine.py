def resources(userCh):
    global resourcesDirectory
    print(resourcesDirectory[userCh].values())


userChoice = input("What would you like? (espresso/latte/cappuccino) : ")
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
        resources(userCh=int(0))
