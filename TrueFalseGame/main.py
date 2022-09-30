import random
from database import questions
from questionModel import Question


newModel = Question()
random.shuffle(questions)
print("The quiz will be 5 marks. 1 marks for each")
print("You need to select true(1) or false(0)")
questionCount = 0
correctAnsCount = 0
while questionCount != 5:
    question = questions[questionCount]
    actualAns = question["answer"]
    newModel.questionValidator(question, actualAns)
    questionCount += 1
print(f"Test Finished - Your Score is : {correctAnsCount}")
# newQ = Question(inpt1, inpt2)
