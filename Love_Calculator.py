print("Welcome to love calculator")
print("##########################")
yourName = input("Enter Your Name : ")
herName = input("Enter His/Her Name : ")
combineName = (yourName + herName).lower()
t = combineName.count("t")
r = combineName.count("r")
u = combineName.count("u")
e = combineName.count("e")
true = t + r + u + e
l = combineName.count("l")
o = combineName.count("o")
v = combineName.count("v")
e = combineName.count("e")
love = l + o + v + e
score = int(str(true) + str(love))
if (score < 10) or (score > 90):
    print(f"Your love score is {score}, You go together like coke and mentos")
if (score >= 40) and (score <= 50):
    print(f"Your love score is {score}, You are alright together!")
else:
    print(f"Your love score is {score}")
