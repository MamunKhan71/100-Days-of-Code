# import smtplib
# myEmail = "mail@gmail.com"
# myPass = "pass"
# myMsg = "Subject:Hello Test\n\nHi there this is an automated email. Testing the workability."
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=myEmail, password=myPass)
#     connection.sendmail(from_addr=myEmail,
#                         to_addrs="mamunkhan3523@yahoo.com",
#                         msg=myMsg
#     )
import datetime as dt
myBirth = dt.datetime(year=1999, month=7,day=1)
print(myBirth)
