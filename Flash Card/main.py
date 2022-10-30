from tkinter import *
BACKGROUND_COLOR = "#563F6D"

window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

canvas = Canvas(height=526, width=771, highlightthickness=0)
cardImage = PhotoImage(file="./images/ff.png")
canvas.create_image(384, 260, image=cardImage)
canvas.config(bg=BACKGROUND_COLOR)
canvas.create_text(384, 180, text="   Quiz - 01   ", font=("Born Rounded Demo", 24, "italic underline"))
canvas.create_text(384, 263, text="What is the name of Bangladesh?", font=("Born Rounded Demo", 24, "bold"))
canvas.grid(row=0, column=0, columnspan=2)
rightImg = PhotoImage(file="./images/buttonr.png")
rightBtn = Button(image=rightImg, highlightthickness=0, bg= BACKGROUND_COLOR, borderwidth=0)
rightBtn.grid(row=1, column=0)
leftImg = PhotoImage(file="./images/buttonx.png")
leftBtn = Button(image=leftImg, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0)
leftBtn.grid(row=1, column = 1)
window.mainloop()
