import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import os
actual_download_speed = 100
actual_upload_speed = 80
chrome_driver = "C:\chromedriver"
twitter_id = os.getenv("twitter_id")
twitter_pass = os.getenv("twitter_pass")

driver = webdriver.Chrome(chrome_driver)
driver.get(url="https://twitter.com/")
login = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/a/div')
login.click()
email = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
email.send_keys(twitter_id)
time.sleep(2)
passWord = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
passWord.send_keys(twitter_pass)
time.sleep(5)