import pyautogui, pyperclip
import time

txt = open('propose.txt', 'r')
a = input("Enter your Name: ")
for i in txt:
    pyautogui.write(a+' '+i)
    pyautogui.press('Enter')
    time.sleep(.3)














