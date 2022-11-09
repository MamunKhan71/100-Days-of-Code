from twilio.rest import Client
import os
import smtplib
import html

user = "mamunkhan3523@gmail.com"
passw = "aefgfgzizrctgrna"


class SmsAlert:
    def __init__(self):
        # self.smsText = None
        pass

    def sms_sender(self, percentage, news):
        account_sid = "AC2376c41ec068151bf6a1db34ac98028c"
        auth_token = "674a29bac39ff84b2a69cd37a480b822"
        client = Client(account_sid, auth_token)
        # self.smsText = f"TSLA: 🔻{percentage}%\nHeadline: {news['title']}\nBrief: {news['description']}"
        # message = client.messages.create(body=self.smsText, from_='+18658003523', to='+12139156465')
        # print(message.sid)

    #
    def emailSender(self, percentage, news):
        smsText = f"TSLA: {percentage}%\nHeadline: {news['title']}\n\nBrief: {news['description']}"
        print(html.unescape(smsText))
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=user, password=passw)
            connection.sendmail(from_addr=user, to_addrs="mkmamun031@gmail.com", msg=f"Subject: Stock Alert \n\n{html.unescape(smsText)}")
            connection.close()
