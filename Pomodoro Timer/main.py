from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
bg = "#F9F9F9"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

window = Tk()
window.title("Tomato Timer")
window.config(bg=bg, width=500, height=500, padx=100, pady=50)
canvas = Canvas(width=300, height=400, bg=bg, highlightthickness=0)
canvas.create_text(150, 30, text="Pomodoro Timer", font=("Consolas", 25, "bold"))
tomatoImg = PhotoImage(file="tomatoTimerPng.png")
canvas.create_image(150, 200, image=tomatoImg)
canvas.create_text(150, 370, text="00:00", fill="red", font=("Consolas", 40, "bold"))
start = Button(text="Start", width=10, bg="black", fg="white", highlightthickness=0)
reset = Button(text="Reset", width=10, bg="blue", fg="white", highlightthickness=0)
start.grid(row=2, column=0)
reset.grid(row=2, column=2)
canvas.grid(row=1, column=1)

window.mainloop()
