from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        self.window = Tk()
        self.window.title("Quizzler - The Quiz App")
        self.window.config(padx=50, pady=50, bg="#ededed", highlightthickness=0)
        self.canvas = Canvas(height=400, width=400, highlightthickness=0, bg="#ededed")
        self.scoreLabel = Label(text="Score : ", font=("Arial", 20, "bold"), bg="#ededed")
        self.scoreLabel.grid(row=0, column=1, columnspan=2)
        self.bgImage1 = PhotoImage(file="images/bg1.png")
        self.bgImage2 = PhotoImage(file="images/bgRed.png")
        self.bgImage3 = PhotoImage(file="images/bgGreen.png")
        self.imageBg = self.canvas.create_image(200, 200, image=self.bgImage1)
        self.canvas.grid(row=1, column=1, columnspan=2)
        self.questionText = self.canvas.create_text(200, 200, text="Question Text",
                                                    width=200,
                                                    font=("Calibiri", 20, "bold"), fill="white", justify=CENTER)
        self.rImage = PhotoImage(file="images/true.png")
        self.rightButton = Button(image=self.rImage, borderwidth=0, command=self.correctAnswer)
        self.rightButton.grid(row=2, column=1)
        self.lImage = PhotoImage(file="images/false.png")

        self.leftButton = Button(image=self.lImage, borderwidth=0, command=self.inCorrectAnswer)
        self.leftButton.grid(row=2, column=2)
        self.get_next_qus()
        self.window.mainloop()

    def get_next_qus(self):
        self.canvas.itemconfig(self.imageBg, image=self.bgImage1)
        self.canvas.itemconfig(self.questionText, fill="white")
        qText = self.quiz.next_question()
        self.canvas.itemconfig(self.questionText, text=qText)

    def correctAnswer(self):
        checkAns = self.quiz.check_answer("True")
        self.feedback(checkAns)

    def inCorrectAnswer(self):
        checkAns = self.quiz.check_answer("False")
        self.feedback(checkAns)

    def feedback(self, checkAnswer):
        if checkAnswer:
            self.score += 1
            self.scoreLabel.config(text=f"Score : {self.score}")
            self.canvas.itemconfig(self.questionText, fill="black")
            self.canvas.itemconfig(self.imageBg, image=self.bgImage3)
            self.window.after(1000, func=self.get_next_qus)

        else:
            self.scoreLabel.config(text=f"Score : {self.score}")
            self.canvas.itemconfig(self.questionText, fill="black")
            self.canvas.itemconfig(self.imageBg, image=self.bgImage2)
            self.window.after(1000, func=self.get_next_qus)

