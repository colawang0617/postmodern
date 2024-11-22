import os.path

import pygame


class SoundPlayer:
    __input_sound_map = {}
    __box_open_sound = None
    __wrong_password_sound = None
    __box_open_warning = None
    __DEF_PATH = os.path.join("assets", "audio")
    __sound_playing = None

    def __init__(self):
        pygame.mixer.init()
        self.__init_sound_map()
        self.__box_open_sound = self.__get_sound_at("feedback", "unlocked.wav")
        self.__wrong_password_sound = self.__get_sound_at("feedback", "wrong_password.wav")
        self.__box_open_warning = self.__get_sound_at("feedback", "close_mailbox.wav")

    def __get_sound_at(self, *args):
        return pygame.mixer.Sound(os.path.join(self.__DEF_PATH, *args))

    def __init_sound_map(self):
        self.__input_sound_map['0'] = self.__get_sound_at("inputs", "zero.wav")
        self.__input_sound_map['1'] = self.__get_sound_at("inputs", "one.wav")
        self.__input_sound_map['2'] = self.__get_sound_at("inputs", "two.wav")
        self.__input_sound_map['3'] = self.__get_sound_at("inputs", "three.wav")
        self.__input_sound_map['4'] = self.__get_sound_at("inputs", "four.wav")
        self.__input_sound_map['5'] = self.__get_sound_at("inputs", "five.wav")
        self.__input_sound_map['6'] = self.__get_sound_at("inputs", "six.wav")
        self.__input_sound_map['7'] = self.__get_sound_at("inputs", "seven.wav")
        self.__input_sound_map['8'] = self.__get_sound_at("inputs", "eight.wav")
        self.__input_sound_map['9'] = self.__get_sound_at("inputs", "nine.wav")
        self.__input_sound_map['*'] = self.__get_sound_at("inputs", "star.wav")
        self.__input_sound_map['#'] = self.__get_sound_at("inputs", "hash.wav")
        self.__input_sound_map['A'] = self.__get_sound_at("inputs", "A.wav")
        self.__input_sound_map['B'] = self.__get_sound_at("inputs", "B.wav")
        self.__input_sound_map['C'] = self.__get_sound_at("inputs", "C.wav")
        self.__input_sound_map['D'] = self.__get_sound_at("inputs", "D.wav")

    def __play_sound(self, sound):
        if self.__sound_playing is not None:
            self.__sound_playing.stop()
        sound.play()
        self.__sound_playing = sound

    def say_pressed_key(self, key):
        self.__play_sound(self.__input_sound_map[key])

    def say_correct_password(self):
        self.__play_sound(self.__box_open_sound)

    def say_wrong_password(self):
        self.__play_sound(self.__wrong_password_sound)

    def say_open_box_warning(self):
        self.__play_sound(self.__box_open_warning)