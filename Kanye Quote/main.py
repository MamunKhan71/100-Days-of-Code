from tkinter import *
import requests


def quoteChanger():
    response = requests.get(url="https://api.kanye.rest/")
    response.raise_for_status()
    quote = response.json()
    newQuote = quote["quote"]
    canvas.itemconfig(canvasText, text=newQuote)


window = Tk()

window.title("Kanye Says")
window.config(padx=20, pady=20)
canvas = Canvas(height=414, width=300, highlightthickness=0)
# image = PhotoImage(file="quoteBackground.png")
canvas.config(bg="white")
# canvas.create_image(250, 220, image=image)
canvas.grid(row=0, column=0, columnspan=1)
canvasText = canvas.create_text(150, 207, text="Hello there", font=("Consolas", 10, "bold"),width=250)
quoteChanger()
face = PhotoImage(file="icon.png")
button = Button(image=face, highlightthickness=0, bg="white", width=300, command=quoteChanger)
button.grid(row=1, column=0, columnspan=1)

window.mainloop()
