import smtplib
import ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "outsource0075@gmail.com"
    password = os.getenv("pySendEmailPassword")

    receiver = "outsource0075@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


if __name__ == "__main__":
    email_message = """\
Subject: Hi!
How are you?
Bye!
"""
    send_email(email_message)
