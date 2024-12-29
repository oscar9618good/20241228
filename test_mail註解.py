# import smtplib    #引用email寄送套組
# import ssl        #引用加密套組
import smtplib, ssl #兩個套組合併成一行, merge 1.2行

    # h = Header("Test send mail", "utf-8")     #UTF-8全語系文字
    # a = h.encode()
    # a = Header("Test send mail", "utf-8").encode()    #merge 5.6行
    # msg["Subject"] = a
    #msg["Subject"] = Header("Test send mail", "utf-8").encode()    #merge 7.8行

#body = "This is sent by Python.\nHow are you?"     #\n換行
#with smtplib.SMTP_SSL("smtp.gmail.com", 465, context= c) as server:  #選擇傳送port通道，google用465

# multireceiver = list(receiver)
# for email in multireceiver:
#     print(email)

# f = open("123.txt")
# f.writelines("hello")
# f.close()
# with open("123.txt") as f:    #merge 18.19.20行   #with, as語法，完成指令後自動結束程式
#     f.writelines("hello")

#for loop
# a = ["abc", "123"]
# for i in a:
#     print(i)       #依序print出list裡的elements