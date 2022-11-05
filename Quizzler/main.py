import requests
from tkinter import *
quest = requests.get(url="https://opentdb.com/api.php?amount=50&category=18&difficulty=easy&type=boolean")
quest.raise_for_status()
print(quest.json())