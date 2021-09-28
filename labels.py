from PyQt5.QtWidgets import QWidget
from PyQt5 import QtGui, QtWidgets, QtCore

class Labels:
    def __init__(self , screen: QWidget, broj):
        self.koji = broj
        if self.koji == 0:
            self.label = QtWidgets.QLabel(screen)
            self.label.setGeometry(QtCore.QRect(0, 592, 200, 30))
            self.label.setStyleSheet('background: pink')
            font = QtGui.QFont()
            font.setFamily("Playbill")
            font.setPointSize(15)
            self.label.setFont(font)
            self.label.setObjectName("label")
            self.label.setText("Score: ")

            self.points = 0

            self.label_2 = QtWidgets.QLabel(screen)
            self.label_2.setGeometry(QtCore.QRect(65, 592, 40, 30))
            self.label_2.setStyleSheet('background-image: url()')
            font = QtGui.QFont()
            font.setFamily("Playbill")
            font.setPointSize(15)
            self.label_2.setFont(font)
            self.label_2.setObjectName("label2")
            self.label_2.setNum(self.points)

            self.label_3 = QtWidgets.QLabel(screen)
            self.label_3.setGeometry(QtCore.QRect(80, 592, 50, 30))
            self.label_3.setStyleSheet('background-image: url()')
            font = QtGui.QFont()
            font.setFamily("Playbill")
            font.setPointSize(15)
            self.label_3.setFont(font)
            self.label_3.setObjectName("label3")
            self.label_3.setText("Lives:")

            self.lives = 3

            self.label_4 = QtWidgets.QLabel(screen)
            self.label_4.setGeometry(QtCore.QRect(135, 592, 70, 30))
            self.label_4.setStyleSheet('background-image: url()')
            font = QtGui.QFont()
            font.setFamily("Playbill")
            font.setPointSize(15)
            self.label_4.setFont(font)
            self.label_4.setObjectName("label4")
            self.label_4.setNum(self.lives)

            self.label_5 = QtWidgets.QLabel(screen)
            self.label_5.setGeometry(QtCore.QRect(351, 592, 100, 30))
            self.label_5.setStyleSheet('background: yellow')
            font = QtGui.QFont()
            font.setFamily("Playbill")
            font.setPointSize(15)
            self.label_5.setFont(font)
            self.label_5.setObjectName("label5")
            self.label_5.setText("LEVEL:")

            self.level = 1

            self.label_6 = QtWidgets.QLabel(screen)
            self.label_6.setGeometry(QtCore.QRect(415, 592, 30, 30))
            self.label_6.setStyleSheet('background-image: url()')
            font = QtGui.QFont()
            font.setFamily("Playbill")
            font.setPointSize(15)
            self.label_6.setFont(font)
            self.label_6.setObjectName("label5")
            self.label_6.setNum(self.level)

        else:
            self.label = QtWidgets.QLabel(screen)
            self.label.setGeometry(QtCore.QRect(0, 592, 200, 30))
            self.label.setStyleSheet('background: pink')
            font = QtGui.QFont()
            font.setFamily("Playbill")
            font.setPointSize(15)

            self.label.setFont(font)
            self.label.setObjectName("label")
            self.label.setText("Score1: ")

            self.points = 0

            self.label_2 = QtWidgets.QLabel(screen)
            self.label_2.setGeometry(QtCore.QRect(65, 592, 40, 30))
            self.label_2.setStyleSheet('background-image: url()')
            font = QtGui.QFont()
            font.setFamily("Playbill")
            font.setPointSize(15)
            self.label_2.setFont(font)
            self.label_2.setObjectName("label2")
            self.label_2.setNum(self.points)

            self.label_3 = QtWidgets.QLabel(screen)
            self.label_3.setGeometry(QtCore.QRect(90, 592, 50, 30))
            self.label_3.setStyleSheet('background-image: url()')
            font = QtGui.QFont()
            font.setFamily("Playbill")
            font.setPointSize(15)
            self.label_3.setFont(font)
            self.label_3.setObjectName("label3")
            self.label_3.setText("Lives:")

            self.lives = 3

            self.label_4 = QtWidgets.QLabel(screen)
            self.label_4.setGeometry(QtCore.QRect(145, 592, 50, 30))
            self.label_4.setStyleSheet('background-image: url()')
            font = QtGui.QFont()
            font.setFamily("Playbill")
            font.setPointSize(15)
            self.label_4.setFont(font)
            self.label_4.setObjectName("label4")
            self.label_4.setNum(self.lives)

            self.label_5 = QtWidgets.QLabel(screen)
            self.label_5.setGeometry(QtCore.QRect(351, 592, 100, 30))
            self.label_5.setStyleSheet('background: yellow')
            font = QtGui.QFont()
            font.setFamily("Playbill")
            font.setPointSize(18)
            self.label_5.setFont(font)
            self.label_5.setObjectName("label5")
            self.label_5.setText("LEVEL:")

            self.level = 1

            self.label_6 = QtWidgets.QLabel(screen)
            self.label_6.setGeometry(QtCore.QRect(435, 592, 30, 30))
            self.label_6.setStyleSheet('background: yellow')
            font = QtGui.QFont()
            font.setFamily("Playbill")
            font.setPointSize(18)
            self.label_6.setFont(font)
            self.label_6.setObjectName("label5")
            self.label_6.setNum(self.level)
