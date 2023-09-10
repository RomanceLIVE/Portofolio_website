import smtplib, ssl
#python email library
#ssl secure library

host = "smtp.gmail.com"
port = 465

username = "robert.horvath93@gmail.com"
password = "occqvucjowjbpujh"

receiver = "robert.horvath93@gmail.com"
context = ssl.create_default_context()

message = """
Hi !
How are you?
Bye !
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
            #context(red) from smtplib is an argument
    server.login(username, password)
    server.sendmail(username, receiver, message)