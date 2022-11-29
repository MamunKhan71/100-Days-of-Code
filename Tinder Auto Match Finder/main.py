import time

from selenium import webdriver
from selenium.webdriver.common.by import By
chrome = "C:\chromedriver"
driver = webdriver.Chrome(chrome)
driver.get(url="https://tinder.com/")

time.sleep(2)
login = driver.find_element(By.XPATH, '//*[@id="q798806120"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
login.click()
time.sleep(1)
fb_login = driver.find_element(By.XPATH, '//*[@id="q-929574956"]/main/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]')
time.sleep(1)
fb_login.click()
fb_window = driver.window_handles[1]
driver.switch_to.window(fb_window)
time.sleep(2)
fb_email = driver.find_element(By.NAME, "email")
fb_email.send_keys("01643091606")
fb_pass = driver.find_element(By.NAME, "pass")
fb_pass.send_keys("AimDaP,IwCtpuD.Ia24n")
login_btn = driver.find_element(By.NAME, "login")
login_btn.click()
time.sleep(15)
redirect = driver.find_element(By.XPATH, '//*[@id="mount_0_0_/3"]/div/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div')
redirect.click()
time.sleep(5)


