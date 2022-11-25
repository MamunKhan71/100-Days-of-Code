import requests
import os
from bs4 import BeautifulSoup
import spotipy
from pprint import pprint
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
redirectUrl = "http://example.com"
userDate = input("Type the date you want (YYYY-MM-DD) : ")
year = datetime.strptime(userDate, "%Y-%m-%d").year
response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{userDate}")
soup = BeautifulSoup(response.text, "html.parser")
topSong = soup.find_all("div", class_="o-chart-results-list-row-container")
songList = [song.find('h3').text.strip() for song in topSong]

spotifyLogin = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                         client_secret=client_secret, redirect_uri=redirectUrl))

# userName = spotifyLogin.me()['display_name']
# userId = spotifyLogin.me()['id']
print(songList[0])
spotifySearch = spotifyLogin.search(q=f"{songList[0]} {year}", limit=10, type="track", offset=0)
# print(songList)
pprint(spotifySearch)
