from dotenv import load_dotenv    # 將敏感資訊存入外部配置檔案，如 .env，並使用程式讀取。
import os                         
# 建立 .env 檔案： 在程式所在目錄中建立 .env，內容如右： PASSWORD_TOKEN=xxxx xxxx xxxx xxxx
# 安裝 python-dotenv 套件： 在終端執行： pip install python-dotenv

import smtplib, ssl                   # 引入 smtplib 和 ssl 模組，用於發送郵件和建立安全連接
from email.mime.text import MIMEText  # 從 email.mime.text 模組引入 MIMEText 類，用於構建純文字的郵件內容
from email.mime.multipart import MIMEMultipart  # 從 email.mime.multipart 模組引入 MIMEMultipart 類，用於構建包含多部分內容的電子郵件
from email.header import Header       # 從 email.header 模組引入 Header 類，用於正確編碼郵件標題中的特殊字符（如非 ASCII 字符）

# 載入 .env 檔案
load_dotenv()

sender = "oscar9618good@gmail.com"     #寄件者
receiver = ["oscar1316good@gmail.com", "oscar9618good@yahoo.com.tw", "oscar@dotjet.com"] #收件者串列
passwordToken = os.getenv("PASSWORD_TOKEN")         #Token從.env檔案中讀取  #從環境變數讀取

if not passwordToken:
    raise ValueError("Password token not found in .env file.")

for recipient in receiver:
    msg = MIMEMultipart()  #建立一個多部分(Multipart）郵件物件，用於構建帶有多個部分（如文字、附件）的電子郵件
    msg["From"] = sender
    msg["To"] = recipient
    # msg["Cc"] = "cc_recipient@example.com"
    msg["Subject"] = Header("Test send mail", "utf-8").encode()  
               # "utf-8"：適用於多語言。"iso-8859-1"：適用於西歐語言。"big5"用於繁體中文
    # from email.utils import formatdate        # 指定郵件的發送日期
    # msg["Date"] = formatdate(localtime=True)  # 使用本地時間


    body = "This is sent by Python.\nHow are you?" 
    # body2 = "Nice to meet you"
    msg_text = MIMEText(body)              # 建立一個 MIMEText 物件，代表郵件的純文字內容
    msg.attach(msg_text)                   # msg_text 是郵件的一部分，通常需要附加到 MIMEMultipart 對象中
    c = ssl.create_default_context()       # 建立一個預設的 SSL 安全上下文，用於加密與伺服器之間的連接

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context= c) as server:  # 使用 SSL 加密協議連接到 Gmail 的 SMTP 伺服器，並將連接對象命名為 server
        server.login(sender, passwordToken)          # 使用發件人的郵件地址和密碼登錄 SMTP 伺服器
        server.sendmail(sender, recipient, msg.as_string())  # 發送郵件，指定發件人、收件人以及郵件內容
    print(f"Email successfully sent to {recipient}")
