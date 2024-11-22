import os.path

import pygame


class SoundPlayer:
    __KEY_TO_FILENAME = {'0': 'zero.wav', '1': 'one.wav', '2': 'two.wav', '3': 'three.wav', '4': 'four.wav',
                         '5': 'five.wav', '6': 'six.wav', '7': 'seven.wav', '8': 'eight.wav', '9': 'nine.wav',
                         '*': 'star.wav', '#': 'hash.wav', 'A': 'A.wav', 'B': 'B.wav', 'C': 'C.wav', 'D': 'D.wav'}
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
        for key, filename in self.__KEY_TO_FILENAME:
            self.__input_sound_map[key] = self.__get_sound_at("inputs", filename)

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
