from tkinter import *
BACKGROUND_COLOR = "#5D1049"

window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

canvas = Canvas(height=526, width=771, highlightthickness=0)
cardImage = PhotoImage(file="./images/Flash1.png")
canvas.create_image(384, 260, image=cardImage)
canvas.config(bg=BACKGROUND_COLOR)
canvas.create_text(192, 130, text="Hello There")
canvas.grid(row=0, column=0)
window.mainloop()
