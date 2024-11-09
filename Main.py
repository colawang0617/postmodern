from KeypadReader import KeypadReader
from PasswordMatcher import PasswordMatcher

reader = KeypadReader()
matcher = PasswordMatcher()

current_password = ""
maxlen = matcher.PASSWORD_LENGTH
status = False


def printPassword(password, current_len):
    for i in range(current_len):
        print(password[i], end="")
    print()


while not status:
    if not ((n := reader.read()) is None):
        current_password += n
        print(current_password)
        if len(current_password) == maxlen:
            if matcher.is_owner_password(current_password):
                status = True
                print('The password is correct!')
            else:
                print('Wrong password')
                current_password = ""
