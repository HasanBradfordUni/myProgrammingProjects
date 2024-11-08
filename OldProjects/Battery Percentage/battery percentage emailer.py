import os
from email.message import EmailMessage
import ssl, smtplib
import psutil

battery = psutil.sensors_battery()

email_sender = "akhtarhasan2005@gmail.com"
email_password = "nhmgwpldtszyvsoy"
email_receiver = "akhtarhasan2005@gmail.com"

subject = "Battery"
body = "Your battery is now fully charged"

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["Subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

while True:
    try:
        percentage = battery.percent
        if percentage == 100:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, em.as_string())
            break
    except:
        print("No battery is installed, e.g. it is a desktop computer!")
        break

