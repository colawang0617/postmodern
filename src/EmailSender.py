import smtplib
import ssl
from email.message import EmailMessage


class EmailSender:
    __sender_address = 'hjjhwan@gmail.com'
    __sender_password = 'bwkl zjfh ewah oilt'
    __owner_email = None

    def __init__(self, owner_email):
        self.__owner_email = owner_email

    def open_time_warning(self):
        subject = 'Please check your mailbox'
        body = """
        The mailbox door has been left open for a prolonged period of time.
        """
        em = EmailMessage()
        em['From'] = self.__sender_address
        em['To'] = self.__owner_email
        em['Subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(self.__sender_address, self.__sender_password)
            smtp.sendmail(self.__sender_address, self.__owner_email, em.as_string())

    def item_arrival_email(self, item_arrived):
        subject = 'Please check your mailbox'
        body = """
        The following item has been delivered to your mailbox:
        {}
        """.format(item_arrived.order_item)
        em = EmailMessage()
        em['From'] = self.__sender_address
        em['To'] = self.__owner_email
        em['Subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(self.__sender_address, self.__sender_password)
            smtp.sendmail(self.__sender_address, self.__owner_email, em.as_string())
