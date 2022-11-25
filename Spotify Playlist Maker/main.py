import requests
from bs4 import BeautifulSoup

userDate = input("Type the date you want (YYYY-MM-DD) : ")
response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{userDate}")
soup = BeautifulSoup(response.text, "html.parser")
topSong = soup.find_all("div", class_="o-chart-results-list-row-container")
songList = [song.find('h3').text.strip() for song in topSong]
print(songList)
