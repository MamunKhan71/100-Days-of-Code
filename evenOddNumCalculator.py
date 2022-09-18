ranges = int(input("Enter Your Range : "))
evnSUM = 0
oddSUM = 0
for num in range(1, ranges + 1):
    if num % 2 == 0:
        evnSUM += num
    else:
        oddSUM += num
print(f"Even Sum is : {evnSUM}")
print(f"Odd Sum is : {oddSUM}")