#drugi igrac
            self.label_7 = QtWidgets.QLabel(screen)
            self.label_7.setGeometry(QtCore.QRect(600, 592, 200, 30))
            self.label_7.setStyleSheet('background: pink')
            font = QtGui.QFont()
            font.setFamily("Playbill")
            font.setPointSize(15)
            self.label_7.setFont(font)
            self.label_7.setObjectName("label")
            self.label_7.setText("Score2:")

            self.points2 = 0

            self.label_8 = QtWidgets.QLabel(screen)
            self.label_8.setGeometry(QtCore.QRect(670, 592, 40, 30))
            self.label_8.setStyleSheet('background-image: url()')
            font = QtGui.QFont()
            font.setFamily("Playbill")
            font.setPointSize(15)
            self.label_8.setFont(font)
            self.label_8.setObjectName("label2")
            self.label_8.setNum(self.points2)

            self.label_9 = QtWidgets.QLabel(screen)
            self.label_9.setGeometry(QtCore.QRect(690, 592, 50, 30))
            self.label_9.setStyleSheet('background-image: url()')
            font = QtGui.QFont()
            font.setFamily("Playbill")
            font.setPointSize(15)
            self.label_9.setFont(font)
            self.label_9.setObjectName("label3")
            self.label_9.setText("Lives:")

            self.lives2 = 3

            self.label_10 = QtWidgets.QLabel(screen)
            self.label_10.setGeometry(QtCore.QRect(745, 592, 50, 30))
            self.label_10.setStyleSheet('background-image: url()')
            font = QtGui.QFont()
            font.setFamily("Playbill")
            font.setPointSize(15)
            self.label_10.setFont(font)
            self.label_10.setObjectName("label4")
            self.label_10.setNum(self.lives2)

    def resetAll1(self):
        self.points = 0
        self.lives = 3
        self.level = 1
        self.label_2.setNum(self.points)
        self.label_4.setNum(self.lives)
        self.label_6.setNum(self.level)

    def resetAll2(self):
        self.points = 0
        self.lives2 = 3
        self.level = 1
        self.label_2.setNum(self.points)
        self.label_4.setNum(self.lives)
        self.label_6.setNum(self.level)
        self.points2 = 0
        self.lives2 = 3
        self.label_8.setNum(self.points2)
        self.label_10.setNum(self.lives2)

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

    def changeScore2(self, pts):
        self.points2 = pts
        self.label_8.setNum(self.points2)

    def changeLives2(self):
        if self.lives2 - 1 >= 0:
            self.lives2 -= 1
            self.label_10.setNum(self.lives2)