import pyautogui,pyperclip
import time

txt = open('animals.txt','r')
a = "You are a"
for i in txt:
    pyautogui.write(a+' '+i)
    pyautogui.press('Enter')
    time.sleep(.3)













