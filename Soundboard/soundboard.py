#!/usr/bin/env python

import sys
import os.path
from pygame import mixer, time

folder = '/home/mike/eva/Soundboard/sounds'
ext = 'mp3'

def play(args):
    try:
        sound = args[0]
    except IndexError:
        msg_text = "What would you like to play?"
        msg = {'msg': msg_text}
        return msg

    path = '%s/%s.%s' % (folder, sound, ext)

    if os.path.isfile(path):
        mixer.init()
        mixer.music.load(path)
        mixer.music.play()      

        #msg_text = "Playing %s.%s" % (sound, ext)
        #msg = {'msg': msg_text}
        #return msg

    else:
        msg_text = "I don't see %s.%s" % (sound, ext)
        msg = {'msg': msg_text}
        return msg