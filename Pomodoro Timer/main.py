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
window.config(pady=50, padx=50, bg=bg)
canvas = Canvas(width=500, height=500, bg=bg, highlightthickness=0)
canvas.create_text(250, 30, text="Pomodoro Timer", font=("Consolas", 25, "bold"))
tomatoImg = PhotoImage(file="tomatoTimerPng.png")
canvas.create_image(250, 200, image=tomatoImg)
canvas.create_text(250, 370, text="00:00", font=("Consolas", 40, "bold"))
canvas.pack()




window.mainloop()
