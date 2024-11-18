from KeypadReader import KeypadReader
from PasswordMatcher import PasswordMatcher
from LockOperator import LockOperator

reader = KeypadReader()
matcher = PasswordMatcher()
operator = LockOperator()


def printInfo(info):
    print(info.pincode + " " + info.order_item + " " + info.order_status + " " + info.box_id)


printInfo(matcher.get_order_info("25252"))
printInfo(matcher.get_order_info("3064D"))
printInfo(matcher.get_order_info("B1198"))

"""
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
            else:
                print('Wrong password')
                current_password = ""

"""
