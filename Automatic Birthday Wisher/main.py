import pandas as pd
import datetime as dt
Date = dt.datetime.now()
todayMonth = Date.month
todayDate = Date.day
birthdate = (todayMonth, todayDate)
birthday = pd.read_csv("./Birthday Data/birthdays.csv")

birthdayDict = {birthdate: value for (key, value) in birthday.iterrows()}
print(birthdayDict)
# if todayMonth in birthday.iterrows():
#     print("Yes")
# else:
#     print("No")

# birthdayMonth = str(birthdays)
# print(birthdayMonth)
# print(type(birthdayMonth))
# print(todayDate)
# print(todayMonth)
# if todayMonth in birthday.get("month"):
#     print("Exist")
# else:
#     print("Not")
# # 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
