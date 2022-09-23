import random
from art import numberGuessingGameLogo

print(numberGuessingGameLogo)
computerGuess = random.randint(1, 100)
noOfAttempts = 0
gameLevel = int(input("█░ Choose your difficulty level \n1.Easy \n2.Hard \n: "))
if gameLevel == 1:
    noOfAttempts = 10
elif gameLevel == 2:
    noOfAttempts = 5
while noOfAttempts != 0:
    userGuess = int(input("█░ Enter your guess: "))
    if userGuess == computerGuess:
        print("+----------------------------------+---------+------------------------+----------------+")
        print("|                             Congratulations! You Win!                                |")
        print("+----------------------------------+---------+------------------------+----------------+")
        break
    elif userGuess > computerGuess:
        print("+----------------------------------+---------+------------------------+----------------+")
        print("|                     Number is too high - Select lower number                         |")
        print(f"|                         ─── ∙ Remaining Attempts {noOfAttempts-1} ∙ ──                              |")
        print("+----------------------------------+---------+------------------------+----------------+")
    elif userGuess < computerGuess:
        print("+----------------------------------+---------+------------------------+----------------+")
        print("|                    Number is too low  - Select Higher number                         |")
        print(f"|                         ─── ∙ Remaining Attempts {noOfAttempts-1} ∙ ──                              |")
        print("+----------------------------------+---------+------------------------+----------------+")
    noOfAttempts -= 1
if noOfAttempts == 0:
    print("█░ █░ █░ █░ █░  Game over! You have used all of your possible attempts!   ░█ ░█ ░█ ░█ ░█")
