from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QDesktopWidget
import threading
import variables
import time

class GameOver(QWidget):

    def __init__(self, sw):
        super().__init__()
        self.sw = sw
        self.init()

    def init(self):
        self.setFixedSize(820, 600)

        layout = QVBoxLayout()

        self.setStyleSheet("background-image : url(Pictures/go.jpg)")

        self.btn = QPushButton(self)

        layout.addWidget(self.btn)

        self.setLayout(layout)
        self.btn.clicked.connect(self.returnToMenu)
        self.btn.setFixedSize(820, 600)
        self.setLayout(layout)

        thread = threading.Thread(target=self.endGame)
        thread.start()

    def endGame(self):
        while True:
            if variables.gameOver == True:
                self.sw.setCurrentIndex(3)
                variables.gameOver = False
                variables.gameLive = False
                variables.gameMultiLive = False
                variables.charDead2 = False
                variables.charDead = False
                variables.reset = True
            time.sleep(0.3)

    def returnToMenu(self):
        self.sw.setCurrentIndex(0)

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2 - 50)