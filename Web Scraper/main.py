from bs4 import BeautifulSoup
import requests
response = requests.get("https://news.ycombinator.com/news")
webpage = response.text
article_texts = []
article_links = []
article_score = []
soup = BeautifulSoup(webpage, "html.parser")
article = soup.find_all(name="span", class_="titleline")
for articles in article:
    article_texts.append(articles.getText())
    article_links.append(articles.get("href"))
article_score = [int(score.getText().split(" ")[0]) for score in soup.find_all(name="span", class_="score")]
highest_upvote = int(article_score.index(max(article_score)))
print(article_texts[highest_upvote].split("(")[0])



