import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
user_pass = os.getenv("user_pass")
drivePath = f"C:\chromedriver"

driver = webdriver.Chrome(drivePath)
driver.get(url="https://www.linkedin.com/home")
user_name = driver.find_element(By.ID, 'session_key')
user_name.send_keys("mkmamun031@gmail.com")
user_passW = driver.find_element(By.ID, 'session_password')
user_passW.send_keys(f"{user_pass}")
submit = driver.find_element(By.CLASS_NAME, "sign-in-form__submit-button")
submit.click()
driver.get(
    url="https://www.linkedin.com/jobs/search/?currentJobId=3370668718&f_AL=true&geoId=102257491&keywords=digital%20marketing")

apply_job = driver.find_element(By.XPATH, '//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/button')

apply_job.click()

time.sleep(5)