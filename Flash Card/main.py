import random
from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#563F6D"
database = pd.read_csv("./data/french_words.csv")
dbList = database.to_dict(orient="records")
print(dbList)

current_card = {}


def nextCardChooser():
    global current_card
    current_card = random.choice(dbList)
    canvas.itemconfig(titleText, text=f"French")
    canvas.itemconfig(questionText, text=f"{current_card['French']}")
    canvas.after(3000, func=cardFlipper)


def cardFlipper():
    global current_card
    # newImage = PhotoImage(file="./images/ffb.png")
    # canvas.item-config(canvasImage, image=newImage)
    canvas.itemconfig(titleText, text="English")
    canvas.itemconfig(questionText, text=current_card["English"])


window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

canvas = Canvas(height=526, width=771, highlightthickness=0)
cardImage = PhotoImage(file="./images/ff.png")
canvasImage = canvas.create_image(384, 260, image=cardImage)
canvas.config(bg=BACKGROUND_COLOR)
titleText = canvas.create_text(384, 180, font=("Born Rounded Demo", 24, "italic underline"))
questionText = canvas.create_text(384, 263, font=("Born Rounded Demo", 24, "bold"))
canvas.grid(row=0, column=0, columnspan=2)
rightImg = PhotoImage(file="./images/buttonr.png")
rightBtn = Button(image=rightImg, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0, command=nextCardChooser)
rightBtn.grid(row=1, column=0)
leftImg = PhotoImage(file="./images/buttonx.png")
leftBtn = Button(image=leftImg, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0, command=nextCardChooser)
leftBtn.grid(row=1, column=1)
nextCardChooser()
window.mainloop()
