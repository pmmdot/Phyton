import smtplib
import ssl

from email.message import EmailMessage

email_sender = 'c3.prajwalmm.mlo.2020@gmail.com'
email_password = 'aomiflmfjpvrpwpf'
email_receiver = input("Enter the receivers mailid: ")

subject = input("Enter the subject: ")
body = input("Enter the body: ")
r = int(input("Enter no of mails: "))

em = EmailMessage()

em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject

em.set_content(body)
context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    for no in range(r):
        smtp.sendmail(email_sender, email_receiver, em.as_string())
        print(f"{no+1}th Email sent!")