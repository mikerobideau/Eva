#/usr/bin/env python

import sys
import urllib2
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Parser import parser
from Soundboard import soundboard
from Watch import watch
from Places import places
from Weather import weather
from Thing import thing

#Dimensions
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
COMMAND_Y = 10
COMMAND_WIDTH = 700
COMMAND_HEIGHT = 30
MSG_Y = 100
MSG_WIDTH = 1000
MSG_HEIGHT = 140
IMG_Y = 260
CONFIRM_Y = 10
CONFIRM_HEIGHT = 30
CONFIRM_WIDTH = 75

#Widgets
app = QApplication(sys.argv)
win = QDialog()
command_w = QLineEdit(win)
msg_w = QTextEdit(win)
img_w = QLabel(win)
global msg

#Functions
fncs = {
    'soundboard.play': soundboard.play,
    'watch.add_to_watch_list': watch.add_to_watch_list,
    'watch.search_movies': watch.search_movies,
    'places.search': places.search,
    'weather.current': weather.current,
    'thing.add': thing.add,
    'thing.search': thing.search
}

def window(): 
    command_font = QFont()
    command_font.setFamily('Courier New')
    command_font.setPointSize(14)

    command_w.setGeometry((WINDOW_WIDTH - COMMAND_WIDTH) / 2, 10, COMMAND_WIDTH, COMMAND_HEIGHT)
    command_w.setFont(command_font)
    command_w.editingFinished.connect(do_command)   

    msg_font = QFont()
    msg_font.setFamily('Helvetica')
    msg_font.setPointSize(12)

    msg_w.setGeometry((WINDOW_WIDTH - MSG_WIDTH) / 2, MSG_Y, MSG_WIDTH, MSG_HEIGHT)
    msg_w.setReadOnly(True)
    msg_w.setFont(msg_font)

    p = win.palette()
    p.setColor(win.backgroundRole(), Qt.white)
    win.setPalette(p)
    win.setGeometry(0,0, WINDOW_WIDTH, WINDOW_HEIGHT)
    win.setWindowTitle("Eva")
    win.show()
    sys.exit(app.exec_())
    
def do_command():
    print 'Doing command!'

    reset()

    cmd = str(command_w.text())

    if(cmd == 'next'): 
        if msg:
            print 'Current msg is ' + msg
        else:
            print 'No msg found'
        return

    parse = parser.parse(cmd)

    if(not parse):
        return False

    if(not parse['task']):
        return False

    fnc = fncs[parse['task']]

    if(not fnc):
        return

    msg = fnc(parse['args'])

    if msg:
        if 'msg' in msg:
            print msg
            update_msg(msg['msg'])

        if 'img_url' in msg:
            update_img(msg['img_url'], msg['img_width'], msg['img_height'])

def reset():
    img_w.hide()
    msg_w.setText('')

def update_img(url, w, h):
    data = urllib2.urlopen(url).read()
    pixmap = QPixmap()
    pixmap.loadFromData(data)
    img_w.setPixmap(pixmap)
    img_w.setGeometry((WINDOW_WIDTH - w)/ 2, IMG_Y, w, h)
    img_w.show()

def update_msg(msg):
    msg_w.setText(msg)

if __name__ == '__main__':
    window()
