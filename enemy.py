import math

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtCore import QTimer
import random
import variables

class Enemy(QLabel):
    def __init__(self, parent, coords, broj, char, neki):
        print('usao u enemy')
        QLabel.__init__(self, parent)
        self.character = char
        self.kojiBroj = neki
        self.isHit = False
        variables.currentPositionEnemy[broj] = coords
        self.init(coords[0], coords[1])
        print(coords[0] + coords[1])
        self.koji = broj
        print(self.koji)



    def init(self, x, y):
        self.pix1 = QPixmap('Pictures/enemy_black.png')
        self.setPixmap(self.pix1.scaled(50, 50))
        self.setGeometry(x, y, 50, 50)
        self.setFixedSize(50, 50)
        self.setStyleSheet("background-image: url()")
        timer = QTimer(self)
        timer.start(20)
        timer.timeout.connect(self.changePosition)


    def changePosition(self):
        if variables.gameLive == True and self.kojiBroj == 0:
            if((variables.currPos[self.koji][0] - 50 < variables.x and variables.currPos[self.koji][0] + 50 > variables.x) and
                    (variables.currPos[self.koji][1] - 50 < variables.y and variables.currPos[self.koji][1] + 50 > variables.y) and variables.Collected[self.koji]==False):
                variables.Collected[self.koji] = True
                variables.collectedEnemy += 1
                variables.points += 1
            if variables.Frozen[self.koji] == True:
                self.pix1 = QPixmap('Pictures/dead_enemy.png')
                self.setPixmap(self.pix1.scaled(30, 30))
            else:
                self.pix1 = QPixmap('Pictures/enemy_black.png')
                self.setPixmap(self.pix1.scaled(50, 50))
                self.setVisible(True)

            self.position = self.geometry()

            if variables.Collected[self.koji] == True:
                self.setVisible(False)

            if variables.isShot == True and variables.bulletused == False and variables.Frozen[self.koji] == False :
                if(self.position.x() < variables.bulletX and self.position.x() + 50 > variables.bulletX) and (self.position.y() - 50 < variables.bulletY and self.position.y() + 50 > variables.bulletY):
                    self.isHit = True
                    variables.aliveEnemy -= 1
                    variables.deadEnemy += 1
                    variables.Frozen[self.koji] = True
                    variables.currPos[self.koji][0] = self.position.x()
                    variables.currPos[self.koji][1] = self.position.y()
                    variables.bulletused = True
                    variables.points += 1

            if variables.Frozen[self.koji] == False:
                if(self.position.x() - 50 < variables.x and self.position.x() + 50 > variables.x ) and (self.position.y() - 50 < variables.y and self.position.y() + 50 > variables.y ):
                    variables.charDead = True
                    variables.takeLife = True
                    print(variables.lives)

            self.whereToGo2()

            if variables.charDead == True:
                self.setVisible(True)
                variables.x = 370
                variables.y = 552
                variables.charDead = False
                variables.Frozen = [False, False, False, False]
                variables.Collected = [False, False, False, False]
                variables.currPos = [[0, 0], [0, 0], [0, 0], [0, 0]]
                variables.currentPositionEnemy = [random.randrange(100, 700, 10), random.randrange(100, 500, 10)],\
                                                 [random.randrange(100, 700, 10), random.randrange(100, 500, 10)],\
                                                 [random.randrange(100, 700, 10), random.randrange(100, 500, 10)],\
                                                 [random.randrange(100, 700, 10), random.randrange(100, 500, 10)]

                variables.aliveEnemy = 4
                variables.deadEnemy = 0
                variables.collectedEnemy = 0
                self.dontJump = True

            self.setGeometry(variables.currentPositionEnemy[self.koji][0],
                                 variables.currentPositionEnemy[self.koji][1], 50, 50)

            if variables.collectedEnemy == 4:
                self.setVisible(True)
                variables.x = 370
                variables.y = 552
                variables.charDead = False
                variables.Frozen = [False, False, False, False]
                variables.Collected = [False, False, False, False]
                variables.currPos = [[0, 0], [0, 0], [0, 0], [0, 0]]
                variables.currentPositionEnemy = [random.randrange(100, 700, 10), random.randrange(100, 500, 10)],\
                                                 [random.randrange(100, 700, 10), random.randrange(100, 500, 10)], \
                                                 [random.randrange(100, 700, 10), random.randrange(100, 500, 10)], \
                                                 [random.randrange(100, 700, 10), random.randrange(100, 500, 10)]
                variables.aliveEnemy = 4
                variables.deadEnemy = 0
                variables.collectedEnemy = 0
                variables.increaseLevel = True
                self.dontJump = True

        elif variables.gameMultiLive == True and self.kojiBroj == 1:
            if variables.lives == 0 and variables.lives2 == 0:
                variables.gameOver = True
