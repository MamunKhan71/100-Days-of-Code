from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.minsize(height=400, width=500)
window.config(padx=20,pady=20)
window.title("Password Manager")
canvas = Canvas(height=400, width=500)
images = PhotoImage(file="padlock.png")
canvas.create_image(250, 100, image=images)
canvas.grid(row=0, column=2)
webLabel = Label(text="Website:")


window.mainloop()