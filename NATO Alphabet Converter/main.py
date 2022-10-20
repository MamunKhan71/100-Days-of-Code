# NATO Alphabet Converter!
import pandas
natoLetter = pandas.read_csv("nato_phonetic_alphabet.csv")
userInput = list(input("Enter Your Name: ").upper())
newList = {row.letter: row.code for (index, row) in natoLetter.iterrows() if row.letter in userInput}

nameList = [newList[letter] for letter in userInput]
print(nameList)
