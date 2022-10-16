import pandas as pd
sqRL = pd.read_csv("Squirrel_Data_2018.csv")
colorSL = sqRL["Primary Fur Color"]
gray = len(colorSL[colorSL == "Gray"])
red = len(colorSL[colorSL == "Cinnamon"])
black = len(colorSL[colorSL == "Black"])

squirrel_count = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [gray, red, black]
}
dataConverter = pd.DataFrame(squirrel_count)
print(dataConverter)
dataConverter.to_csv("squirrel_count")

