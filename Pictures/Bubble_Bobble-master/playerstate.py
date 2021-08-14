from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QThread, QObject
from PyQt5 import QtGui, QtWidgets
import time

import variables

#y x1 x2

Platforms = [[552, 51, 750],
    [442, 70, 649],
    [332, 160, 574],
    [218, 235, 499]]

movingLeft = False
movingRight = False

class State(QObject):
    isJumping = False
    movingLeft = False
    movingRight = False
    isFalling = False
    onPlatform = True
    jumpCount = 0

    def __init__(self, broj):
        super().__init__()
        self.thread = QThread()
        self.koji = broj
        self.is_done = False
        self.moveToThread(self.thread)
        if self.koji == 0:
            self.pix1 = QPixmap('Pictures/bbobble.png')

        self.thread.started.connect(self.check)
        self.dontJump = False

    def start(self):
        self.thread.start()

    def checkOnPlatform(self):
        self.rec1 = [variables.x, variables.y]
        for x in Platforms:
            if(self.rec1[1] < x[0] + 30 and self.rec1[1] > x[0] and self.rec1[0] > x[1] and self.rec1[0] < x[2] ):
                self.onPlatform = True
                self.isFalling = False
                break
            else:
                self.onPlatform = False
                self.isFalling = True

    def check(self):
        if (self.koji == 0):
            while not self.is_done:
                if (self.isJumping == True and self.onPlatform == True):
                    while self.jumpCount < 40 and variables.y > 20:
                        #ako se pomera i levo da pomeri i tamo
                        if(self.movingLeft == True and variables.x > 55):
                            variables.left = True
                            variables.x -= 5
                            self.movingLeft = False
                        if (self.movingRight == True and variables.x < 720):
                            variables.left = False
                            variables.x += 5
                            self.movingRight = False
                        if ( self.dontJump == True):
                            self.onPlatform = True
                            self.isJumping = False
                            self.isFalling = False
                            break
                        variables.y -= 5
                        self.jumpCount += 1
                        self.thread.msleep(1)
                    self.isJumping = False
                    self.jumpCount = 0
                    self.isFalling = True
                    self.onPlatform = False
                elif(self.isFalling == True):
                    while self.onPlatform == False:
                        if(self.movingLeft == True and variables.x > 55):
                            variables.left = True
                            variables.x -= 5
                            self.movingLeft = False
                        if (self.movingRight == True and variables.x < 720):
                            variables.left = False
                            variables.x += 5
                            self.movingRight = False
                        if (self.dontJump == True):
                            self.onPlatform = True
                            self.isJumping = False
                            self.isFalling = False
                            break
                        variables.y += 5
                        self.thread.msleep(1)
                        self.checkOnPlatform()
                    self.isFalling = False
                elif(self.onPlatform == True and self.movingRight == True and variables.x < 720):
                    variables.left = False
                    variables.x += 5
                    self.checkOnPlatform()
                    self.movingRight = False
                elif (self.onPlatform == True and self.movingLeft == True and variables.x > 55):
                    variables.left = True
                    variables.x -= 5
                    self.checkOnPlatform()
                    self.movingLeft = False
                time.sleep(0.01)





    def kill(self):
        self.is_done = True
        self.thread.quit()