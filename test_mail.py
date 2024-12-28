# import smtplib    #引用email寄送套組
# import ssl        #引用加密套組
import smtplib, ssl #兩個套組合併成一行, merge 1.2行
from email.mime.text import MIMEText  #大駝峰命名法 #class
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender = "oscar9618good@gmail.com"  #取出重複的字串，例如寄件者
receiver = ["oscar1316good@gmail.com", "oscar9618good@yahoo.com.tw", "oscar@dotjet.com"]   #多個收件者email list
passwordToken = "yvdx hydr ivub tahx"

for i in receiver:
    msg = MIMEMultipart()  
    msg["From"] = sender
    msg["To"] = i
    # h = Header("Test send mail", "utf-8")     #UTF-8全語系文字
    # a = h.encode()
    # a = Header("Test send mail", "utf-8").encode()    #merge 11.12行
    # msg["Subject"] = a
    msg["Subject"] = Header("Test send mail", "utf-8").encode()    #merge 13.14行

    body = "This is sent by Python.\nHow are you?"     #\n換行
    # body2 = "Nice to meet you"
    msg_text = MIMEText(body)   #mail本文
    msg.attach(msg_text)
    c = ssl.create_default_context()       #與google伺服器產生安全溝通

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context= c) as server:    #選擇傳送port通道，google用465
        server.login(sender, passwordToken)
        server.sendmail(sender, i, msg.as_string())
    print("success send Email")

# multireceiver = list(receiver)
# for email in multireceiver:
#     print(email)

# f = open("123.txt")
# f.writelines("hello")
# f.close()
# with open("123.txt") as f:    #merge 22.23.24行   #with, as語法，完成指令後自動結束程式
#     f.writelines("hello")
