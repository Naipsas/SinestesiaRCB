#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import time
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QDesktopWidget

from PyQt5.QtGui import QPen, QPainter, QPaintEvent, QConicalGradient, QColor, QBrush

class Circle(QWidget):

    def __init__(self, size, color):
        super().__init__()

        self.loadingAngle = 0
        self.width = 0
        self.color = color
        self.pixmap_opacity = 1

        self.resize(size, size);
        self.center()

        self.initUI()

    def initUI(self):

        self.width = 15
        self.loadingAngle = 0
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def paintEvent(self, qevent):

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("background:transparent;")

        drawingRect = QRect()
        drawingRect.setX(qevent.rect().x() + self.width)
        drawingRect.setY(qevent.rect().y() + self.width)
        drawingRect.setWidth(qevent.rect().width() - self.width * 2)
        drawingRect.setHeight(qevent.rect().height() - self.width * 2)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        gradient = QConicalGradient()
        gradient.setCenter(drawingRect.center())
        gradient.setAngle(90)
        gradient.setColorAt(1, QColor(0,0,0))
        gradient.setColorAt(0, QColor(self.color[0], self.color[1],self.color[2]))

        arcLengthApproximation = self.width + self.width / 3
        pen = QPen(QBrush(gradient), self.width)
        pen.setCapStyle(Qt.RoundCap)
        painter.setPen(pen)
        painter.drawArc(drawingRect, 90 * 16 - arcLengthApproximation, -self.loadingAngle * 16)
        #time.sleep(0.25)

        if self.loadingAngle < 360:
            self.loadingAngle += 1
            #self.paintEvent(QDrawEvent())
            self.paintEvent(QPaintEvent())

        if self.loadingAngle == 360:
            if self.pixmap_opacity > 0:
                self.pixmap_opacity -= 0.05
                #painter.setOpacity(self.pixmap_opacity)
                #self.repaint()
