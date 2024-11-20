import importlib
import time

try:
    importlib.util.find_spec('RPi.GPIO')
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO


class LockOperator:
    __LOCK_PIN = 11
    __LOCK_CHECK_OUT = 19
    __LOCK_CHECK_IN = 26
    LOW = 0

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
        self.open_time = time.time()

    def is_lock_open(self):
        return GPIO.input(self.__LOCK_CHECK_IN) != self.LOW
    
    def time_warnning(self):
        close_time = time.time()
        if self.open_time is None:
            return False
        duration = close_time - self.open_time
        return duration >= 60