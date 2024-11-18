import importlib
from time import sleep

try:
    importlib.util.find_spec('RPi.GPIO')
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO


class KeypadReader:
    __key_pressed = None
    __COL_PINS = [17, 4, 3, 2]
    __ROW_PINS = [9, 10, 22, 27]
    LOW = 0
    __KEYPAD_MAP = [["1", "4", "7", "*"], ["2", "5", "8", "0"], ["3", "6", "9", "#"], ["A", "B", "C", "D"]]

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        for col in self.__COL_PINS:
            GPIO.setup(col, GPIO.OUT)
        for row in self.__ROW_PINS:
            GPIO.setup(row, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.__set_cols(GPIO.HIGH)

    def __change_key_pressed(self, new_key):
        if self.__key_pressed is None:
            self.__key_pressed = new_key
            return True
        return False

    def __depress_key(self):
        self.__key_pressed = None

    def __set_cols(self, status):
        for col in self.__COL_PINS:
            GPIO.output(col, status)

    def __readInput(self, column, char_map):
        GPIO.output(column, GPIO.LOW)
        for i in range(len(self.__ROW_PINS)):
            if GPIO.input(self.__ROW_PINS[i]) == self.LOW:
                if self.__change_key_pressed(char_map[i]):
                    return char_map[i]
        GPIO.output(column, GPIO.HIGH)
        return None

    def __is_anything_pressed(self):
        self.__set_cols(GPIO.LOW)
        for row in self.__ROW_PINS:
            if GPIO.input(row) == self.LOW:
                self.__set_cols(GPIO.HIGH)
                return True
        self.__set_cols(GPIO.HIGH)
        return False

    def read(self):
        if self.__key_pressed is None:
            for i in range(len(self.__COL_PINS)):
                if not ((ans := self.__readInput(self.__COL_PINS[i], self.__KEYPAD_MAP[i])) is None):
                    sleep(0.1)
                    return ans
        else:
            if not (self.__is_anything_pressed()):
                sleep(0.1)
                self.__depress_key()
            return None
