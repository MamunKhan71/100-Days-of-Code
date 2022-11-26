from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_app = f"C:\chromedriver"
driver = webdriver.Chrome(chrome_driver_app)

driver.get(url="https://www.amazon.com/Instant-Pot-Ultra-Programmable-Sterilizer/dp/B07588SJHN/ref=ex_alt_wg_d"
               "?_encoding=UTF8&pd_rd_i=B07588SJHN&psc=1&pd_rd_w=t7Ud0&pf_rd_p=4e1b46a8-daf9-4433-b97e-d6df97cf3699"
               "&pf_rd_r=8EY0YVPAP31Y8RS5MK9N&pd_rd_wg=ptXRO&pd_rd_r=312ff4fa-7c61-4ac3-ba95-8d8028b11a3e&content-id"
               "=amzn1.sym.4e1b46a8-daf9-4433-b97e-d6df97cf3699")
price = driver.find_element(By.CLASS_NAME, "a-price-whole")
print(price.text)
driver.quit()

