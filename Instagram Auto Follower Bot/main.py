import time

from selenium import webdriver
from selenium.webdriver.common.by import By




email = chromeDriver.find_element(By.NAME, 'username')
time.sleep(5)
email.send_keys(instaGram_userName)