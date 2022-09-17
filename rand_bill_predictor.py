import random
billerName = ["Mamun", "Limon", "Shammo", "Faisal", "Shopnil", "Sayed"]
bill_lenght = len(billerName)
randNum = random.randint(0 , bill_lenght)
print(f"{billerName[randNum]} is going to pay the bill today!")
