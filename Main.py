from KeypadReader import KeypadReader
from PasswordMatcher import PasswordMatcher
from LockOperator import LockOperator

reader = KeypadReader()
matcher = PasswordMatcher()
operator = LockOperator()

current_password = ""
maxlen = matcher.PASSWORD_LENGTH
status = False


def printPassword(password, current_len):
    for i in range(current_len):
        print(password[i], end="")
    print()


while not status:
    if not ((n := reader.read()) is None):
        #if operator.is_lock_open(): print("the lock is open")
        #else: print("the lock is closed")

        current_password += n
        print(current_password)
        if len(current_password) == maxlen:
            if matcher.is_owner_password(current_password):
                status = True
                print('The password is correct!')
                #operator.unlock_door()
            else:
                print('Wrong password')
                current_password = ""
