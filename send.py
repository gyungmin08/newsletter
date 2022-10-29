# send.py

import smtplib
from email.mime.text import MIMEText
from info import *

def send_email(subject, message):
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(sender_email, sender_password)

    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["To"] = receiver_email

    smtp.sendmail(sender_email, receiver_email, msg.as_string())
    smtp.quit()

    return True
