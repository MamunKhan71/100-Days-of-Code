import random

letter = ['hello', 'banana','error']
rand = random.choice(letter)
randLtr = len(rand)
blankLtr = ""
life = 0
for num in range(randLtr):
    blankLtr += "_"
print(f"Guess The Word: {blankLtr}")
while life != randLtr:
    userInput = input("Enter Your Letter : ")
    for num in range(randLtr):
        if userInput == rand[num]:
            blankLtr = blankLtr[:num] + userInput + blankLtr[num + 1:]
        if "_" in blankLtr:
            continue
    print(blankLtr)
    if blankLtr == rand:
        life = randLtr
    else:
        life += 1
if blankLtr == rand:
    print(f"{blankLtr} matches {rand} # You win! - Thanks for saving a life!")
else:
    print("You loose! Game Over!")