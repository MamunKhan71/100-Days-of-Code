def resources(resDec,userCh):



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
        resources(resDec=resourcesDirectory,userCh=1)
    case "latte":
        resources(resDec=resourcesDirectory, userCh=2)
    case "cappuccino":
        resources(resDec=resourcesDirectory, userCh=3)
    case "off":
        print("Machine is in maintenance mode. Turning off!")
        exit(0)
    case "report":
        resources(resDec=resourcesDirectory, userCh=0)
