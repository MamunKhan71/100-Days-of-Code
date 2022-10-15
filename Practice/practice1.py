import csv
with open("weather_report.csv", "r") as weather:
    data = csv.reader(weather)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(row[1])
    print(temperatures)
