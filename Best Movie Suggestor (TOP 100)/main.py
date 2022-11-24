import requests
from bs4 import BeautifulSoup
response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best"
                        "-movies-2/").text
movieList = []
soup = BeautifulSoup(response, "html.parser")
article_text = soup.find_all("h3", class_="title")

for movieName in article_text:
    movieList.append((movieName.getText()))

with open(file="movieList.txt", mode="w", encoding="utf-8") as file:
    for lst in movieList[::-1]:
        file.write(f"{lst}\n")

