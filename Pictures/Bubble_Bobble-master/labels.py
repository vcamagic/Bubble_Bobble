from PyQt5.QtWidgets import QWidget
from PyQt5 import QtGui,QtWidgets,QtCore

class Labels:
    def __init__(self , screen: QWidget, broj):
        self.koji = broj
        if self.koji == 0:
            self.label = QtWidgets.QLabel(screen)
            self.label.setGeometry(QtCore.QRect(10, 20, 100, 35))
            self.label.setStyleSheet('background-image: url()')
            font = QtGui.QFont()
            font.setFamily("Playbill")
            font.setPointSize(50)
            self.label.setFont(font)
            self.label.setObjectName("label")
            self.label.setText("Score: ")

            self.points = 0

            self.label_2 = QtWidgets.QLabel(screen)
            self.label_2.setGeometry(QtCore.QRect(10, 39, 55, 100))
            self.label_2.setStyleSheet('background-image: url()')
            font.setPointSize(50)
            self.label_2.setFont(font)
            self.label_2.setObjectName("label2")
            self.label_2.setNum(self.points)

            self.label_3 = QtWidgets.QLabel(screen)
            self.label_3.setGeometry(QtCore.QRect(10, 20, 100, 435))
            self.label_3.setStyleSheet('background-image: url()')
            font = QtGui.QFont()
            font.setFamily("Playbill")
            font.setPointSize(50)
            self.label_3.setFont(font)
            self.label_3.setObjectName("label3")
            self.label_3.setText("LIVES:")

            self.lives = 3

            self.label_4 = QtWidgets.QLabel(screen)
            self.label_4.setGeometry(QtCore.QRect(10, 39, 55, 500))
            self.label_4.setStyleSheet('background-image: url()')
            font = QtGui.QFont()
            font.setFamily("Playbill")
            font.setPointSize(50)
            self.label_4.setFont(font)
            self.label_4.setObjectName("label4")
            self.label_4.setNum(self.lives)

            self.label_5 = QtWidgets.QLabel(screen)
            self.label_5.setGeometry(QtCore.QRect(530, -150, 100, 435))
            self.label_5.setStyleSheet('background-image: url()')
            font = QtGui.QFont()
            font.setFamily("Playbill")
            font.setPointSize(50)
            self.label_5.setFont(font)
            self.label_5.setObjectName("label5")
            self.label_5.setText("LEVEL:")

            self.level = 1

            self.label_6 = QtWidgets.QLabel(screen)
            self.label_6.setGeometry(QtCore.QRect(660, -150, 55, 435))
            self.label_6.setStyleSheet('background-image: url()')
            font = QtGui.QFont()
            font.setFamily("Playbill")
            font.setPointSize(50)
            self.label_6.setFont(font)
            self.label_6.setObjectName("label5")
            self.label_6.setNum(self.level)

    def resetAll1(self):
        self.points = 0
        self.lives = 3
        self.level = 1
        self.label_2.setNum(self.points)
        self.label_4.setNum(self.lives)
        self.label_6.setNum(self.level)

    def changeScore(self, pts):
        self.points = pts
        self.label_2.setNum(self.points)

    def changeLives(self):
        if self.lives - 1 >= 0:
            self.lives -= 1
            self.label_4.setNum(self.lives)

    def changeLevel(self):
        self.level += 1
        self.label_6.setNum(self.level)