#1
            if ((variables.currPos[self.koji][0] - 50 < variables.x and variables.currPos[self.koji][0] + 50 > variables.x) and
                (variables.currPos[self.koji][1] - 50 < variables.y and variables.currPos[self.koji][1] + 50 > variables.y) and
                 variables.Collected[self.koji] == False):
                variables.Collected[self.koji] = True
                variables.collectedEnemy += 1
                variables.points += 1
#2
            if ((variables.currPos[self.koji][0] - 50 < variables.x2 and variables.currPos[self.koji][0] + 50 > variables.x2) and
                (variables.currPos[self.koji][1] - 50 < variables.y2 and variables.currPos[self.koji][1] + 50 > variables.y2) and
                 variables.Collected[self.koji] == False):
                variables.Collected[self.koji] = True
                variables.collectedEnemy += 1
                variables.points2 += 1

            if variables.Frozen[self.koji] == True:
                self.pix1 = QPixmap('Pictures/dead_enemy.png')
                self.setPixmap(self.pix1.scaled(30, 30))
            else:
                self.pix1 = QPixmap('Pictures/enemy_black.png')
                self.setPixmap(self.pix1.scaled(50, 50))
                self.setVisible(True)

            self.position = self.geometry()

            if variables.Collected[self.koji] == True:
                self.setVisible(False)
#1
            if variables.isShot == True and variables.bulletused == False and variables.Frozen[self.koji] == False :
                if(self.position.x() < variables.bulletX and self.position.x() + 50 > variables.bulletX) and (self.position.y() - 50 < variables.bulletY and self.position.y() + 50 > variables.bulletY):
                    self.isHit = True
                    variables.aliveEnemy -= 1
                    variables.deadEnemy += 1
                    variables.Frozen[self.koji] = True
                    variables.currPos[self.koji][0] = self.position.x()
                    variables.currPos[self.koji][1] = self.position.y()
                    variables.bulletused = True
                    variables.points += 1
#2
            if variables.isShot2 == True and variables.bulletused2 == False and variables.Frozen[self.koji] == False :
                if(self.position.x() < variables.bullet2X and self.position.x() + 50 > variables.bullet2X) and \
                        (self.position.y() - 50 < variables.bullet2Y and self.position.y() + 50 > variables.bullet2Y):
                    self.isHit = True
                    variables.aliveEnemy -= 1
                    variables.deadEnemy += 1
                    variables.Frozen[self.koji] = True
                    variables.currPos[self.koji][0] = self.position.x()
                    variables.currPos[self.koji][1] = self.position.y()
                    variables.bulletused2 = True
                    variables.points2 += 1
#1
            if variables.Frozen[self.koji] == False:
                if(self.position.x() - 50 < variables.x and self.position.x() + 50 > variables.x ) and (self.position.y() - 50 < variables.y and self.position.y() + 50 > variables.y) and variables.charDead == False:
                    variables.charDead = True
                    variables.takeLife = True
                    print(variables.lives)
