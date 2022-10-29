from tkinter import *
BACKGROUND_COLOR = "5D1049"

window = Tk()
window.minsize(height=500, width=600)
window.title("Flashy")
window.config(pady=30, padx=30)

canvas = Canvas(height=500, width=600)
cardImage = PhotoImage(file="./images/")
canvas.create_image()
window.mainloop()
