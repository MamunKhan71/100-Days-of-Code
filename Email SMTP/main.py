import smtplib
import ssl
server = None
smtp_server = "smtp.gmail.com"
port = 587
sender_email = "mamunkhan3523@gmail.com"
password = "AtgsWbics3523"
myMsg = "Congratulations! Your mail is received successfully!"
context = ssl.create_default_context()
try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender_email, password)
    server.sendmail(from_addr=sender_email, to_addrs=password, msg=myMsg)
except Exception as e:
    print("Message sending fail. Please Try Again!")
    print(e)

finally:
    server.quit()


