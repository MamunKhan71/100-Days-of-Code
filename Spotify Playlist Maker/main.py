import requests
from bs4 import BeautifulSoup

userDate = input("Type the date you want (YYYY-MM-DD) : ")
response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{userDate}")

soup = BeautifulSoup(response.text, "html.parser")
topSong = soup.find("h3", id="title-of-a-story",
                    class_="c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 "
                           "lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 "
                           "u-line-height-normal@mobile-max a-truncate-ellipsis "
                           "u-max-width-330 u-max-width-230@tablet-only")
print(topSong)
