from selenium import webdriver
from selenium.webdriver.common.by import By

instaGram_userName = "01643-091606"
instaGram_userPass = "ilyjdylm?"


class InstaFollower:
    def __init__(self):
        self.chromeDriver = webdriver.Chrome("C:\chromedriver.exe")
        self.chromeDriver.get(url="https://www.instagram.com/")

    def login(self):
        pass

    def find_followers(self):
        pass

    def follow(self):
        pass
