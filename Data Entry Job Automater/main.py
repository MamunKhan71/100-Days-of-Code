from pprint import pprint

import requests
from bs4 import BeautifulSoup

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
url = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B" \
      "%22west%22%3A-122.55961648331483%2C%22east%22%3A-122.30624429093201%2C%22south%22%3A37.659589507852374%2C" \
      "%22north%22%3A37.888628199563115%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B" \
      "%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22" \
      "%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B" \
      "%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C" \
      "%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22" \
      "%3Atrue%7D "
property_name = []
property_price = []
web_list = requests.get(url=url, headers=header).content
soup = BeautifulSoup(web_list, 'html.parser')
html_address = soup.find_all('a', class_='property-card-link')
html_price = soup.find_all('div', class_='StyledPropertyCardDataArea-c11n-8-73-8__sc-yipmu-0 hRqIYX')
# print(html_price[0])


for link in html_address:
    link_text = link.text
    property_name.append(link_text)

while "" in property_name:
    property_name.remove("")
for price in html_price:
    prices = (price.text.split('+')[0]).split('/')[0]
    property_price.append(prices)

print(property_price)
print(property_name)
