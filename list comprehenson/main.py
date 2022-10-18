file1 = open("file1.txt")
file2 = open("file2.txt")

newfile1 = file1.readlines()
newfile2 = file2.readlines()

newList = [int(lists) for lists in newfile1 if lists in newfile2]
aFile = newfile2
print(newList)
