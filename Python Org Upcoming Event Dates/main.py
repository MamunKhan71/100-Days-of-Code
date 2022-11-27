from pprint import pprint

from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
chrome_driver_app = f"C:\chromedriver"
driver = webdriver.Chrome(chrome_driver_app)
driver.get(url="https://www.python.org/")
year = str(datetime.now().year)
upcoming_schedule = {

}

xPath_link = '//*[@id="content"]/div/section/div[3]/div[2]/div/ul/'
for num in range(1, 6):
    pythonWeb = driver.find_element(By.XPATH, f"{xPath_link}/li[{num}]/time").text
    pythonCompeteDate = f"{year}-{pythonWeb}"
    pythonContent = driver.find_element(By.XPATH, f"{xPath_link}/li[{num}]/a").text
    upcoming_schedule[pythonCompeteDate] = pythonContent

pprint(upcoming_schedule)

