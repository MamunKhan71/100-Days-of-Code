from tkinter import *

window = Tk()
window.title("Registration Form")
window.minsize(height=500, width=500)
# Creating Label

label = Label(text="Registration Form", font=("Arial", 20, "bold"))
label.pack()


def entryGrabber():
    print(entry1.get())


# Creating Name Field
entry1 = Entry(width=30)
entry1.insert(END, string="Full Name")
entry1.get()
entry1.focus()
spacer1 = Label(text="")
spacer1.pack()
entry1.pack()
entry2 = Entry(width=30)
spacer1 = Label(text="")
spacer1.pack()
entry2.insert(END, string="Email")
entry2.pack()


# Gender Radio Button
def radioBtn():
    print(radioState.get())


radioState = IntVar()
rdBtn1 = Radiobutton(text="Male", variable=radioState, value=1, command=radioBtn)
rdBtn2 = Radiobutton(text="Female", variable=radioState, value=2, command=radioBtn)
rdBtn1.pack()
rdBtn2.pack()


# Check Button
def checkBtns():
    print(checkBtn.get())


checkBtn = IntVar()
chkBtn1 = Checkbutton(text="English", variable=checkBtn, command=checkBtns)
chkBtn1.pack()
chkBtn2 = Checkbutton(text="Bangla", variable=checkBtn, command=checkBtns)
chkBtn2.pack()

# Button
btn = Button(text="Submit", width=20, bg="Black", fg="White")
btn.pack()
window.mainloop()
