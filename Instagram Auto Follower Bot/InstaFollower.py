import time

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
        self.chromeDriver.get(url="https://www.instagram.com/codewithharry/")
        time.sleep(5)
        followers = self.chromeDriver.find_element(By.XPATH, '//*[@id="mount_0_0_d6"]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[2]').find_element(By.TAG_NAME, 'a')
        followers.click()
        time.sleep(10)


    def find_followers(self):
        pass

    def follow(self):
        pass
