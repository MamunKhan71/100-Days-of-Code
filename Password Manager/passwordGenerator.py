import random


class passGen:

    def __init__(self):
        passWSavers = []
        lTrs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numBers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symBols = ['!', '#', '$', '%', '&', ',', '*', '+', '@']


def passWGen():
    print("Welcome to PyPassword Generator")
    letterCount = int(15)
    numberCount = random.randint(1, 5)
    symbolCount = random.randint(1, 5)
    for num in range(0, letterCount):
        rand_char = random.choice(numBers)
        self.passWSavers.append(rand_char)
    for num in range(0, numberCount):
        rand_num = random.choice(self.numBers)
        self.passWSavers.append(rand_num)
    for num in range(0, symbolCount):
        rand_sym = random.choice(self.symBols)
        self.passWSavers.append(rand_sym)
    passViewer(self)


def passViewer(self):
    random.shuffle(self.passWSavers)
    genString = ''.join(self.passWSavers)
    print(f"Randomly Generated Pass is : {genString}")
