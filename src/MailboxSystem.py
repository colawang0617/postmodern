from src.hardware.KeypadReader import KeypadReader
from src.database.PasswordMatcher import PasswordMatcher
from src.hardware.LockOperator import LockOperator
from src.hardware.SoundPlayer import SoundPlayer
from time import sleep
from src.EmailSender import EmailSender


class MailboxSystem:
    __reader = KeypadReader()
    __matcher = PasswordMatcher()
    __operator = LockOperator()
    __sound_player = SoundPlayer()
    __mailer = EmailSender(__matcher.get_owner_email())
    __current_password = ""
    __password_length = __matcher.PASSWORD_LENGTH

    def __is_password_entered(self):
        return len(self.__current_password) == self.__password_length

    def __open_time_check_action(self):
        self.__operator.update_open_time()
        if self.__operator.is_open_too_long():
            self.__mailer.open_time_warning()
            self.__sound_player.say_open_box_warning()
            self.__operator.reset_open_time()

    def __password_matching_action(self):
        if self.__matcher.is_owner_password(self.__current_password):
            self.__operator.unlock_door()
            self.__sound_player.say_correct_password()
            self.__mailer.owner_open_the_box()
        elif (order_data := self.__matcher.get_order_info(self.__current_password)) is not None:
            self.__operator.unlock_door()
            self.__sound_player.say_correct_password()
            self.__mailer.item_arrival_email(order_data)
        else:
            self.__sound_player.say_wrong_password()
        self.__current_password = ""

    def run_program(self):
        self.__sound_player.play_ready_to_use()
        while True:
            self.__open_time_check_action()
            if (not self.__operator.is_lock_open()) and (not ((key := self.__reader.read()) is None)):
                self.__current_password += key
                if self.__is_password_entered():
                    self.__password_matching_action()
                else:
                    self.__sound_player.say_pressed_key(key)
                sleep(0.2)
