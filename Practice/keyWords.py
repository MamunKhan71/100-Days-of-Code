def calculate(defaultNum, **kwargs):
    defaultNum += kwargs["add"]
    defaultNum *= kwargs["mul"]
    defaultNum /= kwargs["div"]

    print(defaultNum)


calculate(defaultNum=5, add=5)
