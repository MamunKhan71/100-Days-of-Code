from tkinter import *
import response

window = Tk()
window.title("Kanye Says")
window.config(padx=20, pady=20)
canvas = Canvas(height=400, width=500, highlightthickness=0)
image = PhotoImage(file="quoteBackground.png")
canvas.config(bg="white")
canvas.create_image(250, 220, image=image)
canvas.grid(row=0, column=0, columnspan=1)
face = PhotoImage(file="icon.png")
button = Button(image=face, highlightthickness=0, bg="white", width=500)
button.grid(row=1,column=0, columnspan=1)

window.mainloop()
