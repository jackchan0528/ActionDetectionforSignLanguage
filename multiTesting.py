import playsound
from multiprocessing import Process
import os


def play_audio(word):
    playsound.playsound(os.path.join('speech_audio', f'{word}.mp3'))
    # p1 = Process(target=play_audio, args=(word, ))
    # p1.start()


def process_play_audio(word):
    p1 = Process(target=play_audio, args=(word, ))
    p1.start()


if __name__ == '__main__':
    process_play_audio('good')
