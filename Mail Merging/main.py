# Adding Mail Merging with customization features!
with open("./Input/Name/names.txt", "r") as names:
    with open("./Input/Letter/letter.txt", "r") as letter:
        for num in names:
            newNum = num.strip("\n")
            for ltr in letter:
                with open(f"./Output/ReadyToSend/{newNum}.txt", "w") as modFile:
                    newMail = ltr.replace("[name]", newNum)
                    # modFile.write(newMail)

                    modFile.write(str(newMail))




