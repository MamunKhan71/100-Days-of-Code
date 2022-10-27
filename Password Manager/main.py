from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from passwordGenerator import PassGen


def passGenerator():
    passGen = PassGen()
    randomPass = passGen.passWGen()
    passEntry.delete(0, END)
    passEntry.insert(END, string=f"{randomPass}")


# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=20, pady=20)
window.title("Password Manager")
canvas = Canvas(height=200, width=200)
images = PhotoImage(file="padlock.png")
canvas.create_image(100, 100, image=images)
canvas.grid(row=0, column=0, columnspan=3)

webLabel = Label(text="Website : ", )
webLabel.grid(row=1, column=0, sticky="W", pady=5)

webEntry = Entry(width=35)
webEntry.insert(END, string="Website Name")
webEntry.focus()
webEntry.grid(row=1, column=1, columnspan=2)
emlLabel = Label(text="Email/Username : ")
emlLabel.grid(row=2, column=0, sticky="W", pady=5)
emlEntry = Entry(width=35)
emlEntry.insert(END, string="User Name / Email")
emlEntry.grid(row=2, column=1, columnspan=2, sticky="W", pady=5)

passLbl = Label(text="Password : ")
passLbl.grid(row=3, column=0, sticky="W", pady=5)
passEntry = Entry(width=21)
passEntry.insert(END, string="********")
passEntry.grid(row=3, column=1, sticky="W", pady=5)
genPassBtn = Button(text="Generate", width=10, bg="blue", fg="white", command=passGenerator)
genPassBtn.grid(row=3, column=2, sticky="W", pady=5)

addBtn = Button(text="Add", width=29, height=1, bg="green", fg="white")
addBtn.grid(row=4, column=1, columnspan=2, sticky="W", pady=5)
window.mainloop()
