from tkinter import *

window = Tk()
window.title("Registration Form")
window.minsize(height=400, width=300)
window.config(padx=5, pady=5)
# Creating Label

label1 = Label(text="Enter Name")
label1.config(padx=15, pady=15)
label1.grid(row=0, column=0)


def entryGrabber():
    print(entry1.get())


# Creating Name Field
entry1 = Entry(width=20)
entry1.insert(END, string="Python")
entry1.get()

entry1.grid(row=0, column=1)
entry2 = Entry(width=20)
##
label2 = Label(text="Enter Email")
label2.grid(row=1, column=0)
entry2.insert(END, string="py@python.org")
label2.config(padx=15, pady=15)
entry2.grid(row=1, column=1)
#
label3 = Label(text="Password")
label3.grid(row=2, column=0)
#
entry3 = Entry(width=20)
entry3.insert(END, string="*******")
label3.config(padx=15, pady=15)
entry3.grid(row=2, column=1)
#
label4 = Label(text="re-enter Pass")
label4.config(padx=15, pady=15)
label4.grid(row=3, column=0)
#


entry4 = Entry(width=20)
entry4.insert(END, string="*******")
entry4.grid(row=3, column=1)
#
btn = Button(text="Register")
btn.focus()
btn.grid(row=4, column=0)

#
# # Gender Radio Button
# def radioBtn():
#     print(radioState.get())
#
#
# radioState = IntVar()
# rdBtn1 = Radiobutton(text="Male", variable=radioState, value=1, command=radioBtn)
# rdBtn2 = Radiobutton(text="Female", variable=radioState, value=2, command=radioBtn)
# rdBtn1.pack()
# rdBtn2.pack()
#
#
# # Check Button
# def checkBtns():
#     print(checkBtn.get())
#
#
# checkBtn = IntVar()
# chkBtn1 = Checkbutton(text="English", variable=checkBtn, command=checkBtns)
# chkBtn1.pack()
# chkBtn2 = Checkbutton(text="Bangla", variable=checkBtn, command=checkBtns)
# chkBtn2.pack()
#
# # Button
# btn = Button(text="Submit", width=20, bg="Black", fg="White")
# btn.pack()
window.mainloop()
