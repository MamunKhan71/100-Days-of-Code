import smtplib
myEmail = "mamunkhan3523@gmail.com"

connect = smtplib.SMTP("smtp.gmail.com")
connect.starttls()
