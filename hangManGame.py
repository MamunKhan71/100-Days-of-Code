import random
from gameWords import word_list, gameLogo, gameStages

letter = word_list
logo = gameLogo
stages = gameStages
print(logo)
userName = input("What is Your Name: ")
rand = random.choice(letter)
randLtr = len(rand)
blankLtr = ""
life = 0
trig = 0
for num in range(randLtr):
    blankLtr += "_"
print(f"Guess The Word: {blankLtr}")
while life != randLtr:
    userInput = input(f"Enter Your Letter (Remaining Lives: {randLtr - life}): ").lower()
    trig = 0
    for num in range(randLtr):
        if userInput == rand[num]:
            blankLtr = blankLtr[:num] + userInput + blankLtr[num + 1:]
            trig = 1
    if "_" not in blankLtr:
        break
    elif trig == 0:
        life += 1
        print(stages[randLtr - life])
    else:
        print(blankLtr)
        continue

if blankLtr == rand:
    print(f"Congratulations! {userName}! You win! - Thanks for saving a life!")
else:
    print(f"Sorry {userName} You loose! The Game Is Over!")
