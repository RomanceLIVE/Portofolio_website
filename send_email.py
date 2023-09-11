import smtplib, ssl
#python email library
#ssl secure library
import  os

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "robert.horvath93@gmail.com"
    password = (os.getenv("PASSWORD"))

    # os.getenv("PASSWORD")) use this line in password =" "  when u share code with ppl
    # we store our password on Pc using event variables
    # in case we share the code with ppl
    receiver = "robert.horvath93@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        # context(red) from smtplib is an argument
        server.login(username, password)
        server.sendmail(username, receiver, message)




# def send_email(): was made by selecting the code and refactor then extract method
# send_email() will call that function
