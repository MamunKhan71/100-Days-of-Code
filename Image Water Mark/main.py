import tkinter as tk
from tkinter import filedialog, END
from PIL import Image, ImageTk, ImageDraw, ImageFont
from matplotlib import pyplot as plt
from tkinter import messagebox

global b2
global img
my_w = tk.Tk()
my_w.geometry("600x600")
frame = tk.Frame(my_w, height=500, width=500)
frame.pack()
frame.place(anchor='center', rely=.5, relx=.5)
my_w.title('Photo Water Mark Professional')
my_font1 = ('times', 18, 'bold')
l1 = tk.Label(frame, text='Photo Water Mark Professional', width=30, font=my_font1)
l1.grid(row=0, column=1, columnspan=2, pady=10, padx=10)
b1 = tk.Button(frame, text='Upload File', width=20, command=lambda: upload_file())
b1.grid(row=2, column=1, columnspan=2, pady=10, padx=10)


def upload_file():
    global img
    global b2
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    image = Image.open(filename)
    resized = image.resize((300, 300))
    img = ImageTk.PhotoImage(resized)
    b2 = tk.Label(frame, image=img)  # using Button
    b2.grid(row=1, column=1, columnspan=2, pady=10, padx=10)
    text = tk.Text(frame, height=2, width=37)
    text.grid(row=2, column=1, columnspan=2, pady=10, padx=10)
    text.focus_set()
    b1.config(text="Add Watermark", command=lambda: getText(filename, text))
    b1.grid(row=3, column=1, columnspan=2, padx=10, pady=10)


def getText(filename, text):
    inputs = text.get("1.0", END)
    waterMarkAdder(filename, inputs)


def waterMarkAdder(filenames, inputs):
    global img
    global b2
    image = Image.open(filenames)
    watermark_image = image.copy()
    print(inputs)
    w, h = image.size
    x, y = int(w / 2), int(h / 2)
    draw = ImageDraw.Draw(watermark_image)
    font = ImageFont.truetype("arial.ttf", int(x / 6))
    draw.text((x, y), inputs, fill=(0, 0, 0), font=font, anchor='ms')
    plt.imshow(watermark_image)
    watermark_image.save("watered.jpg")
    messagebox.showinfo("Watermark Added Successfully", "Your watermark has been added successfully!")
    image = Image.open("watered.jpg")
    resized = image.resize((300, 300))
    img = ImageTk.PhotoImage(resized)
    b2.config(image=img)


my_w.mainloop()
