# assign key email aspects to variables for easier future editing
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

from pages.base import Base

class Test_Emails:
    def test_sendemail(self):
        subject = "Test Run Report"
        body = "This is an email with the desired report attached"
        sender_email = "neerajvsharma@gmail.com"
        receiver_email = "neerajksharma80@gmail.com"
        filename = "index.html" # in the same directory as script
        filepath = "/Users/neerajsharma/PycharmProjects/Framework_Web/Report/html/"
        b = Base()
        password = b.decrypt_message("VmlubnB2QDE5ODA=")
        # Create the email head (sender, receiver, and subject)
        email = MIMEMultipart()
        email["From"] = sender_email
        email["To"] = receiver_email
        email["Subject"] = subject
        try:
            # Add body and attachment to email
            email.attach(MIMEText(body, "plain"))
            attach_file = open(filepath+filename, "rb") # open the file
            report = MIMEBase("application", "octate-stream")
            report.set_payload((attach_file).read())
            encoders.encode_base64(report)
            #add report header with the file name
            report.add_header("Content-Decomposition", "attachment", filename = filename)
            email.attach(report)
            #Create SMTP session for sending the mail
            session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
            session.starttls() #enable security
            session.login(sender_email, password) #login with mail_id and password
            print("Login Successfull")
            text = email.as_string()
            session.sendmail(sender_email, receiver_email, text)
            print('Mail Sent')
            session.quit()

        except Exception as e:
            print(f"Email Not Sent: {e}")
