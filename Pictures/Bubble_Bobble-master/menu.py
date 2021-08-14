import sys, random

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import *
from PyQt5 import  QtCore, QtGui, QtWidgets
import game
from singleplayer import SinglePlayer

class UI(QtWidgets.QWidget):

    def init(self):

        self.StackedWidgets = QStackedWidget()
        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()
        self.stack4 = QWidget()

        self.stack2 = SinglePlayer()
        self.MenuUI()

        self.StackedWidgets.addWidget(self.stack1)
        self.StackedWidgets.addWidget(self.stack2)
        self.StackedWidgets.addWidget(self.stack3)
        self.StackedWidgets.addWidget(self.stack4)

    def MenuUI(self):
        self.stack1.setFixedSize(800, 620)

        layout = QVBoxLayout()

        oImage = QImage('Pictures/menu_bcgrdn.jpg')
        sImage = oImage.scaled(QSize(800, 620))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.btn = QPushButton(self.stack1)
        self.btn1 = QPushButton(self.stack1)
        self.btn2 = QPushButton(self.stack1)
        self.btn3 = QPushButton(self.stack1)

        self.btn.setText("Singleplayer")
        self.btn1.setText("Multiplayer")
        self.btn2.setText("Options")
        self.btn3.setText("Exit")

        self.btn.setFixedSize(200, 80)
        self.btn1.setFixedSize(200, 80)
        self.btn2.setFixedSize(200, 80)
        self.btn3.setFixedSize(200, 80)

        layout.addWidget(self.btn)
        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        layout.addWidget(self.btn3)
        layout.setAlignment(QtCore.Qt.AlignCenter)

        self.stack1.setLayout(layout)


    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2 - 50)
