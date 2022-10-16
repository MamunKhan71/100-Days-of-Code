import csv
import pandas as pd

# with open("weather_report.csv", "r") as weather:
#     data = csv.reader(weather)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)
temperature = pd.read_csv("weather_report.csv")
monday = temperature[temperature.day == "Monday"]
fHeit = (9/5)*float(monday.temp)+32
print(fHeit)

