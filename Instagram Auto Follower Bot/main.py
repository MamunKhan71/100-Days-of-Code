import time

from selenium import webdriver
from selenium.webdriver.common.by import By

instaGram_userName = "01643-091606"
instaGram_userPass = "ilyjdylm?"
chromeDriver = webdriver.Chrome("C:\chromedriver.exe")
chromeDriver.get(url="https://www.instagram.com/")

email = chromeDriver.find_element(By.NAME, 'username')
time.sleep(5 )
email.send_keys(instaGram_userName)