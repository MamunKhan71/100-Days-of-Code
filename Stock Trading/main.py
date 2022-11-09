import requests
from newsFetcher import NewsFetcher
from datetime import datetime, timedelta
parameter = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": "TSLA",
    "apikey": "2HPA006D8O95JJDE",
}
newsFetcher = NewsFetcher()
timeDay = datetime.today()
today = str((timeDay - timedelta(days=2)).date())
yesterday = str((timeDay - timedelta(days=3)).date())
print(today)
print(yesterday)
response = requests.get(url="https://www.alphavantage.co/query?", params=parameter)
response.raise_for_status()
data = response.json()
todayStockMarket = float(data["Time Series (Daily)"][today]["4. close"])
yesterdayStockMarket = float(data["Time Series (Daily)"][yesterday]["4. close"])
percentage = round(((yesterdayStockMarket - todayStockMarket)/(
    (todayStockMarket+yesterdayStockMarket)/2) * 100), 2)
if percentage < 5.00:
    news = newsFetcher.top3newsFetcher(today)
    print(type(news))

