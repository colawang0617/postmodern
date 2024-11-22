from src.hardware.KeypadReader import KeypadReader
from src.database.PasswordMatcher import PasswordMatcher
from src.hardware.LockOperator import LockOperator
from src.hardware.SoundPlayer import SoundPlayer
from time import sleep

reader = KeypadReader()
matcher = PasswordMatcher()
operator = LockOperator()
sound_player = SoundPlayer()

current_password = ""
maxlen = matcher.PASSWORD_LENGTH
status = False

while not status:
    if not ((key := reader.read()) is None):
        current_password += key
        print(current_password)
        if len(current_password) == maxlen:
            if matcher.is_owner_password(current_password):
                print('The password is correct!')
                sound_player.say_correct_password()
                operator.unlock_door()
                current_password = ""
            elif (order_data := matcher.get_order_info(current_password)) is not None:
                print('an order password is entered for: ')
                print(order_data.order_item)
                current_password = ""
            else:
                print('Wrong password')
                sound_player.say_wrong_password()
                current_password = ""
        else:
            sound_player.say_pressed_key(key)
        sleep(0.1)
