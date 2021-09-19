from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import sys
import variables
import os

from TournamentWindow import TournamentWindow
from menu import UI

class Game(QMainWindow, UI):

    def __init__(self, parent=None):
        super(Game, self).__init__(parent)
        self.init()
        self.initUI()
        self.btn.clicked.connect(self.openSinglePlay)
        self.btn1.clicked.connect(self.openMultiPlay)
        self.btn2.clicked.connect(self.openTournament)
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

    def openMultiPlay(self):
        self.StackedWidgets.setCurrentIndex(2)
        variables.lives = 3
        variables.lives2 = 3
        variables.gameMultiLive = True

    def openTournament(self):
        self.StackedWidgets.setCurrentIndex(3)
        variables.lives = 3
        variables.lives2 = 3
        variables.gameMultiLive = True
        self.w = TournamentWindow()

    def display(self):
        self.stackedWidgets.setCurrentIndex(0)

if __name__=='__main__':
    app = QApplication(sys.argv)
    bubbleBobble = Game()
    sys.exit(app.exec_())
