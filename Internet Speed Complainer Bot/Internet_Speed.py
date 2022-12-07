import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class InternetSpeedMeter:
    def __init__(self):
        self.upload_speed = 0
        self.download_speed = 0
        self.website_name = "https://fast.com/"
        self.chrome_driver = "C:\chromedriver"

    def get_upload_speed(self):
        driver = webdriver.Chrome(self.chrome_driver)
        driver.get(url=self.website_name)
        time.sleep(20)
        get_speed = driver.find_element(By.ID, 'speed-value')
        return get_speed
        # get_speed.click()
        # get_speed.submit()
        # self.download_speed = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
        #                                                     '3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
        #                                                     '1]/div/div[2]/span')

