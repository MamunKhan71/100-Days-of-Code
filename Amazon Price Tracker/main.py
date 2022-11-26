import requests
from pprint import pprint
from bs4 import BeautifulSoup

url = "https://www.amazon.com/Instant-Pot-Ultra-Programmable-Sterilizer/dp/B07588SJHN/ref=ex_alt_wg_d?_encoding=UTF8&pd_rd_i=B07588SJHN&pd_rd_w=t7Ud0&pf_rd_p=4e1b46a8-daf9-4433-b97e-d6df97cf3699&pf_rd_r=8EY0YVPAP31Y8RS5MK9N&pd_rd_wg=ptXRO&pd_rd_r=312ff4fa-7c61-4ac3-ba95-8d8028b11a3e&content-id=amzn1.sym.4e1b46a8-daf9-4433-b97e-d6df97cf3699&th=1"

headers = {
    "Request Line": "GET / HTTP/1.1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 "
                  "Safari/537.36",
}

response = requests.get(url=url, headers=headers)
soup = BeautifulSoup(response.text, features="lxml")
price = soup.find("span", class_="a-price-whole")
priceFraction = soup.find("span", class_="a-price-fraction")
priceConvert = float(f"{price.getText()}{priceFraction.getText()}")


