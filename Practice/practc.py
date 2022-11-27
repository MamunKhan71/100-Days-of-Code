from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_app = f"C:\chromedriver"
driver = webdriver.Chrome(chrome_driver_app)

driver.get(url="https://www.python.org/")
price = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[2]/a')
print(price.text)
driver.quit()

