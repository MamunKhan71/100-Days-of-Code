def isPrime(userInpt):
    temp = 0
    num = 2
    while num != userInpt:
        if userInpt % num == 0:
            temp += 1
        num += 1
    if temp == 0 and userInpt != 1:
        print("Is a Prime Number")
    else:
        print("Is not a prime number")


print("Welcome to prime number checker")

userInput = int(input("Enter a number to check : "))
isPrime(userInpt=userInput)
