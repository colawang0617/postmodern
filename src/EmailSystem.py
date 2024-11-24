import smtplib
import ssl
from email.message import EmailMessage

class EmailSender:
    
    email_sender = 'hjjhwan@gmail.com'
    email_password = 'bwkl zjfh ewah oilt'

    def __too_long_email(self,email):
        subject = 'Messege from PostModern'
        body = """
        The lock has been left open for too long!!
        """
        em = EmailMessage()
        em['From'] = self.email_sender
        em['To'] = email
        em['Subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
         smtp.login(self.email_sender, self.email_password)
         smtp.sendmail(self.email_sender, self.email_receiver, em.as_string())

    def __item_arrival_email(self,email):
        subject = 'Messege from PostModern'
        body = """
        There is a new item arriving in your mailbox!!
        """
        em = EmailMessage()
        em['From'] = self.email_sender
        em['To'] = email
        em['Subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
         smtp.login(self.email_sender, self.email_password)
         smtp.sendmail(self.email_sender, self.email_receiver, em.as_string())


    