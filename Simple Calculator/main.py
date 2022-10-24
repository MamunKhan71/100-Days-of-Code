from tkinter import *

window = Tk()
window.minsize(height=250, width=200)
window.title("Simple Calculator")
window.config(padx=50, pady=50)


# Entry Deleter
def entryDeleter():
    resultShow.delete(0, END)


# Add function
def addFunc():
    firstNum = float(fEntry.get())
    secondNum = float(sEntry.get())
    rsLT = firstNum + secondNum
    entryDeleter()
    resultShow.insert(END, string=f"{rsLT}")


def subFunc():
    firstNum = float(fEntry.get())
    secondNum = float(sEntry.get())
    rsLT = firstNum - secondNum
    entryDeleter()
    resultShow.insert(END, string=f"{rsLT}")


# First Name
fName = Label(text="First Number : ")
fName.grid(sticky="W", row=0, column=0)
fEntry = Entry(width=20)
fEntry.focus()
fEntry.grid(row=0, column=1)
fName.config(pady=10)
# Second Number
sLabel = Label(text="Second Number : ")
sLabel.grid(sticky="W", row=1, column=0)

sEntry = Entry(width=20)
sEntry.grid(row=1, column=1)
sLabel.config(pady=20)

# Add Button
addButton = Button(text="Add", width=10, bg="blue", fg="white", command=addFunc)
addButton.grid(sticky="W", row=2, column=0)

# Sub Button

subButton = Button(text="Subtract", width=10, bg="dark red", fg="white", command=subFunc)
subButton.grid(sticky="W", row=2, column=1)

# Result

result = Label(text="Result : ")
result.config(pady=20)
result.grid(sticky="W", row=3, column=0)
resultShow = Entry(width=20)
resultShow.insert(END, string="")
resultShow.grid(sticky="W", row=3, column=1)

window.mainloop()
