from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

window = Tk()
window.title("Tomato Timer")
window.config(pady=50, padx=50)
canvas = Canvas(width=500, height=500)
canvas.create_text(250, 30, text="Pomodoro Timer", font=("Consolas", 24, "bold"))
tomatoImg = PhotoImage(file="tomatoTimerPng.png")
canvas.create_image(250, 200, image=tomatoImg)
canvas.pack()

window.mainloop()
