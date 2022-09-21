from art import calculatorLogo

print(calculatorLogo)


def add(num1, num2):
    newVal = num1 + num2
    return newVal


def minus(num1, num2):
    newVal = num1 - num2
    return newVal


def mul(num1, num2):
    newVal = num1 * num2
    return newVal


def div(num1, num2):
    newVal = num1 / num2
    return newVal


userChoice = True
value = 0
preValue = 0
userCc = "n"
while userChoice:
    if userCc == "n":
        numInput = float(input("What's the first number? : "))
    else:
        numInput = preValue
    print("+\n-\n*\n/")
    operator = str(input("Pick an operation : "))
    numInput2 = float(input("What's the next number? : "))
    if operator == "+":
        value = add(numInput, numInput2)
    elif operator == "-":
        value = minus(numInput, numInput2)
    elif operator == "*":
        value = mul(numInput, numInput2)
    elif operator == "/":
        value = div(numInput, numInput2)
    else:
        print("Invalid Operator Selected!")
    print(f"{numInput} {operator} {numInput2} = {value}")
    userCc = input(f"Type y to continue with {value}, or type n to start a new calculation : ")
    if userCc == "y":
        preValue = value
    else:
        userCc = "n"
