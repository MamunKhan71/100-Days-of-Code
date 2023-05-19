import tkinter as tk

texts = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
window = tk.Tk()
window.title("TypeTester")
window.geometry("720x720")
window.resizable(False, False)
window.iconbitmap("F:/TypTest/image/4.ico")
label = tk.Label(window, text="Welcome to TypeTest", font=("Helvetica", 18))
label.pack(padx=20, pady=20)


def onKeyPress(event):
    text2.insert('end', 'You Pressed %s\n' % (event.char, ))


text = tk.Text(window, height=10, width=80, font=('Helvetica', 13), wrap="word")
text.insert('1.0', texts)
text.pack(padx=10, pady=10)
text.config(state="disabled")
text2 = tk.Text(window, height=10, width=80, font=("Helvetica", 13), wrap="word")
text2.pack(pady=10, padx=10)
text2 = tk.Text(window, background='black', foreground='white', font=('Comic Sans MS', 12))
text2.pack()
window.bind('<KeyPress>', onKeyPress)

window.mainloop()

