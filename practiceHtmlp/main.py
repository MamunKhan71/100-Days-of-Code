from bs4 import BeautifulSoup
import requests
response = requests.get("https://news.ycombinator.com/")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
allLinks = soup.find(name="a", class_="title")
print(allLinks)