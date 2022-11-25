import requests
import os
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
redirectUrl = "http://example.com"
userDate = input("Type the date you want (YYYY-MM-DD) : ")
response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{userDate}")
soup = BeautifulSoup(response.text, "html.parser")
topSong = soup.find_all("div", class_="o-chart-results-list-row-container")
songList = [song.find('h3').text.strip() for song in topSong]
print(songList)

spotifyLogin = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                         client_secret=client_secret, redirect_uri=redirectUrl))

userName = spotifyLogin.me()['display_name']
userId = spotifyLogin.me()['id']
spotifySearch = spotifyLogin.search(q="Dreams Revisited", limit=10, type="track", offset=0)
