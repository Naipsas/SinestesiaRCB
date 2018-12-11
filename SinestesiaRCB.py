#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import socket
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
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.host = 'localhost';
        self.port = 50288;
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
            #print("end")
            self.s.sendto(bytes("end", "utf-8"), (self.host, self.port))
            self.close()
        else:
            numero = event.key() - 48
            self.s.sendto(bytes(str(numero), "utf-8"), (self.host, self.port))
            #print(str(numero))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())