from src.hardware.KeypadReader import KeypadReader
from src.database.PasswordMatcher import PasswordMatcher
from src.hardware.LockOperator import LockOperator
from src.hardware.SoundPlayer import SoundPlayer
from time import sleep


class MailboxSystem:
    __reader = KeypadReader()
    __matcher = PasswordMatcher()
    __operator = LockOperator()
    __sound_player = SoundPlayer()

    __current_password = ""
    __password_length = __matcher.PASSWORD_LENGTH

    def __is_password_entered(self):
        return len(self.__current_password) == self.__password_length

    def __open_time_check_action(self):
        self.__operator.update_open_time()
        if self.__operator.is_open_too_long():
            print("The lock has been left open for too long")
            # send email to the user
            self.__sound_player.say_open_box_warning()
            self.__operator.reset_open_time()

    def __password_matching_action(self):
        if self.__matcher.is_owner_password(self.__current_password):
            self.__sound_player.say_correct_password()
            self.__operator.unlock_door()
        elif (order_data := self.__matcher.get_order_info(self.__current_password)) is not None:
            print(order_data.order_item)
            self.__sound_player.say_correct_password()
            # send email to the user
            self.__operator.unlock_door()
        else:
            self.__sound_player.say_wrong_password()
        self.__current_password = ""

    def run_program(self):
        while True:
            self.__open_time_check_action()
            if not ((key := self.__reader.read()) is None):
                self.__current_password += key
                print(self.__current_password)
                if self.__is_password_entered():
                    self.__password_matching_action()
                else:
                    self.__sound_player.say_pressed_key(key)
                sleep(0.2)
