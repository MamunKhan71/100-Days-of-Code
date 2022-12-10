import time
from random import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class InstaFollower:
    def __init__(self):
        self.instaGram_userName = "01643-091606"
        self.instaGram_userPass = "ilyjdylm?"
        self.chromeDriver = webdriver.Chrome("C:\chromedriver.exe")
        self.chromeDriver.get(url="https://www.instagram.com/accounts/login/")

    def login(self):
        time.sleep(5)
        email = self.chromeDriver.find_element(By.NAME, "username")
        email.send_keys(self.instaGram_userName)
        pass_word = self.chromeDriver.find_element(By.NAME, 'password')
        pass_word.send_keys(self.instaGram_userPass)
        submit = self.chromeDriver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div')
        submit.click()
        time.sleep(5)
        # self.chromeDriver.get(url="https://www.instagram.com/codewithharry/followers/")
        # time.sleep(5)
        self.find_followers()

    def find_followers(self):
        time.sleep(5)
        self.chromeDriver.get(f"https://www.instagram.com/codewithharry/followers")

        time.sleep(5)
        buttons = self.chromeDriver.find_element(By.XPATH, "//button[contains(.,'Follow')]").text
        for btn in buttons:
            # Use the Java script to click on follow because after the scroll down the buttons will be un clickeable
            # unless you go to it's location
            self.chromeDriver.execute_script("arguments[0].click();", btn)
            time.sleep(3)

    def follow(self):
        pass
