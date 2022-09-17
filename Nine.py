print("User Authenticator")
print("##################")
name = input("Enter Your Name \n: ")

if name == "mamun":
    print("Name verification success...")
    password = input("Enter Password to login \n: ")
    if password == "mamun3523":
        print("Logged In Successful...")
    else:
        print("Invalid Login Credentials.. TRY Again!")
