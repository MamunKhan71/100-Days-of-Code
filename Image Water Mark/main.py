import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk

my_w = tk.Tk()
my_w.geometry("600x600")  # Size of the window
frame = tk.Frame(my_w, height=500, width=500)
frame.pack()
frame.place(anchor='center', rely=.5, relx=.5)
my_w.title('Photo Water Mark Professional')
my_font1 = ('times', 18, 'bold')
img = ImageTk.PhotoImage(Image.open("uploads.png"))
l1 = tk.Label(frame, text='Photo Water Mark Professional', width=30, font=my_font1)
l1.grid(row=0, column=1, columnspan=2, pady=10, padx=10)
b1 = tk.Button(frame, text='Upload File', width=20, command=lambda: upload_file())
b1.grid(row=2, column=1, columnspan=2, pady=10, padx=10)


def upload_file():
    global img
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    image = Image.open(filename)
    resized = image.resize((300, 300))
    img = ImageTk.PhotoImage(resized)
    b2 = tk.Label(frame, image=img)  # using Button
    b2.grid(row=1, column=1, columnspan=2, pady=10, padx=10)
    b1.config(text="Add Watermark")



my_w.mainloop()  # Keep the window open
