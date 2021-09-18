from PyQt5.QtWidgets import QLabel
from playerstate import State
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer
from PyQt5 import QtGui
import time
import variables

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
        if(self.koji == 0):
            self.pix1 = QPixmap('Pictures/bbobble.png')
            self.setPixmap(self.pix1.scaled(50,50))
            self.setGeometry(370, 552, 50, 50)
            self.setFixedSize(50, 50)
            variables.x = 370
            variables.y = 552
            timer = QTimer(self)
            timer.start(20)
            timer.timeout.connect(self.changePosition)
        elif(self.koji == 1):
            self.pix1 = QPixmap('Pictures/bbobble2.png')
            self.setPixmap(self.pix1.scaled(50, 50))
            self.setGeometry(540, 552, 50, 50)
            self.setFixedSize(50, 50)
            variables.x2 = 540
            variables.y2 = 552
            timer = QTimer(self)
            timer.start(20)
            timer.timeout.connect(self.changePosition2)

    def changePosition(self):
        self.move(variables.x, variables.y)
        if variables.charDead == True:
            self.setVisible(False)
        else:
            self.setVisible(True)
        if variables.left == True:
            self.setPixmap(self.pix1.scaled(50, 50).transformed((QtGui.QTransform().scale(-1, 1))))
        else:
            self.setPixmap(self.pix1.scaled(50, 50))

    def changePosition2(self):
        self.move(variables.x2, variables.y2)
        if variables.charDead2 == True:
            self.setVisible(False)
        else:
            self.setVisible(True)
        if variables.left2 == True:
            self.setPixmap(self.pix1.scaled(50, 50).transformed((QtGui.QTransform().scale(-1, 1))))
        else:
            self.setPixmap(self.pix1.scaled(50, 50))

    def __update_position__(self, key):
        if self.koji == 0:
            if variables.charDead == False:
                if key == Qt.Key_Plus:
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
        elif self.koji == 1:
            if variables.charDead2 == False:
                if key == Qt.Key_Space:
                    if self.bullet.shoot.ableToFire == True:
                        self.bullet.shoot.char = self
                        self.bullet.shoot.bullet = self.bullet
                        self.bullet.shoot.ableToFire = False
                        self.bullet.shoot.fireing = True
                if key == Qt.Key_D:
                    self.jump.movingRight = True
                    self.bullet.shoot.turnedLeft = False
                if key == Qt.Key_W:
                    self.jump.isJumping = True
                if key == Qt.Key_A:
                    self.jump.movingLeft = True
                    self.bullet.shoot.turnedLeft = True
