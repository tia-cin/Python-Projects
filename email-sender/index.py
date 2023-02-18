from email.message import EmailMessage
from priv import password
import ssl
import smtplib

sender = 'cintiaayelenarce@gmail.com'
password = password

receiver = input("Email to: ")

subject = input("Subject: ")
body = input("Body: ")

em = EmailMessage()
em['From'] = sender
em["To"] = receiver
em["subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(sender, password)
    smtp.sendmail(sender, receiver, em.as_string())