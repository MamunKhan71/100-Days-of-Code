import json
from tkinter import *
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from passwordGenerator import PassGen

randomPass = None


def passGenerator():
    global randomPass
    passGen = PassGen()
    randomPass = passGen.passWGen()
    passEntry.delete(0, END)
    passEntry.insert(END, string=f"{randomPass}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def errorPrinter(messageName):
    messagebox.showerror(title=f"{messageName} error", message=f"Please enter the {messageName}")


def findPassword():
    website = webEntry.get()
    with open(file="passSaver.json") as dataFile:
        data = json.load(dataFile)
        if website in data:
            email = data[website]['Name']
            passW = data[website]['Password']
            messagebox.showinfo(title=f"{website} Password", message=f"Your Information for {website} is :\n"
                                                                     f"User Name : {email}\nPassword: {passW}")
        else:
            messagebox.showinfo(title=f"{website} Password Not Found", message=f"Error 404 - Password Not found ")


def fileSaver():
    webSiteName = webEntry.get()
    print(webSiteName)
    userOrEmail = emlEntry.get()
    passWord = passEntry.get()
    passWordJson = {
        webSiteName: {
            "Name": userOrEmail,
            "Password": passWord,
        }
    }
    if not webSiteName:
        webEntry.focus()
        errorPrinter("Website Name")
    elif not userOrEmail:
        emlEntry.focus()
        errorPrinter("User Name or Email")
    elif not passWord:
        passEntry.focus()
        errorPrinter("Password")
    else:
        pyperclip.copy(passWord)
        userInput = messagebox.askokcancel(title=webSiteName,
                                           message=f"These are the details entered \nUser Name : {userOrEmail} "
                                                   f"\nPassword : {passWord}\nIs it okay?")
        if userInput:
            try:
                with open(file="passSaver.json", mode="r") as passSaver:
                    data = json.load(passSaver)
                    data.update(passWordJson)
                with open(file="passSaver.json", mode="w") as passSaver:
                    json.dump(data, passSaver, indent=4)
            except FileNotFoundError:
                with open(file="passSaver.json", mode="w") as passSaver:
                    json.dump(passWordJson, passSaver, indent=4)
            finally:
                webEntry.delete(0, END)
                emlEntry.delete(0, END)
                passEntry.delete(0, END)


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

webEntry = Entry(width=21)
# webEntry.insert(END, string="Website Name")
webEntry.focus()
webEntry.grid(row=1, column=1)
webSearch = Button(text="Search", width=10, bg="black", fg="white", command=findPassword)
webSearch.grid(row=1, column=2, sticky="W")
emlLabel = Label(text="Email/Username : ")
emlLabel.grid(row=2, column=0, sticky="W", pady=5)
emlEntry = Entry(width=35)
# emlEntry.insert(END, string="User Name / Email")
emlEntry.grid(row=2, column=1, columnspan=2, sticky="W", pady=5)

passLbl = Label(text="Password : ")
passLbl.grid(row=3, column=0, sticky="W", pady=5)
passEntry = Entry(width=21)
# passEntry.insert(END, string="********")
passEntry.grid(row=3, column=1, sticky="W", pady=5)
genPassBtn = Button(text="Generate", width=10, bg="blue", fg="white", command=passGenerator)
genPassBtn.grid(row=3, column=2, sticky="W", pady=5)

addBtn = Button(text="Add", width=29, height=1, bg="green", fg="white", command=fileSaver)
addBtn.grid(row=4, column=1, columnspan=2, sticky="W", pady=5)
window.mainloop()
