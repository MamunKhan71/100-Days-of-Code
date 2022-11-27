from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_app = f"C:\chromedriver"
driver = webdriver.Chrome(chrome_driver_app)

driver.get(url="http://secure-retreat-92358.herokuapp.com/")
# price = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[2]/a')
# price.click()
def sender():
    first_name = driver.find_element(By.NAME, "fName")
    first_name.send_keys("Md.")
    lName = driver.find_element(By.NAME, "lName")
    lName.send_keys("Mamun")
    email_name = driver.find_element(By.NAME, "email")
    email_name.send_keys("mamunkhan3523@diu.edu.bd")
    email_name.send_keys(Keys.TAB)
    email_name.send_keys(Keys.ENTER)
    time.sleep(10)
sender()


