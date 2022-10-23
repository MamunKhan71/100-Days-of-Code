from tkinter import *

window = Tk()
window.minsize(height=500, width=500)
button = Button()
window.title("Widget Example")
label = Label(text="This is new text", font=("Arial", 10, "bold"))
label.pack()
button.config(text="Click Me", font=("Arial", 10, "bold"))
button.pack()
multiLine = Text()
entry = Entry(width=30)
entry.insert(END, string="Some text to begin : ")
entry.pack()
# Text
text = Text(height=5, width=30)
text.focus()
text.insert(END, "Example of multi-line text entry.")
print(text.get(1.0, END))
text.pack()


def spinBox():
    print(spinBox.get())


def Scales(value):
    print(value)


# Spin Box
spinBox = Spinbox(width=10, from_=1, to=10, command=spinBox)
spinBox.pack()
# Scale
scale = Scale(from_=1, to=50, command=Scales)
scale.pack()


# Check Button
def checkButton():
    print(checkedState.get())


checkedState = IntVar()
chkBtn = Checkbutton(text="Is On?", variable=checkedState, command=checkButton)
chkBtn.pack()


# Radio Button:

def radioUsed():
    print(radioState.get())


radioState = IntVar()
radioState1 = Radiobutton(text="Option 1", value=1, variable=radioState, command=radioUsed)
radioState2 = Radiobutton(text="Option 2", value=2, variable=radioState, command=radioUsed)
radioState1.pack()
radioState2.pack()


# list box
def listUsed(event):
    print(listBox.get(listBox.curselection()))


listBox = Listbox(height=5, width=30)
newList = ["Apple", "Pear", "Orange", "Banana"]
for n in newList:
    listBox.insert(newList.index(n), n)
    listBox.bind("<<ListboxSelect>>", listUsed)
listBox.pack()
window.mainloop()
