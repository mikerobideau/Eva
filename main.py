#!/usr/bin/env python

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Parser import parser

app = QApplication(sys.argv)
win = QDialog()
command = QLineEdit(win)

def window(): 
    command.setGeometry(100, 185, 400, 30)
    command.setFont(QFont('Century Gothic', .20))
    command.editingFinished.connect(parse)   

    p = win.palette()
    p.setColor(win.backgroundRole(), Qt.black)
    win.setPalette(p)
    win.setGeometry(0,0,600,400)
    win.setWindowTitle("PyQt")
    win.show()
    sys.exit(app.exec_())
    
def parse():
    parser.parse(command.text())

if __name__ == '__main__':
    window()
