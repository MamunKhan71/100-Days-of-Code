import pandas as pd
temperature = pd.read_csv("./Practice/weather_report.csv")
monday = temperature[temperature.day == "Monday"]
fHeit = (9/5)*float(monday.temp)+32
print(f"Temperature in F is : {fHeit}")
