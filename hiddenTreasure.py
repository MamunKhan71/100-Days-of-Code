print("Welcome to hidden treasure land!")
print("#-------------------------------#")
row1 = ["🕳", "🕳", "🕳"]
row2 = ["🕳", "🕳", "🕳"]
row3 = ["🕳", "🕳", "🕳"]
tr_rows = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}\n")
userInput = input("Please specify where you would like to put the treasure!\n: ")
row = int(userInput[0])
column = int(userInput[1])
tr_rows[column-1][row-1] = "💰"
print(f"{row1}\n{row2}\n{row3}\n")



