import random

userInput = input("Please add all the names separated by comma(,)\n: ")
billerName = userInput.split(",")
bill_len = len(billerName) - 1
randNum = random.randint(0, bill_len)
print(f"{billerName[randNum]} is going to pay the bill today!")
