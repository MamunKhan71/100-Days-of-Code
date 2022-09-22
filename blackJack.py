from art import blackJackLogo
import random


def randNumMaker():
    new_randVal = []
    for num in range(0, 2):
        new_randVal.append(random.randint(1, 11))
    return new_randVal


def replace_values(list_to_replace, item_to_replace, item_to_replace_with):
    return [item_to_replace_with if item == item_to_replace else item for item in list_to_replace]


def blackJackCheck(randUsrs):
    i = 0
    while i < 2:
        if randUsrs.__contains__(11) and randUsrs.__contains__(10):
            return True
        else:
            return False


def bustCheck(randUsrs, usrSum1):
    if usrSum1 > 21:
        if randUsrs.__contains__(11):
            newVal = randUsrs
            replace_values(newVal, 11, 1)
            newSum = sum(newVal)
            if newSum > 21:
                return 1
            else:
                return 0


def userCardChoice(randUsr, userSum):
    userChoice = input("Do you want to get another Card? (Y/N) : ")
    if userChoice == "Y":
        newRand = random.randint(1, 11)
        randUsr.append(newRand)
        userSum = sum(randUsr)
        return userSum
    else:


print(blackJackLogo)
randUsr = randNumMaker()
usrSum = sum(randUsr)
randCom = randNumMaker()
comSum = randCom[0] + randCom[1]
if blackJackCheck(randCom):
    print(f"The Computer Has BlackJack {randCom[0]} and {randCom[1]} : Computer Wins")
elif blackJackCheck(randUsr):
    print(f"The User Has BlackJack {randUsr[0]} and {randUsr[1]} : User Wins")
else:
    bustChecker = bustCheck(randUsr, usrSum)
    if bustChecker == 1:
        print("You are busted! You Loose!")
    else:
        newUserSum = userCardChoice(randUsr, usrSum)
        bustCheck(randUsr, newUserSum)
