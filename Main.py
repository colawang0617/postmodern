from KeypadReader import KeypadReader
from PasswordMatcher import PasswordMatcher
from LockOperator import LockOperator
from SoundPlayer import SoundPlayer

reader = KeypadReader()
matcher = PasswordMatcher()
operator = LockOperator()
sound_player = SoundPlayer()

current_password = ""
maxlen = matcher.PASSWORD_LENGTH
status = False

while not status:
    operator.update_open_time()
    if operator.is_open_too_long():
        print("The lock has been left open for too long")
        # send email to the user
        operator.reset_open_time()
    if not ((key := reader.read()) is None):
        sound_player.say_pressed_key(key)
        current_password += key
        print(current_password)
        if len(current_password) == maxlen:
            if matcher.is_owner_password(current_password):
                status = True
                print('The password is correct!')
                sound_player.say_correct_password()
                # operator.unlock_door()
                current_password = ""
            elif (order_data := matcher.get_order_info(current_password)) is not None:
                print('an order password is entered for: ')
                print(order_data.order_item)
                sound_player.say_correct_password()
                current_password = ""
                # send email to the user
                # operator.unlock_door()
            else:
                print('Wrong password')
                sound_player.say_wrong_password()
                current_password = ""
