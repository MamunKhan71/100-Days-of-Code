import random

letter = ['rainbow', 'computer', 'science', 'programming',
          'python', 'mathematics', 'player', 'condition',
          'reverse', 'water', 'board', 'geeks']
rand = random.choice(letter)
randLtr = len(rand)
blankLtr = ""
life = 0
tri = int(0)
trig = 0
for num in range(randLtr):
    blankLtr += "_"
print(f"Guess The Word: {blankLtr}")
while life != randLtr:
    userInput = input(f"Enter Your Letter (Remaining Lives: {randLtr - life}): ")
    trig = 0
    for num in range(randLtr):
        if userInput == rand[num]:
            blankLtr = blankLtr[:num] + userInput + blankLtr[num + 1:]
            trig = 1
    if "_" not in blankLtr:
        break
    elif trig == 0:
        life += 1
    else:
        print(blankLtr)
        continue

if blankLtr == rand:
    print(f"{blankLtr} matches {rand} # You win! - Thanks for saving a life!")
else:
    print("You loose! Game Over!")
