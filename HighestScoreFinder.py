score = input("Enter Your Numbers separated by comma \n: ")
maxSc = score.split(",")
newMax = int(maxSc[0])
newMin = int(maxSc[0])
for scr in maxSc:
    if int(scr) > newMax:
        newMax = int(scr)
    if int(scr) < newMin:
        newMin = int(scr)
print(f"The Maximum number is : {newMax}")
print(f"The Minimum number is : {newMin}")
