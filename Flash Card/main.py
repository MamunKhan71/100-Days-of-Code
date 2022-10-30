import random
from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#563F6D"
NEW_BACKGROUND_COLOR = "#56AB45"
database = None
try:
    database = pd.read_csv("./data/to_learn.csv")
except FileNotFoundError:
    database = pd.read_csv("./data/french_words.csv")
finally:
    dbDictToLearn = database.to_dict(orient="records")
current_card = {}


def nextCardChooser():
    global current_card, flipWindow
    window.after_cancel(flipWindow)
    current_card = random.choice(dbDictToLearn)
    canvas.itemconfig(canvasImage, image=cardImage)
    canvas.itemconfig(titleText, text=f"French")
    canvas.itemconfig(questionText, text=f"{current_card['French']}")
    flipWindow = window.after(3000, func=cardFlipper)


def cardFlipper():
    global current_card
    canvas.itemconfig(canvasImage, image=backImg)
    canvas.itemconfig(titleText, text="English")
    canvas.itemconfig(questionText, text=current_card["English"])


def knownCards():
    dbDictToLearn.remove(current_card)
    newDict = pd.DataFrame(dbDictToLearn)
    newDict.to_csv("./data/to_learn.csv", index=False)
    print(len(dbDictToLearn))
    nextCardChooser()


window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
flipWindow = window.after(3000, func=nextCardChooser)
canvas = Canvas(height=526, width=771, highlightthickness=0)
cardImage = PhotoImage(file="./images/ff.png")
backImg = PhotoImage(file="./images/ffb.png")
canvasImage = canvas.create_image(384, 260, image=cardImage)
canvas.config(bg=BACKGROUND_COLOR)
titleText = canvas.create_text(384, 180, font=("Born Rounded Demo", 24, "italic underline"))
questionText = canvas.create_text(384, 263, font=("Born Rounded Demo", 30, "bold"))
canvas.grid(row=0, column=0, columnspan=2)
rightImg = PhotoImage(file="images/buttonRight.png")
rightBtn = Button(image=rightImg, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0, command=knownCards)
rightBtn.grid(row=1, column=0)
leftImg = PhotoImage(file="images/buttonWrong.png")
leftBtn = Button(image=leftImg, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0, command=nextCardChooser)
leftBtn.grid(row=1, column=1)
nextCardChooser()
window.mainloop()
