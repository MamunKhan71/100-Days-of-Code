import smtplib

import pandas as pd
import random
from datetime import datetime
userEmail = "mamunkhan3523@gmail.com"
userPass = "aefgfgzizrctgrna"
today = datetime.now()
todayDate = (today.month, today.day)

birthday = pd.read_csv("./Birthday Data/birthdays.csv")
birthdayDict = {(row["month"], row["day"]): row for (index, row) in birthday.iterrows()}

if todayDate in birthdayDict:
    birthPerson = birthdayDict[todayDate]
    file_path = f"./letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file=file_path, mode='r') as file:
        newText = file.read()
        newText = newText.replace("[NAME],", birthPerson["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=userEmail, password=userPass)
        connection.sendmail(from_addr=userEmail, to_addrs="mamunkhan3523@yahoo.com", msg=f"Subject: Happy Birthday "
                                                                                         f"{birthPerson['name']}\n\n"
                                                                                         f"{newText}")
        print("Email Sent Successfully!")
else:
    print("No Birthday Today")
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
