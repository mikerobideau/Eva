#!/usr/bin/env python

import sys
from pygame import mixer, time

folder = '/home/pi/SmartPi/Soundboard/sounds'
ext = 'mp3'
def play_sound():

    try:
        sound = sys.argv[1]
    except IndexError:
        sys.stdout.write('Please specify a sound name \n')
        return False

    path = '%s/%s.%s' % (folder, sound, ext)
    mixer.init()

    #sys.stdout.write('Searching for %s \n' % (path))

    try:
        mixer.music.load(path)
        mixer.music.play()      
        
        while mixer.music.get_busy():
            time.Clock().tick(10)
        return True

    except Exception:
        sys.stdout.write('Unable to play %s.%s.  Does the file exist? \n' % (sound, ext))
        return False

if __name__ == '__main__':
    play_sound()
