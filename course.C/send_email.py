import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "mikebstudy@gmail.com"
password = ""

context = ssl.create_default_context()

receiver = "mikebstudy@gmail.com"
message= """\
Subject: Test message
Hi!
How are you?
Bye
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)