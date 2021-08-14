from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPalette, QBrush
from PyQt5.QtCore import QSize, Qt, QThread ,QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, random, time
import time, variables
from playerstate import  State

class Charachter(QLabel):

    def __init__(self, parent, broj):
        QLabel.__init__(self, parent)
        self.koji = broj
        self.initChar()
        self.jump = State(broj)
        self.jump.start()
        self.time = time.time()
        self.isJumping = False



    def initChar(self):
        if(self.koji==0):
            self.pix1 = QPixmap('Pictures/bbobble.png')
            self.setPixmap(self.pix1.scaled(50,50))
            self.setGeometry(370,552 , 50, 50)
            self.setFixedSize(50, 50)
            #self.setStyleSheet("background-image: url()")
            variables.x = 370
            variables.y = 552
            timer = QTimer(self)
            timer.start(20)
            timer.timeout.connect(self.changePosition)

    def changePosition(self):
        self.move(variables.x, variables.y)
        if variables.charDead == True:
            self.setVisible(False)
        else:
            self.setVisible(True)
        if variables.left == True:
            self.setPixmap(self.pix1.scaled(50,50).transformed((QtGui.QTransform().scale(-1, 1))))
        else:
            self.setPixmap(self.pix1.scaled(50, 50))

    def __update_position__(self, key):
        if self.koji == 0:
            if variables.charDead == False:
                if key == Qt.Key_Space:
                    if self.bullet.shoot.ableToFire == True:
                        self.bullet.shoot.char = self
                        self.bullet.shoot.bullet = self.bullet
                        self.bullet.shoot.ableToFire = False
                        self.bullet.shoot.fireing = True
                if key == Qt.Key_Right:
                    self.jump.movingRight = True
                    self.bullet.shoot.turnedLeft = False
                if key == Qt.Key_Up:
                    self.jump.isJumping = True
                if key == Qt.Key_Left:
                    self.jump.movingLeft = True
                    self.bullet.shoot.turnedLeft = True

