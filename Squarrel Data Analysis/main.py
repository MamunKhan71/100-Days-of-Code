import pandas as pd
sqRL = pd.read_csv("Squirrel_Data_2018.csv")
greySL = sqRL["Primary Fur Color"]
gray = len(greySL[greySL == "Gray"])
red = len(greySL[greySL == "Cinnamon"])
black = len(greySL[greySL == "Black"])

squirrel_count = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [gray, red, black]
}
dataConverter = pd.DataFrame(squirrel_count)
print(dataConverter)
dataConverter.to_csv("squirrel_count")

