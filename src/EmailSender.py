import smtplib
import ssl
import os
from email.message import EmailMessage


class EmailSender:
    __sender_address = os.environ.get("SENDER_ADDRESS")
    __sender_password = os.environ.get("SENDER_PASSWORD")
    __owner_email = None

    def __init__(self, owner_email):
        self.__owner_email = owner_email

    def __send_email(self, subject, body):
        em = EmailMessage()
        em['From'] = self.__sender_address
        em['To'] = self.__owner_email
        em['Subject'] = subject
        em.set_content(body)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(self.__sender_address, self.__sender_password)
            smtp.sendmail(self.__sender_address, self.__owner_email, em.as_string())

    def open_time_warning(self):
        body = 'The mailbox door has been left open for a prolonged period of time'
        self.__send_email('Please check your mailbox', body)

    def item_arrival_email(self, item_arrived):
        body = """ The following item has been delivered to your mailbox: {}
            """.format(item_arrived.order_item)
        self.__send_email('Please check your mailbox', body)

    def owner_open_the_box(self):
        body = 'If you are not aware of this happening, please change your password.'
        self.__send_email('The mailbox was opened using your password', body)
