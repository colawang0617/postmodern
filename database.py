import mysql.connector
import random
import os


class PasswordMatcher:
    __HOST = os.environ.get("DATA_HOST")
    __USER = os.environ.get("DATABASE_USER_NAME")
    __PASSWORD = os.environ.get("DATABASE_PASSWORD")
    __DATABASE = os.environ.get("DATABASE_NAME")
    __BOX_ID = os.environ.get("BOX_ID")

    connection = None

    PASSWORD_LENGTH = 5

    def __init__(self):
        self.connection = self.__establish_connection()

    def __establish_connection(self):
        try:
            connection = mysql.connector.connect(host=self.__HOST, user=self.__USER, password=self.__PASSWORD,
                                                 database=self.__DATABASE)
            return connection
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None

    def is_owner_password(self, password):
        result = False
        cursor = None
        try:
            cursor = self.connection.cursor()
            query = """
            SELECT Owner_passcode
            FROM Mailboxes
            WHERE Box_id = {}
            """.format(self.__BOX_ID)

            cursor.execute(query)
            results = cursor.fetchone()

            if results is not None:
                result = results[0] == password

        except mysql.connector.Error as err:
            print(f"Query Error: {err}")
        finally:
            if cursor:
                cursor.close()
            return result

    def init_order_information(self, password, order_item, box_id):
        cursor = self.connection.cursor()
        query = """
        INSERT INTO Passwords
        Values(password,order_item,True,box_id);
        """.format(self.__BOX_ID)
        cursor.execute(query)
        cursor.close()

    def is_unique(self, password):
        cursor = self.connection.cursor()
        query = """
        SELECT Pincode
        FROM Passwords
        WHERE Box_id != {}  AND Pincode = password 
        """.format(self.__BOX_ID)
        cursor.execute(query)
        results = cursor.fetchone
        if (results == None):
            return True
        else:
            return False

    def paired_order(self, password):
        cursor = self.connection.cursor()
        query = """
        SELECT * FROM Passwords
        WHERE Pincode = password
        """.format(self.__BOX_ID)

        cursor.execute(query)

        class result():
            result = cursor.fetchall

        return result
