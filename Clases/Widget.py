#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import time
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt, QRect, QTimeLine
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QDesktopWidget

class Circle(QWidget):

    def __init__(self, size, color):
        super().__init__()

        self._loading_angle = 0
        self.width = 0
        self.color = color

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("background:transparent;")

        self.resize(size, size);
        self.center()
        self.initUI()

        timeline = QTimeLine(1500, self)
        timeline.setFrameRange(360, 0)
        timeline.frameChanged.connect(self.setLoadingAngle)
        timeline.start()

        #time.sleep(2)

        #timeline.setFrameRange(360, 0)
        #timeline.frameChanged.connect(self.setLoadingAngle)
        #timeline.start()

    def initUI(self):

        self.width = 15
        self.setLoadingAngle(0)
        self.show()

    def loadingAngle(self):
        return self._loading_angle

    def setLoadingAngle(self, angle):
        self._loading_angle = angle
        self.update()

    loadingAngle = QtCore.pyqtProperty(int, fget=loadingAngle, fset=setLoadingAngle)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def paintEvent(self, event):

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("background:transparent;")

        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        drawingRect  = QRect(QtCore.QPoint(), self.rect().size() - 2*self.width*QtCore.QSize(1, 1))
        drawingRect.moveCenter(self.rect().center())

        gradient = QtGui.QConicalGradient()
        gradient.setCenter(drawingRect.center())
        gradient.setAngle(90)
        gradient.setColorAt(1, QtGui.QColor(0,0,0))
        gradient.setColorAt(0, QtGui.QColor(self.color[0],self.color[1],self.color[2] ))

        arcLengthApproximation = self.width + self.width / 3
        pen = QtGui.QPen(QtGui.QBrush(gradient), self.width)
        pen.setCapStyle(QtCore.Qt.RoundCap)
        painter.setPen(pen)
        painter.drawArc(drawingRect, 90 * 16 - arcLengthApproximation, -self._loading_angle * 16)

class Cross():

    def __init__(self, parent, size, color):

        # First arm
        item = Line(size, color, "L")
        item.setParent(parent)
        item.show()

        # Second
        item = Line(size, color, "R")
        item.setParent(parent)
        item.show()

class Line(QWidget):

    def __init__(self, size, color, side):
        super().__init__()

        self._next_step = 0
        self.width = 0
        self.color = color
        self.side = side

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("background:transparent;")

        self.resize(size, size);
        self.center()
        self.initUI()

        timeline = QTimeLine(1500, self)
        timeline.setFrameRange(size, 0)
        timeline.frameChanged.connect(self.setNextStep)
        timeline.start()

    def initUI(self):

        self.width = 15
        self.setNextStep(0)
        self.show()

    def NextStep(self):
        return self._next_step

    def setNextStep(self, step):
        self._next_step = step
        self.update()

    NextStep = QtCore.pyqtProperty(int, fget=NextStep, fset=setNextStep)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def paintEvent(self, event):

        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        drawingRect  = QRect(QtCore.QPoint(), self.rect().size() - 2*self.width*QtCore.QSize(1, 1))
        drawingRect.moveCenter(self.rect().center())

        gradient = QtGui.QConicalGradient()
        gradient.setCenter(drawingRect.center())
        gradient.setAngle(90)
        gradient.setColorAt(1, QtGui.QColor(0,0,0))
        gradient.setColorAt(0, QtGui.QColor(self.color[0],self.color[1],self.color[2] ))

        arcLengthApproximation = self.width + self.width / 3
        pen = QtGui.QPen(QtGui.QBrush(gradient), self.width)
        pen.setCapStyle(QtCore.Qt.RoundCap)
        painter.setPen(pen)
        #painter.drawArc(drawingRect, 90 * 16 - arcLengthApproximation, -self._loading_angle * 16)
        if self.side == "L":
            painter.drawLine(0,0, self.NextStep, self.NextStep)
        else:
            painter.drawLine(drawingRect.width(), 0, drawingRect.width() - self.NextStep, self.NextStep)
