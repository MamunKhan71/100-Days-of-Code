from tkinter import *
from questionBank import QuestionBank
from questionModel import QuestionModel
from quizzBrain import QuizzBrain
import html
question_bank = []
questionBank = QuestionBank()
questions = questionBank.questionFetcher()

for question in questions:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = QuestionModel(question_text, question_answer)
    question_bank.append(new_question)

print(question_bank)

quiz = QuizzBrain(question_bank)