#2
            if variables.Frozen[self.koji] == False:
                if(self.position.x() - 50 < variables.x2 and self.position.x() + 50 > variables.x2 ) and (self.position.y() - 50 < variables.y2 and self.position.y() + 50 > variables.y2) and variables.charDead2 == False:
                    variables.charDead2 = True
                    variables.takeLife2 = True
                    print(variables.lives2)

            self.whereToGo()

            if variables.charDead == True and variables.charDead2 == True:
                self.setVisible(True)
                variables.x = 370
                variables.y = 552
                variables.x2 = 540
                variables.y2 = 552
                if variables.lives != 0:
                    variables.charDead = False
                if variables.lives2 != 0:
                    variables.charDead2 = False
                variables.Frozen = [False, False, False, False]
                variables.Collected = [False, False, False, False]
                variables.currPos = [[0, 0], [0, 0], [0, 0], [0, 0]]
                variables.currentPositionEnemy = [random.randrange(100, 700, 10), random.randrange(100, 500, 10)],\
                                                 [random.randrange(100, 700, 10), random.randrange(100, 500, 10)],\
                                                 [random.randrange(100, 700, 10), random.randrange(100, 500, 10)],\
                                                 [random.randrange(100, 700, 10), random.randrange(100, 500, 10)]

                variables.aliveEnemy = 4
                variables.deadEnemy = 0
                variables.collectedEnemy = 0
                self.dontJump = True

            self.setGeometry(variables.currentPositionEnemy[self.koji][0],
                             variables.currentPositionEnemy[self.koji][1], 50, 50)

            if variables.collectedEnemy == 4:
                self.setVisible(True)
                variables.x = 370
                variables.y = 552
                variables.x = 540
                variables.y = 552
                if variables.lives != 0:
                    variables.charDead = False
                if variables.lives2 != 0:
                    variables.charDead2 = False
                variables.Frozen = [False, False, False, False]
                variables.Collected = [False, False, False, False]
                variables.currPos = [[0, 0], [0, 0], [0, 0], [0, 0]]
                variables.currentPositionEnemy = [random.randrange(100, 700, 10), random.randrange(100, 500, 10)],\
                                                 [random.randrange(100, 700, 10), random.randrange(100, 500, 10)], \
                                                 [random.randrange(100, 700, 10), random.randrange(100, 500, 10)], \
                                                 [random.randrange(100, 700, 10), random.randrange(100, 500, 10)]
                variables.aliveEnemy = 4
                variables.deadEnemy = 0
                variables.collectedEnemy = 0
                variables.increaseLevel = True
                self.dontJump = True

    def whereToGo2(self):
        if variables.Frozen[self.koji] == False:
            if (variables.x - 5 < variables.currentPositionEnemy[self.koji][0] and variables.x + 5 >variables.currentPositionEnemy[self.koji][0]):
                    variables.currentPositionEnemy[self.koji][0] = variables.x + variables.level / 2
            else:
                if(variables.x > variables.currentPositionEnemy[self.koji][0]):
                    self.setPixmap(self.pix1.scaled(50, 50).transformed((QTransform().scale(-1, 1))))
                    variables.currentPositionEnemy[self.koji][0] += 2 + variables.level / 2
                else:
                    self.setPixmap(self.pix1.scaled(50, 50))
                    variables.currentPositionEnemy[self.koji][0] -= 2 + variables.level / 2
            if (variables.y - 5 < variables.currentPositionEnemy[self.koji][1] and variables.y + 5 > variables.currentPositionEnemy[self.koji][1]):
                variables.currentPositionEnemy[self.koji][1] = variables.y
            else:
                if(variables.y > variables.currentPositionEnemy[self.koji][1]):
                    variables.currentPositionEnemy[self.koji][1] += 1 + variables.level / 2
                else:
                    variables.currentPositionEnemy[self.koji][1] -= 1 + variables.level / 2

    def whereToGo(self):
        if variables.Frozen[self.koji] == False:
            daljeOdCharX = abs(variables.x - variables.currentPositionEnemy[self.koji][0])
            daljeOdCharY = abs(variables.y - variables.currentPositionEnemy[self.koji][1])

            daljeOdChar2X = abs(variables.x2 - variables.currentPositionEnemy[self.koji][0])
            daljeOdChar2Y = abs(variables.y2 - variables.currentPositionEnemy[self.koji][1])

            temp1 = math.sqrt(math.pow(daljeOdCharX, 2) + math.pow(daljeOdCharY, 2))
            temp2 = math.sqrt(math.pow(daljeOdChar2X, 2) + math.pow(daljeOdChar2Y, 2))

            if (temp1 > temp2 and variables.charDead2 == False) or variables.charDead == True:
                if (variables.x2 - 5 < variables.currentPositionEnemy[self.koji][0] and variables.x2 + 5 > variables.currentPositionEnemy[self.koji][0]):
                    variables.currentPositionEnemy[self.koji][0] = variables.x2
                else:
                    if (variables.x2 > variables.currentPositionEnemy[self.koji][0]):
                        self.setPixmap(self.pix1.scaled(50, 50).transformed((QTransform().scale(-1, 1))))
                        variables.currentPositionEnemy[self.koji][0] += 4 + variables.level / 2
                    else:
                        self.setPixmap(self.pix1.scaled(50, 50))
                        variables.currentPositionEnemy[self.koji][0] -= 4 + variables.level / 2
                if (variables.y2 - 5 < variables.currentPositionEnemy[self.koji][1] and variables.y2 + 5 > variables.currentPositionEnemy[self.koji][1]):
                    variables.currentPositionEnemy[self.koji][1] = variables.y2
                else:
                    if (variables.y2 > variables.currentPositionEnemy[self.koji][1]):
                        variables.currentPositionEnemy[self.koji][1] += 3 + variables.level / 2
                    else:
                        variables.currentPositionEnemy[self.koji][1] -= 3 + variables.level / 2
            else:
                if (variables.x - 5 < variables.currentPositionEnemy[self.koji][0] and variables.x + 5 > variables.currentPositionEnemy[self.koji][0]):
                    variables.currentPositionEnemy[self.koji][0] = variables.x
                else:
                    if (variables.x > variables.currentPositionEnemy[self.koji][0]):
                        self.setPixmap(self.pix1.scaled(50, 50).transformed((QTransform().scale(-1, 1))))
                        variables.currentPositionEnemy[self.koji][0] += 4 + variables.level / 2
                    else:
                        self.setPixmap(self.pix1.scaled(50, 50))
                        variables.currentPositionEnemy[self.koji][0] -= 4 + variables.level / 2
                if (variables.y - 5 < variables.currentPositionEnemy[self.koji][1] and variables.y + 5 > variables.currentPositionEnemy[self.koji][1]):
                    variables.currentPositionEnemy[self.koji][1] = variables.y
                else:
                    if (variables.y > variables.currentPositionEnemy[self.koji][1]):
                        variables.currentPositionEnemy[self.koji][1] += 3 + variables.level / 2
                    else:
                        variables.currentPositionEnemy[self.koji][1] -= 3 + variables.level / 2
