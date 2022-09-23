# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random

computerGuess = random.randint(1, 100)
noOfAttempts = 0
gameLevel = int(input("Choose your difficulty level : \n1.Easy \n2.Hard \n: "))
if gameLevel == 1:
    noOfAttempts = 9
elif gameLevel == 2:
    noOfAttempts = 4
while noOfAttempts != 0:
    userGuess = int(input("Enter your guess: "))
    if userGuess == computerGuess:
        print("Congratulations! You win!")
        break
    elif userGuess > computerGuess:
        print("Number is too high - Select lower number")
        print(f"Remaining Attempts ({noOfAttempts+1})")
    elif userGuess < computerGuess:
        print("Number is too low - Select higher number")
        print(f"Remaining Attempts ({noOfAttempts+1})")
    noOfAttempts -= 1
if gameLevel == 0:
    print("Game over! You have used all of your possible attempts!")

