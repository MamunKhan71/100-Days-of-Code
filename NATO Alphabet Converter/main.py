# NATO Alphabet Converter!
import pandas
natoLetter = pandas.read_csv("nato_phonetic_alphabet.csv")

newList = {row.letter: row.code for (index, row) in natoLetter.iterrows()}

looper = True
while looper:
    userInput = input("Enter Your Name: ").upper()
    try:
        nameList = [newList[letter] for letter in userInput]
    except KeyError:
        print("Only Letters Are Allowed!")
    else:
        print(nameList)
        break
