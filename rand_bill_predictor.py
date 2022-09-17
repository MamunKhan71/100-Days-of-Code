import random

billerName = ["Mamun", "Limon", "Shammo", "Faisal", "Shopnil", "Sayed"]
bill_len = len(billerName)-1
randNum = random.randint(0, bill_len)
print(f"{billerName[randNum]} is going to pay the bill today!")
