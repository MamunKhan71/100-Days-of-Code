def police(age: int) -> bool:
    if age > 18:
        return "True"
    else:
        return False


if police(24):
    print("You can drive")
else:
    print("You can't")
