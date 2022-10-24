from tkinter import *

window = Tk()
window.minsize(height=150, width=350)
window.title("Mile to KM Converter")
window.config(padx=20, pady=20)


# Mile to Km method
def mile_to_km():
    mile = float(entry.get())
    km = mile * 1.609
    score.config(text=f"{km}")


# Creating Entry
userInput = IntVar()
entry = Entry(width=10)
entry.grid(row=0, column=1)

# Label
lbl = Label(text="Miles")
lbl.config(padx=10)
lbl.grid(row=0, column=2)

# Creating Label
label = Label(text="is equal to")
label.config(padx=10, pady=5)
label.grid(row=1, column=0)

# Creating Score
score = Label(text="0")
score.grid(row=1, column=1)

# Creating label2
label2 = Label(text="Km")
label2.grid(row=1, column=2)

# Creating Button
button = Button(text="Calculate", command=mile_to_km)
button.focus()
button.grid(row=2, column=1)


window.mainloop()
