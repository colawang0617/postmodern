from KeypadReader import KeypadReader
from PasswordMatcher import PasswordMatcher
from LockOperator import LockOperator

reader = KeypadReader()
matcher = PasswordMatcher()
operator = LockOperator()

current_password = ""
maxlen = matcher.PASSWORD_LENGTH
status = False

while not status:
    if not ((n := reader.read()) is None):
        current_password += n
        print(current_password)
        if len(current_password) == maxlen:
            if matcher.is_owner_password(current_password):
                status = True
                print('The password is correct!')
                # operator.unlock_door()
            elif (order_data := matcher.get_order_info(current_password)) is not None:
                print('an order password is entered for: ')
                print(order_data.order_item)
            else:
                print('Wrong password')
                current_password = ""
