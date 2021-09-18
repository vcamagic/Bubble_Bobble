import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPalette, QBrush
from PyQt5.QtCore import QSize
from PyQt5 import QtCore, QtGui
import sys, random, variables, os
from menu import  UI

class Game(QMainWindow, UI):

    def __init__(self, parent=None):
        super(Game, self).__init__(parent)
        self.init()
        self.initUI()
        self.btn.clicked.connect(self.openSinglePlay)
        self.btn3.clicked.connect(self.exit)


    def exit(self):
        os._exit(0)


    def initUI(self):
        self.setGeometry(0, 0, 800, 620)
        self.setWindowTitle('Bubble Bobble')
        self.setWindowIcon(QIcon('Pictures/bbobble.png'))
        self.setFixedSize(800, 620)
        self.setCentralWidget(self.StackedWidgets)
        UI.center(self)

        self.show()

    def openSinglePlay(self):
        self.StackedWidgets.setCurrentIndex(1)
        variables.lives = 3
        variables.gameLive = True

    def display(self):
        self.stackedWidgets.setCurrentIndex(0)

if __name__=='__main__':
    app = QApplication(sys.argv)
    bubbleBobble = Game()
    sys.exit(app.exec_())
