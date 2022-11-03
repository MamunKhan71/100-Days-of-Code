import pandas as pd
from datetime import datetime
today = datetime.now()
todayDate = (today.month, today.day)

birthday = pd.read_csv("./Birthday Data/birthdays.csv")
birthdayDict = {(row["month"], row["day"]): row for (index, row) in birthday.iterrows()}

if todayDate in birthdayDict:
    print(f"Your Name : {birthdayDict['row']}")


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
