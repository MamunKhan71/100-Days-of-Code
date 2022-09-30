from database import questions


class Question:
    def __init__(self):
        pass
        # self.text = text
        # self.answer = answer
        # self.questionAdder()

    # def questionAdder(self):
    #     newQ = {
    #         self.text: {self.answer}
    #     }
    #     questions.append(newQ)

    def questionValidator(self, question,answer):
        print(question["text"])
        choice = input("Your Answer: \n1. True\n2. False\n: ")
        if choice == "1":
            choice = "True"
        else:
            choice = "False"
        if choice == answer:
            print("Correct Answer!")
        else:
            print("Wrong Answer!")
