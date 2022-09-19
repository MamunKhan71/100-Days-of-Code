year = int(input("Year : "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("This is a Leap Year")
        else:
            print("This is Not a Leap Year")
    else:
        print("This is a Leap Year")
else:
    print("This is Not a Leap Year")
