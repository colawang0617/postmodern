from num2words import num2words
from subprocess import call
from KeypadReader import KeypadReader
from PasswordMatcher import PasswordMatcher
from LockOperator import LockOperator

reader = KeypadReader()
matcher = PasswordMatcher()
operator = LockOperator()

current_password = ""
maxlen = matcher.PASSWORD_LENGTH
status = False

cmd_beg= 'espeak '
cmd_end= ' 2>/dev/null'

while not status:
    if not ((n := reader.read()) is None):
        call([cmd_beg+n+cmd_end], shell=True)
        current_password += n
        print(current_password)
        if len(current_password) == maxlen:
            if matcher.is_owner_password(current_password):
                status = True
                print('The password is correct!')
                cmd = 'The password is correct!'
                call([cmd_beg+cmd+cmd_end], shell=True)
                # operator.unlock_door()
            elif (order_data := matcher.get_order_info(current_password)) is not None:
                print('an order password is entered for: ')
                print(order_data.order_item)
                current_password = ""
            else:
                print('Wrong password')
                current_password = ""
