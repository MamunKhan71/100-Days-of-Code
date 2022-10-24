from tkinter import *


class UI:
    def __init__(self, programName):
        window = Tk()
        window.minsize(height=500, width=400)
        window.title(programName)


        window.mainloop()
