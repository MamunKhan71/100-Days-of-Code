import re
import time
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup, SoupStrainer

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
url = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B" \
      "%22west%22%3A-122.6224422454834%2C%22east%22%3A-122.42159843444824%2C%22south%22%3A37.820700646776956%2C" \
      "%22north%22%3A37.93505919587507%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value" \
      "%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A" \
      "%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C" \
      "%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22min%22%3A1000%2C%22max%22%3A2800%7D%2C%22price%22%3A" \
      "%7B%22min%22%3A204482%2C%22max%22%3A572549%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22" \
      "%3Atrue%2C%22mapZoom%22%3A13%7D "
property_name = []
property_price = []
property_links = []
web_list = requests.get(url=url, headers=header).content
soup = BeautifulSoup(web_list, 'html.parser')
html_name = soup.find_all('a', class_='property-card-link')
html_price = soup.find_all('div', class_='StyledPropertyCardDataArea-c11n-8-73-8__sc-yipmu-0 hRqIYX')

for link in html_name:
    link_text = link.text
    property_name.append(link_text)

while "" in property_name:
    property_name.remove("")
for price in html_price:
    prices = (price.text.split('+')[0]).split('/')[0]
    property_price.append(prices)

print(property_price)
print(property_name)
# for link in soup.find_all('a', href=True, class_='property-card-link'):
#     print(link['href'])
property_link = soup.find_all(class_="StyledPropertyCardDataArea-c11n-8-73-8__sc-yipmu-0 lhIXlm property-card-link")

for pr in property_link:
    new_address = f"https://www.zillow.com/{pr['href']}"
    property_links.append(new_address)

driver = webdriver.Chrome("C://chromedriver.exe")
driver.get(url="https://forms.gle/gjB9ZSGX82agahvr9")
p_address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
time.sleep(2)
p_address.send_keys(property_name[0])
p_price = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
p_price.send_keys(property_price[0])
p_links = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
p_links.send_keys(property_links[0])
time.sleep(5)


