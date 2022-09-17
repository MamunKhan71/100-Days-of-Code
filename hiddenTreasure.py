print("Welcome to hidden treasure land!")
print("#-------------------------------#")
row1 = ["🕳", "🕳", "🕳"]
row2 = ["🕳", "🕳", "🕳"]
row3 = ["🕳", "🕳", "🕳"]
tr_rows = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}\n")
userInput = input("Please specify where you would like to put the treasure!\n: ")
dataExtract = list(userInput)
row = int(dataExtract[0])
column = int(dataExtract[1])
selected_row = tr_rows[row-1]
selected_row[column-1] = "💰"
print(f"{row1}\n{row2}\n{row3}\n")



