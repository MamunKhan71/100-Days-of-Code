from selenium import webdriver
from selenium.webdriver.common.by import By

class InternetSpeedMeter:
    def __init__(self):
        self.upload_speed = 0
        self.download_speed = 0
        self.website_name = "https://www.speedtest.net/"
        self.chrome_driver = "C:\chromedriver"
    def get_upload_speed(self):

