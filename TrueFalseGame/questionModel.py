from database import questions


class Question:
    def __init__(self):
        pass

    def questionValidator(self, question, answer):
        print(question["text"])
        choice = input("Your Answer: \n1. True\n2. False\n: ")
        if choice == "1":
            choice = "True"
        else:
            choice = "False"
        if choice == answer:
            print("Correct Answer!")
            return True
        else:
            print("Wrong Answer!")
            return False
