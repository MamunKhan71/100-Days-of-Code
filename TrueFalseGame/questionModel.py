from database import questions


class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
        self.questionAdder()

    def questionAdder(self):
        newQ = {
            self.text: {self.answer}
        }
        questions.append(newQ)
