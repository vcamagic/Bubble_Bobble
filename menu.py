import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel, QWidget, QPushButton, QApplication
import main

class Menu(QWidget):

    def __init__(self):
        super(Menu,self).__init__()
        self.initUI()

    def initUI(self):
        self.initWindow()
        self.setBackground()
        self.meni()
        self.show()

    def initWindow(self):
        self.windowWidth = int(800)
        self.windowHeight = int(620)
        self.setFixedSize(self.windowWidth, self.windowHeight)
        self.setWindowTitle("Bubble Bobble")
        self.setWindowIcon(QIcon('bbobble.png'))

    def setBackground(self):
        self.bacground = QLabel(self)
        self.bacground.setStyleSheet("background-image: url(menu_bcgrdn.jpg)")
        self.bacground.resize(self.windowWidth,self.windowHeight - 20)
        self.bacground.show()

    def meni(self):
        self.button1 = QPushButton(self)
        self.button1.setGeometry(50,200,300,50)
        self.button1.setText('Singleplayer')
        self.button1.clicked.connect(self.spPlay)
        self.button1.show()

        self.button2 = QPushButton(self)
        self.button2.setGeometry(50, 250, 300, 50)
        self.button2.setText('Multiplayer')
        self.button2.clicked.connect(self.mpPlay)
        self.button2.show()

        self.button3 = QPushButton(self)
        self.button3.setGeometry(50, 300, 300, 50)
        self.button3.setText('Settings')
        self.button3.clicked.connect(self.settings)
        self.button3.show()

        self.button4 = QPushButton(self)
        self.button4.setGeometry(50, 350, 300, 50)
        self.button4.setText('Exit')
        self.button4.clicked.connect(self.exit)
        self.button4.show()

    def spPlay(self):
        self.close()
        self.open = main.Example()
        self.open.show()

    def mpPlay(self):
        self.close()

    def settings(self):
        self.close()

    def exit(self):
        self.close()

if __name__ == "__main__":
    app= QApplication(sys.argv)
    menu = Menu()
    sys.exit(app.exec_())
