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
