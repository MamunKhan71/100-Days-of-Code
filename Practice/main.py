import tkinter
window = tkinter.Tk()
window.title("My First Program - GUI")
window.minsize(width=500, height=300)
new_label = tkinter.Label(text="I am a label", font=("Consolas",10,"bold"))
new_label.pack(side="left")




window.mainloop()