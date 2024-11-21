from subprocess import call
import pyttsx3



class SoundPlayer:
    __CMD_BEG = 'espeak '
    __CMD_END = ' | aplay /home/pi/Desktop/Text.wav  2>/dev/null'  # To play back the stored .wav file and to dump the std errors to /dev/null
    __CMD_OUT = '--stdout > /home/pi/Desktop/Text.wav '  # To store the voice file
    __CORRECT_PASSWORD = None
    __WRONG_PASSWORD = None
    engine = pyttsx3.init()
    engine.say("Hi My name is Jeff")
    engine.runAndWait()

    volume = engine.getProperty('volume')
    print(volume)
    

    def __init__(self):
        self.__CORRECT_PASSWORD = "Correct Password"
        self.__WRONG_PASSWORD = "Wrong Password"

    def __say_word(self, word):
        call([self.__CMD_BEG + word + self.__CMD_END], shell=True)
        self.engine.say(word)


    def say_pressed_key(self, key):
        if key == '#':
            self.__say_word("Hash")
        elif key == '*':
            self.__say_word("Star")
        else:
            self.__say_word(key)

    def say_correct_password(self):
        self.__say_word(self.__CORRECT_PASSWORD)

    def say_wrong_password(self):
        self.__say_word(self.__WRONG_PASSWORD)
