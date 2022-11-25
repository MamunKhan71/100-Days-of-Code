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
present = False
spotifyLogin = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                         client_secret=client_secret, redirect_uri=redirectUrl,
                                                         scope="playlist-modify-private"))

userName = spotifyLogin.me()['display_name']
userId = spotifyLogin.me()['id']
print(songList[1])
songSearch = f"track: {songList[1]} year: {year}"
playlistCheck = f"{userDate} Billboard 100"
demoPlayListCheck = 'Music for Videos 📸'
spotifySearch = spotifyLogin.search(q=songSearch, limit=1, type="track", offset=0)
songId = [spotifySearch['tracks']['items'][0]['id']]
pprint(songId)
currentPlaylists = spotifyLogin.current_user_playlists(limit=20)['items']
# pprint(currentPlaylists)
playlist = spotifyLogin.user_playlist_create(
        user=f"{userId}",
        name=f"{userDate} Billboard 100",
        public=False,
        description=f"A playlist of top 100 from {userDate}"
)
items = spotifyLogin.playlist_add_items(playlist_id=playlist['id'], items=songId[0], position=1)


def playlistChecker():

    for lst in currentPlaylists:
        if lst['name'] == playlistCheck:
            play_list_id = lst['id']
            return play_list_id

    return 0


pcCheck = playlistChecker()
if pcCheck == 0:
    playlist = spotifyLogin.user_playlist_create(
        user=f"{userId}",
        name=f"{userDate} Billboard 100",
        public=False,
        description=f"A playlist of top 100 from {userDate}"
    )
    pcCheck = playlistChecker()

else:
    print(pcCheck)

pprint(currentPlaylists[0]['name'])
pprint(currentPlaylists)
