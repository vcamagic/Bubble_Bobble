from PyQt5.QtWidgets import QWidget, QMessageBox,QMainWindow
from PyQt5 import QtCore
from labels import Labels
from character import Charachter
from key_notifier import KeyNotifier
from bullet import Bullet
from enemy import Enemy
from multiprocessing import Queue
global label1
global label2
global labele

import random
import variables
import threading
import time

class Tournament(QWidget):
    def __init__(self, queue: Queue, brojIgraca, name1="Player1", name2="Player2"):
        print('usao u turnir')
        super().__init__()

        self.igrac1 = name1
        self.igrac2 = name2
        self.queue = queue
        self.brojIgraca = brojIgraca



    def inicijalizujSve(self):
        self.label1 = Charachter(self, 0)
        self.label3 = Charachter(self, 1)
        self.label2 = Bullet(self, 0)
        self.label4 = Bullet(self, 1)
        self.enemyLabel1 = Enemy(self, [random.randrange(100, 700, 10), random.randrange(100, 500, 10)], 0, self.label1,
                                 1)
        self.enemyLabel2 = Enemy(self, [random.randrange(100, 700, 10), random.randrange(100, 500, 10)], 1, self.label1,
                                 1)
        self.enemyLabel3 = Enemy(self, [random.randrange(100, 700, 10), random.randrange(100, 500, 10)], 2, self.label1,
                                 1)
        self.enemyLabel4 = Enemy(self, [random.randrange(100, 700, 10), random.randrange(100, 500, 10)], 3, self.label1,
                                 1)
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)

        self.key_notifier = KeyNotifier()
        self.key_notifier.key_signal.connect(self.label1.__update_position__)
        self.key_notifier.key_signal.connect(self.label3.__update_position__)
        self.key_notifier.start()

        self.label1.setStyleSheet("background-image: url()")
        self.label3.setStyleSheet("background-image: url()")

        self.setStyleSheet("background-image: url(Pictures/level.jpg)")

        self.label2.char = self.label1
        self.label1.bullet = self.label2

        self.label4.char = self.label3
        self.label3.bullet = self.label4

        self.labele = Labels(self, 1)

        self.show()
        thread = threading.Thread(target=self.points)
        thread.start()
        thread = threading.Thread(target=self.points2)
        thread.start()



    def keyPressEvent(self, event):
        self.key_notifier.add_key(event.key())

    def keyReleaseEvent(self, event):
        self.key_notifier.rem_key(event.key())

    def writeWinner(self):
        f = open('pobednik.txt', 'w+')
        f.write(variables.pobednik)
        f.close()

    def points(self):
        while True:
            if variables.gameMultiLive == True:
                self.labele.changeScore(variables.points)
                if variables.reset == True:
                    self.labele.resetAll2()
                    variables.reset = False
                    variables.points = 0
                if variables.takeLife:
                    self.labele.changeLives()
                    variables.takeLife = False
                    if (variables.lives == 0 and variables.lives2 != 0):
                        variables.pobednik = self.igrac2
                        self.writeWinner()
                        variables.gameOver = True
                        #self.pobednik = self.igrac2
                        #self.krajText = self.igrac1 + 'died. :(\n'
                        #self.krajText += self.igrac2 + 'won! :)\n'
                        #self.__GameOver()
                    variables.lives -= 1
                if variables.increaseLevel:
                    self.labele.changeLevel()
                    variables.increaseLevel = False
                    variables.level += 1
                    self.__init__(self.queue, self.igrac1,self.igrac2)
            time.sleep(0.3)

    def points2(self):
        while True:
            if variables.gameMultiLive == True:
                self.labele.changeScore2(variables.points2)
                if variables.takeLife2:
                    self.labele.changeLives2()
                    if (variables.lives != 0 and variables.lives2 == 0):
                        variables.pobednik  = self.igrac1
                        self.writeWinner()
                        variables.gameOver = True
                        #self.pobednik = self.igrac1
                        #self.krajText = self.igrac2 + 'died. :(\n'
                        #self.krajText += self.igrac1 + 'won! :)\n'
                        #self.__GameOver()
                    variables.takeLife2 = False
                    variables.lives2 -= 1
            time.sleep(0.3)




