print("Welcome to FizzBuzz Game")
choice = int(input("1.Start\n2.Exit \n: "))
if choice == 1:
    inChoice = int(input("Enter The Max Range \n: "))
    for num in range(1, inChoice+1):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
else:
    exit(0)
