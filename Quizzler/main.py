from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from tkinter import *
import html
window = Tk()
window.title("Quizzler - The Quiz App")
window.config(padx=50, pady=50, bg="#ededed", highlightthickness=0)
canvas = Canvas(height=400, width=400, highlightthickness=0, bg="#ededed")
score = Label(text="Score", font=("Arial", 20, "bold"), bg="#ededed")
score.grid(row=0,column=1, columnspan=2)

bgImage = PhotoImage(file="./images/bg1.png")
canvas.create_image(200,200, image=bgImage)
canvas.grid(row=1, column=1, columnspan=2)
question2 = canvas.create_text(200,200, text="Hello there, My name is Md. Mamun. I am from Dhaka", width=200, font=("Calibiri", 20, "bold"), fill="white", justify=CENTER)
rImage = PhotoImage(file="./images/true.png")
rightButton = Button(image=rImage, borderwidth=0)
rightButton.grid(row=2,column=1)
lImage = PhotoImage(file="./images/false.png")

leftButton = Button(image=lImage, borderwidth=0)
leftButton.grid(row=2, column=2)

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    nextQ = quiz.next_question()
    canvas.itemconfig(question2, text=html.unescape(nextQ))


# print("You've completed the quiz")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")
window.mainloop()
