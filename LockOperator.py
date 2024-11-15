import importlib
from time import sleep

try:
    importlib.util.find_spec('RPi.GPIO')
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO


class LockOperator:
    __LOCK_PIN = 11

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.__LOCK_PIN, GPIO.OUT)
        GPIO.output(self.__LOCK_PIN, GPIO.LOW)

    def unlock_door(self):
        GPIO.output(self.__LOCK_PIN, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(self.__LOCK_PIN, GPIO.LOW)
