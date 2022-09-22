from art import blackJackLogo
import random


def randNumMaker():
    new_randVal = []
    for num in range(0, 2):
        new_randVal.append(random.randint(1, 11))
    return new_randVal


def blackJackCheck(randUsrs):
    i = 0
    while i < 2:
        if randUsrs.__contains__(11) and randUsrs.__contains__(10):
            return True
        else:
            return False


print(blackJackLogo)
randUsr = randNumMaker()
usrSum = randUsr[0] + randUsr[1]
randCom = randNumMaker()
comSum = randCom[0] + randCom[1]
if blackJackCheck(randCom):
    print(f"The Computer Has BlackJack {randCom[0]} and {randCom[1]} : Computer Wins")
elif blackJackCheck(randUsr):
    print(f"The User Has BlackJack {randUsr[0]} and {randUsr[1]} : User Wins")

