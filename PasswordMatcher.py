import mysql.connector
import os
import random


class PasswordMatcher:
    __HOST = os.environ.get("DATA_HOST")
    __USER = os.environ.get("DATABASE_USER_NAME")
    __PASSWORD = os.environ.get("DATABASE_PASSWORD")
    __DATABASE = os.environ.get("DATABASE_NAME")
    __BOX_ID = os.environ.get("BOX_ID")

    __KEYPAD_CHARACTERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D']
    PASSWORD_LENGTH = 5
    connection = None

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

    def __execute_query(self, query):
        result = None
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            result = cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"Query Error: {err}")
        finally:
            if cursor:
                cursor.close()
            return result

    def is_owner_password(self, password):
        result = self.__execute_query(query="""
            SELECT Owner_passcode
            FROM Mailboxes
            WHERE (Box_id = "{}" AND Owner_passcode = "{}") 
            """.format(self.__BOX_ID, password))

        return result is not None

    def generate_password(self):
        password = ''
        for i in range(self.PASSWORD_LENGTH):
            next_symbol_idx = random.randint(0, len(self.__KEYPAD_CHARACTERS) - 1)
            password += self.__KEYPAD_CHARACTERS[next_symbol_idx]
        return password
