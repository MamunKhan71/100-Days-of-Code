import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numBers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symBols = ['!', '#', '$', '%', '&', ',', '*', '+', '@']
print("Welcome to PyPassword Generator")
letterCount = int(input("How many letters password you like to generate\n: "))
numberCount = int(input("How many numbers would you like \n: "))
symbolCount = int(input("How many symbols would you like \n: "))
passSaver = ""
for num in range(0, letterCount):
    rand_char = random.choice(letters)
    passSaver += rand_char
for num in range(0, numberCount):
    rand_num = random.choice(numBers)
    passSaver += rand_num
for num in range(0, symbolCount):
    rand_sym = random.choice(symBols)
    passSaver += rand_sym

print(f"Your generated Password is : {passSaver}")