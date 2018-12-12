#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import time
import socket
import subprocess
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox

from Clases.Widget import Circle, Cross

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
            self.paintOnScreen(numero)

    def paintOnScreen(self, number):

        cir_sizes = [750, 650, 550, 450, 350]
        cir_colors = [ \
        [53, 6, 81], \
        [4, 8, 79], \
        [7, 77, 96], \
        [13, 114, 99], \
        [10, 91, 33]]

        cross_sizes = [550, 500, 450, 400, 350]
        cross_colors = [ \
        [141, 147, 10], \
        [234, 234, 10], \
        [232, 158, 12], \
        [229, 14, 14], \
        [226, 16, 146] ]

        if (0 <= number) and (number < 5):
            # Circles
            item = Circle(cir_sizes[number], cir_colors[number])
            item.setParent(self)
            item.show()

        else:
            # Lines
            item = Cross(self, cross_sizes[number-5], cross_colors[number-5])

        # Vanish

        # Delete Widget
        #item.deleteLater()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())