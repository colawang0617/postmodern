from time import sleep

import importlib.util

try:
    importlib.util.find_spec('RPi.GPIO')
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO

key_pressed = -1
col_pins = [27, 22, 10, 9]
row_pins = [2, 3, 4, 17]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


def change_key_pressed(new_key):
    global key_pressed
    if key_pressed == -1:
        key_pressed = new_key


def set_cols(status):
    for col in col_pins:
        GPIO.output(col, status)


def read(column, char_map):
    GPIO.output(column, GPIO.LOW)
    for i in range(4):
        if GPIO.input(row_pins[i]) == 0:
            print(char_map[i])
            change_key_pressed(1)
    GPIO.output(column, GPIO.HIGH)


for col_pin in col_pins:
    GPIO.setup(col_pin, GPIO.OUT)

for row_pin in row_pins:
    GPIO.setup(row_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

for i in range(20000):
    if key_pressed != -1:
        set_cols(GPIO.LOW)
        if not (GPIO.input(row_pins[0]) == 0 or GPIO.input(row_pins[1]) == 0 or GPIO.input(
                row_pins[2]) == 0 or GPIO.input(row_pins[3]) == 0):
            key_pressed = -1
        sleep(0.1)
        set_cols(GPIO.HIGH)
    else:
        read(col_pins[0], ["1", "4", "7", "*"])
        read(col_pins[1], ["2", "5", "8", "0"])
        read(col_pins[2], ["3", "6", "9", "#"])
        read(col_pins[3], ["A", "B", "C", "D"])
        set_cols(GPIO.HIGH)

print("done")
