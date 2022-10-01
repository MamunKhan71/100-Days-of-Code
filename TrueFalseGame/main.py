import random
from database import questions
from questionModel import Question


newModel = Question()
random.shuffle(questions)
print("The quiz will be 5 marks. 1 marks for each")
print("You need to select true(1) or false(0)")
questionCount = 0
correctAnsCount = 0
quizLen = len(questions)
while questionCount != quizLen:
    question = questions[questionCount]
    actualAns = question["correct_answer"]
    validity = newModel.questionValidator(question, actualAns)
    if validity:
        correctAnsCount += 1
    questionCount += 1
print(f"Test Finished - Your Score is : {correctAnsCount}")
