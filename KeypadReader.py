import importlib
from time import sleep

try:
    importlib.util.find_spec('RPi.GPIO')
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO


class KeypadReader:
    key_pressed = None
    COL_PINS = [27, 22, 10, 9]
    ROW_PINS = [2, 3, 4, 17]
    LOW = 0
    KEYPAD_MAP = [["1", "4", "7", "*"], ["2", "5", "8", "0"], ["3", "6", "9", "#"], ["A", "B", "C", "D"]]

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        for col in self.COL_PINS:
            GPIO.setup(col, GPIO.OUT)
        for row in self.ROW_PINS:
            GPIO.setup(row, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.__set_cols(GPIO.HIGH)

    def __change_key_pressed(self, new_key):
        if self.key_pressed is None:
            self.key_pressed = new_key
            return True
        return False

    def __depress_key(self):
        self.key_pressed = None

    def __set_cols(self, status):
        for col in self.COL_PINS:
            GPIO.output(col, status)

    def __readInput(self, column, char_map):
        GPIO.output(column, GPIO.LOW)
        for i in range(len(self.ROW_PINS)):
            if GPIO.input(self.ROW_PINS[i]) == self.LOW:
                if self.__change_key_pressed(char_map[i]):
                    return char_map[i]
        GPIO.output(column, GPIO.HIGH)
        return None

    def __is_anything_pressed(self):
        self.__set_cols(GPIO.LOW)
        for row in self.ROW_PINS:
            if GPIO.input(row) == self.LOW:
                self.__set_cols(GPIO.HIGH)
                return True
        self.__set_cols(GPIO.HIGH)
        return False

    def read(self):
        if self.key_pressed is None:
            for i in range(len(self.COL_PINS)):
                if not ((ans := self.__readInput(self.COL_PINS[i], self.KEYPAD_MAP[i])) is None):
                    return ans
        else:
            if not (self.__is_anything_pressed()):
                sleep(0.1)
                self.__depress_key()
            return None
