file1 = open("file1.txt")
file2 = open("file2.txt")

newfile1 = file1.readlines()
newfile2 = file2.readlines()

newList = [lists.strip() for lists in newfile1 if newfile2.__contains__(lists)]
aFile = newfile2
print(newList)
