from selenium import webdriver
from selenium.webdriver.common.by import By
import time

t_out = time.time() + 5
chromePath = f"C:\chromedriver"
driver = webdriver.Chrome(chromePath)
driver.get(url="http://orteil.dashnet.org/experiments/cookie/")

# price = driver.find_element(By.ID, 'buyCursor').text.split("-")[1].strip()
price = driver.find_elements(By.ID, 'rightPanel')
for prc in price:
    print(prc.text)

# def check():
#     print("check")

# while True:
#     if time.time() > t_out:
#         pass
#
#
#
#     cookie = driver.find_element(By.ID, 'cookie')
#     cookie.click()
