from tkinter import *
windows = Tk()
windows.minsize(height=500, width=500)
windows.title("Grid Testing")
# Creating Label
label = Label(text="Test", font=("Arial", 10, "bold"))
label.grid(row=0, column=0)
# Creating Button
btn1 = Button(text="Button 1", font=("Arial", 10, "bold"))
btn1.grid(row=1, column=1)
# Creating Button 2
btn2 = Button(text="Button 2", font=("Arial", 10, "bold"))
btn2.grid(row=0, column=2)
# Creating Entry
entry = Entry(width=10)
entry.insert(END, string="Entry Here")
entry.grid(row=2,column=3)








windows.mainloop()
