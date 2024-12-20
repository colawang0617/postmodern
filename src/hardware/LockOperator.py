import importlib
import time

try:
    importlib.util.find_spec('RPi.GPIO')
    # Using RPi.GPIO, licensed under the MIT License
    import RPi.GPIO as GPIO
except ImportError:
    print("Failed to load library")


class LockOperator:
    __LOCK_PIN = 11
    __LOCK_CHECK_OUT = 19
    __LOCK_CHECK_IN = 26
    __ALLOWED_OPEN_TIME = 60
    LOW = 0
    __open_time = None

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.__LOCK_PIN, GPIO.OUT)
        GPIO.output(self.__LOCK_PIN, GPIO.LOW)

        GPIO.setup(self.__LOCK_CHECK_OUT, GPIO.OUT)
        GPIO.output(self.__LOCK_CHECK_OUT, GPIO.LOW)

        GPIO.setup(self.__LOCK_CHECK_IN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def unlock_door(self):
        GPIO.output(self.__LOCK_PIN, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(self.__LOCK_PIN, GPIO.LOW)
        self.__open_time = time.time()

    def is_lock_open(self):
        return GPIO.input(self.__LOCK_CHECK_IN) != self.LOW

    def is_open_too_long(self):
        close_time = time.time()
        if self.__open_time is None:
            return False
        duration = close_time - self.__open_time
        return duration >= self.__ALLOWED_OPEN_TIME

    def reset_open_time(self):
        self.__open_time = None

    def update_open_time(self):
        if not self.is_lock_open():
            self.reset_open_time()
