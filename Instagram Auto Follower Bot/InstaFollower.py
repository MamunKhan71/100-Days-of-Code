import time
from random import random, randint

from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        self.chromeDriver.get(url="https://www.instagram.com/codewithharry/followers/")
        time.sleep(5)

    def find_followers(self):
        modal = self.chromeDriver.find_element(By.CLASS_NAME, '_aano')
        for i in range(3):
            self.chromeDriver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        time.sleep(5)
        followers = self.chromeDriver.find_elements(By.CSS_SELECTOR, 'li button')
        for follower in followers:
            if follower.text == 'Follow':
                time.sleep(randint(1000, 1600) / 1000)
                follower.click()
