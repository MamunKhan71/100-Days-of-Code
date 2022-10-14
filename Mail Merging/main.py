# Adding Mail Merging with customization features!
with open("./Input/Name/names.txt", "r") as names:
    with open("./Input/Letter/letter.txt", "r") as letter:
        ltr = letter.read()
        for num in names:
            newNum = num.strip("\n")
            with open(f"./Output/ReadyToSend/{newNum}.txt", "w") as modFile:
                newNumMail = ltr.replace("[name],", num)
                modFile.write(newNumMail)





