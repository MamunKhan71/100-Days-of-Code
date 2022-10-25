from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
bg = "#F9F9F9"
FONT_NAME = "Consolas"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.2
LONG_BREAK_MIN = 0.3
reps = 0
timer = None


# ---------------------------- TIMER ------------------------------- #
def timeReset():
    global reps
    reps = 0
    checkMark.config(text="", bg="white", fg="white")
    canvas.itemconfig(titleText, text="Pomodoro Timer", fill="black")
    canvas.itemconfig(timeCounters, text=f"00:00")
    window.after_cancel(timer)


def timeCounter(count):
    global reps, timer
    countMin = math.floor(count / 60)
    countSec = count % 60
    if 0 <= countSec <= 9:
        countSec = "0" + str(countSec)
    if 0 <= countMin <= 9:
        countMin = "0" + str(countMin)
    canvas.itemconfig(timeCounters, text=f"{countMin}:{countSec}")
    if count > 0:
        global timer
        timer = window.after(1000, timeCounter, count - 1)
    else:
        startTimer()
        mark = ""
        workSessions = math.floor(reps / 2)
        for _ in range(workSessions):
            mark += "✅"
        checkMark.config(text=mark, bg="green", fg="white")


def startTimer():
    global reps
    reps += 1
    workTime = WORK_MIN * 60
    shortBreak = SHORT_BREAK_MIN * 60
    longBreak = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        canvas.itemconfig(titleText, text=f"Break", fill="blue")
        timeCounter(longBreak)
    elif reps % 2 == 0:
        canvas.itemconfig(titleText, text=f"Break", fill="red")
        timeCounter(shortBreak)
    else:
        timeCounter(workTime)
        canvas.itemconfig(titleText, text=f"Work", fill="green")


window = Tk()
window.title("Pomodoro Timer")
window.config(bg=bg, width=500, height=500, padx=100, pady=50)
canvas = Canvas(width=300, height=430, bg=bg, highlightthickness=0)
titleText = canvas.create_text(150, 20, text="Pomodoro Timer", font=(FONT_NAME, 25, "bold"))
tomatoImg = PhotoImage(file="tomatoTimerPng.png")
canvas.create_image(150, 180, image=tomatoImg)
timeCounters = canvas.create_text(150, 350, text="00:00", fill="red", font=(FONT_NAME, 40, "bold"))
start = Button(text="Start", width=10, bg="black", fg="white", highlightthickness=0, command=startTimer)
reset = Button(text="Reset", width=10, bg="blue", fg="white", highlightthickness=0, command=timeReset)
barImg = PhotoImage(file="complete.png")
barImage = canvas.create_image(150, 400, image=barImg)
checkMark = Label(borderwidth=2, relief="flat", highlightthickness=0)
checkMark.grid(row=2, column=1)
start.grid(row=2, column=0)
reset.grid(row=2, column=2)
canvas.grid(row=1, column=1)
window.mainloop()
