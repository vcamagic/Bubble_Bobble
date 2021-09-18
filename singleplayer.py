from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPalette, QBrush
from PyQt5.QtCore import QSize, Qt
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, random, variables
from labels import Labels
from PyQt5.QtCore import QThread, QTimer

from character import Charachter
from key_notifier import KeyNotifier
from bullet import Bullet
from enemy import Enemy

global label1
global label2
global labele

import time
import  threading

class SinglePlayer(QWidget):
    def __init__(self):
        print('single')
        super().__init__()
        self.label1 = Charachter(self, 0)
        self.label2 = Bullet(self, 0)

        self.enemyLabel1 = Enemy(self, [random.randrange(100, 700, 10), random.randrange(100, 500, 10)], 0,
                               self.label1, 0)
        self.enemyLabel2 = Enemy(self, [random.randrange(100, 700, 10), random.randrange(100, 500, 10)], 1,
                                self.label1, 0)
        self.enemyLabel3 = Enemy(self, [random.randrange(100, 700, 10), random.randrange(100, 500, 10)], 2,
                             self.label1, 0)
        self.enemyLabel4 = Enemy(self, [random.randrange(100, 700, 10), random.randrange(100, 500, 10)], 3,
                                self.label1, 0)

        self.initPrso()
        self.label2.char = self.label1
        self.label1.bullet = self.label2
        self.labele = Labels(self, 0)

        thread = threading.Thread(target=self.points)
        thread.start()

    def initPrso(self):
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)

        self.key_notifier = KeyNotifier()
        self.key_notifier.key_signal.connect(self.label1.__update_position__)

        self.key_notifier.start()

        self.label1.setStyleSheet("background-image: url()")

        self.setStyleSheet("background-image: url(Pictures/level.jpg)")

    def keyPressEvent(self, event):
        self.key_notifier.add_key(event.key())

    def keyReleaseEvent(self, event):
        self.key_notifier.rem_key(event.key())

    def points(self):
        while True:
            if variables.gameLive == True:
                self.labele.changeScore(variables.points)
                if variables.reset == True:
                    self.labele.resetAll1()
                    variables.reset = False
                    variables.points = 0
                if variables.takeLife:
                    self.labele.changeLives()
                    variables.takeLife = False
                    if(variables.lives == 1):
                        variables.gameOver = True
                    variables.lives -= 1
                if variables.increaseLevel:
                    self.labele.changeLevel()
                    variables.increaseLevel = False
                    variables.level += 1
            time.sleep(0.3)
