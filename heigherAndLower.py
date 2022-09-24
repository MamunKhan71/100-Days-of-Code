from art import heightWeightLogo, heightWeightLogoVs
import random
from dataSet import data

print(heightWeightLogo)
scoreCount = 0
loopBreaker = True

while loopBreaker:
    randValue1 = random.choice(data)
    randValue2 = random.choice(data)
    print(f"Compare A: {randValue1['name']}, a {randValue1['description']}, from {randValue1['country']}.")
    print(heightWeightLogoVs)
    print(f"Against B: {randValue2['name']}, a {randValue2['description']}, from {randValue2['country']}.")
    userChoice = input("Who has more followers? Type 'A' or 'B': ")
    if userChoice == 'A' or 'a':
        if randValue1['follower_count'] > randValue2['follower_count']:
            scoreCount += 1
            print(f"You're right! Current score: {scoreCount}.")
        else:
            print(f"Sorry, that's wrong. Final score: {scoreCount}")
            break
    elif userChoice == 'B' or 'b':
        if randValue2['follower_count'] > randValue1['follower_count']:
            scoreCount += 1
            print(f"You're right! Current score: {scoreCount}.")
        else:
            print(f"Sorry, that's wrong. Final score: {scoreCount}")
            break
