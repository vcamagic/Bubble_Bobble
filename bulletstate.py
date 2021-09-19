from PyQt5.QtWidgets import *

from PyQt5.QtCore import QThread, QObject

import time, gc, variables

class BulletSate(QGraphicsObject):
    char = QLabel
    bullet = QLabel
    fireing = False
    ableToFire = True
    turnedLeft = False
    substract = False
    p = 0

    def __init__(self, broj):
        super().__init__()
        self.thread = QThread()
        self.is_done = False
        self.koji = broj
        self.moveToThread(self.thread)


        self.thread.started.connect(self.fire)

    def start(self):
        self.thread.start()

    def fire(self):
        if self.koji == 0:
            while not self.is_done:
                if self.fireing == True:
                    self.fireing = False
                    variables.isShot = True
                    self.bullet.setVisible(True)
                    self.position = self.char.geometry()
                    variables.bulletX = self.position.x()
                    variables.bulletY = self.position.y()
                    self.x = self.position.x()
                    self.substract = True
                    if self.turnedLeft == False:
                        self.x += 20
                        variables.bulletX = self.x
                        self.substract = False
                    while self.p < 50:
                        if variables.bulletused == True:
                            self.bullet.setVisible(False)
                            self.thread.msleep(1)
                        else:
                            if self.substract == False:
                                self.bullet.setGeometry(self.x, self.position.y(), 30, 30)
                                self.x += 5
                                variables.bulletX = self.x
                                self.thread.msleep(1)
                            else:
                                self.bullet.setGeometry(self.x, self.position.y(), 30, 30)
                                self.x -= 5
                                variables.bulletX = self.x
                                self.thread.msleep(1)
                        self.p += 1
                    self.fireing = False
                    variables.isShot = False
                    self.ableToFire = True
                    self.p = 0
                    self.bullet.setVisible(False)
                    variables.bulletused = False
                time.sleep(0.001)
        elif self.koji == 1:
            while not self.is_done:
                if self.fireing == True:
                    self.fireing = False
                    variables.isShot2 = True
                    self.bullet.setVisible(True)
                    self.position = self.char.geometry()
                    variables.bullet2X = self.position.x()
                    variables.bullet2Y = self.position.y()
                    self.x = self.position.x()
                    self.substract = True
                    if self.turnedLeft == False:
                        self.x += 20
                        variables.bullet2X = self.x
                        self.substract = False
                    while self.p < 50:
                        if variables.bulletused2 == True:
                            self.bullet.setVisible(False)
                            self.thread.msleep(1)
                        else:
                            if self.substract == False:
                                self.bullet.setGeometry(self.x, self.position.y(), 30, 30)
                                self.x += 5
                                variables.bullet2X = self.x
                                self.thread.msleep(1)
                            else:
                                self.bullet.setGeometry(self.x, self.position.y(), 30, 30)
                                self.x -= 5
                                variables.bullet2X = self.x
                                self.thread.msleep(1)
                        self.p += 1
                    self.fireing = False
                    variables.isShot2 = False
                    self.ableToFire = True
                    self.p = 0
                    self.bullet.setVisible(False)
                    variables.bulletused2 = False
                time.sleep(0.001)
