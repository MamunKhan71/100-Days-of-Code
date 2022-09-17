print("Welcome to Mamun's Dine")
print("#######")
print("- Menus -")
print("Small Pizza : $15\nMedium Pizza : $20\nLarge Pizza : $25")
print("Pepperoni(Small Pizza) : +$2")
print("Pepperoni(Large Pizza) : +$3")
print("Extra Cheese(Any Size : +$1")
price = 0
print("-------")
choice1 = input("Pizza Size (L | M | S) \n:")
choice2 = input("Pepperoni? (Y | N) \n:")
choice3 = input("Extra Cheese? (Y | N) \n:")

if choice1 == "L" and choice2 == "Y" and choice3 == "Y":
    print("Bill is 25 ")
if choice1 == "L":
    price += 25
    if choice2 == "Y":
        price += 3
        if choice3 == "Y":
            price += 1
if choice1 == "M":
    if choice2 == "Y":
        price += 3
        if choice3 == "Y":
            price += 1
if choice1 == "S":
    if choice2 == "Y":
        price += 2
        if choice3 == "Y":
            price += 1

print(f"Your Bill Is : ${price}")
