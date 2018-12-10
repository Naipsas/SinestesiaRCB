#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

import subprocess

#from mingus.midi import fluidsynth
#fluidsynth.init('/home/btc/Escritorio/DockerImages/Synesthesia/gfx/dani.opus',"alsa")

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'TFG - Rocío Corbacho Barriga'
        self.initUI()

    def initUI(self):

        # Window maximixed and frameless
        self.setWindowTitle(self.title)
        self.setWindowState(Qt.WindowMaximized)
        self.setWindowFlags(Qt.FramelessWindowHint)

        # Black background
        paleta = self.palette()
        paleta.setColor(self.backgroundRole(), Qt.black)
        self.setPalette(paleta)

        self.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
        else:
            # event.key() == Qt.Key_2:
            #fluidsynth.play_Note(64,0,100)
            subprocess.call(['python2', './app.py'])
            numero = event.key() - 48
            print("pulsado " + str(numero))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())