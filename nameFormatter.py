print("Welcome to Name Formatter")
choice = input("Press Y to Begin N to Exit : ")


def nameFormatter(fName1, lName1):
    new_name = f"{fName1} {lName1}"
    new_name = new_name.title()
    print(new_name)


if choice == "Y":
    fName = input("Enter Your First Name : ")
    lName = input("Enter Your Last Name : ")
    nameFormatter(fName, lName)
else:
    print("Thank you for wasting my time ;-) ")
    exit(0)
