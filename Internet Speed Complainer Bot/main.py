import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import os

# actual_download_speed = 100
# actual_upload_speed = 80
# chrome_driver = "C:\chromedriver"
# twitter_id = os.getenv("twitter_id")
# twitter_pass = os.getenv("twitter_pass")
#
# driver = webdriver.Chrome(chrome_driver)
# driver.get(url="https://twitter.com/")
# login = driver.find_element(By.XPATH,
#                             '//*[@id="layers"]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/a/div/span/span')
# login.click()
# time.sleep(3)
# email = driver.find_element(By.XPATH,
#                             '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
# email.send_keys(twitter_id)
# time.sleep(3)
# next = driver.find_element(By.XPATH,
#                            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span')
# next.click()
# time.sleep(100)
# passWord = driver.find_element(By.XPATH,
#                                '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
# passWord.send_keys(twitter_pass)
# time.sleep(100)
# log = driver.find_element(By.XPATH,
#                           '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
# log.click()
# time.sleep(100)
# userInput = driver.find_element(By.XPATH,
#                                 '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
# time.sleep(100)

from Internet_Speed import InternetSpeedMeter

intMeter = InternetSpeedMeter()
internet_speed = float((intMeter.get_upload_speed()).text)
print(internet_speed)
