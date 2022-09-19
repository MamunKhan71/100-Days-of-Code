import random

letter = ['rainbow', 'computer', 'science', 'programming',
          'python', 'mathematics', 'player', 'condition',
          'reverse', 'water', 'board', 'geeks', 'apple', 'olive', 'tomato', 'melon', 'litchi',
          'mango', 'lime', 'kiwi', 'grapes', 'cherry',
          'banana', 'apricot', 'cucumber', 'guava', 'mulberry',
          'orange', 'papaya', 'pear', 'peach', 'berry', 'ants', 'hippo', 'panda', 'giraffe', 'bat', 'bear',
          'catfish', 'cheetah', 'lizard', 'wolf', 'zebra', 'eagle',
          'cobra', 'goose', 'penguin', 'frog', 'mouse', 'flamingo',
          'rabbit', 'crow', 'whale', 'lion', 'monkey', 'ostrich',
          'peacock', 'raccoon', 'rhinoceros', 'sheep', 'dogs',
          'squirrel', 'tiger', 'vulture', 'ring', 'bangle', 'lipstick', 'handbag', 'crown',
          'necklace', 'watch', 'caps', 'glasses', 'wallet',
          'belts', 'comb', 'pendent', 'earring', 'scarf',
          'backpack', 'keychain', 'hairpin', 'shoes', 'hats',
          'jacket', 'boots', 'socks', 'stocking', 'muffler',
          'gloves', 'umbrella', 'ribbon', 'notebook', 'tape', 'pencil', 'eraser', 'sharpener',
          'files', 'favicon', 'inkpot', 'chalk', 'duster',
          'glue', 'paper', 'cutter', 'chart', 'colours',
          'stapler', 'marker', 'staples', 'clips', 'calculator',
          'envelope', 'register', 'kindly', 'recite', 'repeat', 'tree', 'display', 'geeks', 'coder', 'programmer',
          'premium', 'watch']
userName = input("What is Your Name: ")
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
    else:
        print(blankLtr)
        continue

if blankLtr == rand:
    print(f"Congratulations! {userName}! You win! - Thanks for saving a life!")
else:
    print(f"Sorry {userName} You loose! The Game Is Over!")
