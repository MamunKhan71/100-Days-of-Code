import random
from database import questions
from questionModel import Question

print("The quiz will be 5 marks. 1 marks for each")
print("You need to select true(1) or false(0)")

inpt1 = input("Q: ")
inpt2 = input("A: ")
newQ = Question(inpt1, inpt2)
print("Test")


