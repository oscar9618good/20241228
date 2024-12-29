from dotenv import load_dotenv
import os
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 載入 .env 檔案
load_dotenv()

sender = "oscar9618good@gmail.com"
receiver_list = ["oscar9618good@yahoo.com.tw", "oscar@dotjet.com"]
password_token = os.getenv("PASSWORD_TOKEN")

if not password_token:
    raise ValueError("Password token not found in .env file.")

subject = Header("Test send mail", "utf-8").encode()
body = "This is sent by Python.\nHow are you?"
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender, password_token)
    for recipient in receiver_list:
        msg = MIMEMultipart()
        msg["From"] = sender
        msg["To"] = recipient
        msg["Subject"] = subject
        msg.attach(MIMEText(body))
        server.sendmail(sender, recipient, msg.as_string())
        print(f"Email successfully sent to {recipient}")
