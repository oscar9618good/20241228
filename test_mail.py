import smtplib, ssl #兩個套組合併成一行, merge 1.2行
from email.mime.text import MIMEText  #大駝峰命名法 #class
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender = "oscar9618good@gmail.com"  #取出重複的字串，例如寄件者
receiver = ["oscar1316good@gmail.com", "oscar9618good@yahoo.com.tw", "oscar@dotjet.com"] 
passwordToken = "tpry awnm qgsh bmes"

for i in receiver:
    msg = MIMEMultipart()  
    msg["From"] = sender
    msg["To"] = i
    msg["Subject"] = Header("Test send mail", "utf-8").encode()    

    body = "This is sent by Python.\nHow are you?" 
    # body2 = "Nice to meet you"
    msg_text = MIMEText(body)              #mail本文
    msg.attach(msg_text)
    c = ssl.create_default_context()       #與google伺服器產生安全溝通

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context= c) as server:  
        server.sendmail(sender, i, msg.as_string())
    print("success send Email")
