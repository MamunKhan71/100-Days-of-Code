# import tkinter as tk
#
# texts = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
# window = tk.Tk()
# window.title("TypeTester")
# window.geometry("720x720")
# window.resizable(False, False)
# window.iconbitmap("F:/TypTest/image/4.ico")
# label = tk.Label(window, text="Welcome to TypeTest", font=("Helvetica", 18))
# label.pack(padx=20, pady=20)
#
#
# def onKeyPress(event):
#     text2.insert('end', 'You Pressed %s\n' % (event.char, ))
#
#
# text = tk.Text(window, height=10, width=80, font=('Helvetica', 13), wrap="word")
# text.insert('1.0', texts)
# text.pack(padx=10, pady=10)
# text.config(state="disabled")
# text2 = tk.Text(window, height=10, width=80, font=("Helvetica", 13), wrap="word")
# text2.pack(pady=10, padx=10)
# text2 = tk.Text(window, background='black', foreground='white', font=('Comic Sans MS', 12))
# text2.pack()
# window.bind('<KeyPress>', onKeyPress)
#
# window.mainloop()
#
import time

import keyboard
import re

text = "Historically, the fundamental role of pharmacists as a healthcare practitioner was to check and distribute drugs to doctors for medication that had been prescribed to patients.\n In more modern times, pharmacists advise patients and health care providers on the selection, dosages, interactions, and side effects of medications, and act as a learned intermediary between a prescriber and a patient. Pharmacists monitor the health and progress of patients to ensure the safe and effective use of medication. Pharmacists may practice compounding; however, many medicines are now produced by pharmaceutical companies in a standard dosage and drug delivery form. In some jurisdictions, pharmacists have prescriptive authority to either independently prescribe under their own authority or in collaboration with a primary care physician through an agreed upon protocol."


def speedCalculator(timeTaken, totalTyped, incorrectWord):
    print(totalTyped)
    print(f"found mistakes {incorrectWord}")
    grossSpeed = (int(totalTyped) / 5) / (float(timeTaken) / 60)
    netTime = (int(incorrectWord)/((float(timeTaken))/60))
    netSpeed = grossSpeed - netTime
    print(netSpeed)
    print(f"Gross Speed : {int(grossSpeed)} Words Per Minute")
    print(f"Net Speed : {int(netSpeed)} Words Per Minute")


def on_press(event):
    finalWord = 0
    incorrectWord = 0
    start = time.time()
    userInput = input("")
    stop = time.time()
    totalTyped = len(userInput)
    timeTaken = f"{stop - start:.2f}"
    actualText = text.split(" ")
    print(len(actualText))
    userText = userInput.split(" ")
    loopLength = len(userText)
    print(f"{actualText[1]} - {userText[1]}")
    for i in range(loopLength):
        if actualText[i] != userText[i]:
            incorrectWord += 1

    print(f"Total Time Taken : {timeTaken} seconds")
    keyboard.unhook_all()
    speedCalculator(timeTaken, totalTyped, incorrectWord)


print(f"{text}\nType: ")
keyboard.on_press(on_press)
keyboard.wait()
