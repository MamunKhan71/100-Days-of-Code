from tkinter import *

window = Tk()
window.title("Kanye Says")
window.config(padx=20, pady=20)
canvas = Canvas(height=400, width=500, highlightthickness=0)
image = PhotoImage(file="quoteBackground.png")
canvas.config(bg="#55a630")
canvas.create_image(250, 200, image=image)
canvas.grid(row=0, column=1, columnspan=1)


window.mainloop()
