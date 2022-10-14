# Adding Mail Merging with customization features!
with open("./Input/Name/names.txt", "r") as names:
    nameList = names.readlines()
    with open("./Input/Letter/letter.txt", "r") as letter:
        ltr = letter.read()
        for num in nameList:
            newNum = num.strip()
            with open(f"./Output/ReadyToSend/{newNum}.txt", "w") as modFile:
                newNumMail = ltr.replace("[name]", newNum)
                modFile.write(newNumMail)





