import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QGraphicsView, QPushButton
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication, Qt, QBasicTimer
from threading import Thread
from time import sleep


class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.initWindow()
        self.setBackground()
        self.initCharacter()
        self.moveSize = 10
        self.jumpSize = 10
        #button1 = QPushButton('1 Player', self)
        #button1.setGeometry(0,0,70,27)
        #button1.clicked.connect(self.onePlayerGameMode)

        #button2 = QPushButton('2 Player', self)
        #button2.setGeometry(70,0,70,27)
        #button2.clicked.connect(self.twoPlayerGameMode)

        #button3 = QPushButton('Tournament', self)
        #button3.setGeometry(140,0,70,27)
       # button3.clicked.connect(self.tournamentGameMode)
        self.show()

    def onePlayerGameMode(self):
        print('1 Player')
    def twoPlayerGameMode(self):
        print('2 Player')
    def tournamentGameMode(self):
        print('Tournament')

    def initWindow(self):
        self.windowWidth = int(800)
        self.windowHeight = int(620)
        self.setFixedSize(self.windowWidth, self.windowHeight)
        self.setWindowTitle("Bubble Bobble")
        self.setWindowIcon(QIcon('bbobble.png'))

    def setBackground(self):
        self.bacground = QLabel(self)
        self.bacground.setStyleSheet("background-image: url(bckgrnd.jpg)")
        self.bacground.resize(self.windowWidth, self.windowHeight - 20)

    def initCharacter(self):
        self.side = 'r'
        self.characterWidth = int(60)
        self.characterHeight = int(50)
        self.character = QLabel(self)
        self.characterX = int(self.windowWidth / 2) - int(self.characterWidth / 2)
        self.characterY = int(self.windowHeight - 110)
        self.character.setStyleSheet("image: url(bbobble.png)")
        self.character.resize(self.characterWidth, self.characterHeight)
        self.character.move(self.characterX, self.characterY)
        self.ableToFire = True

    def canMoveLeft(self) -> bool:
        canMove = True

        if self.characterX - self.moveSize <=30:
            canMove = False
        return canMove

    def canMoveRight(self) -> bool:
        canMove = True

        if self.characterX + self.moveSize >= self.windowWidth-30 - self.characterWidth:
            canMove = False
        return canMove

    def canMoveUp(self) -> bool:
        canMove = True

        if self.characterY - self.moveSize <= 20:
            canMove = False
        return canMove

    def canMoveDown(self) -> bool:
        canMove = True

        if self.characterY + self.moveSize >= self.windowHeight-20 - self.characterHeight:
            canMove = False
        return canMove

    def initBubble(self):
        self.bubble = QLabel(self)
        self.bubble.setStyleSheet("image: url(circle31.png)")
        self.bubble.resize(25, 25)
        self.bubbleY = self.characterY + 7
        if (self.side == 'r'):
            self.bubbleX = self.characterX + self.characterWidth / 2 + 9
        else:
            self.bubbleX = self.characterX - 1

        self.bubble.move(self.bubbleX, self.bubbleY)
        self.Fiering = False
        self.bubble.show()

    def fire(self, b, x, y, s):
        while True:
            if s == 'r':
                x = x + 5
            else:
                x = x - 5
            b.move(x, y)
            if (x <= 40 or x >= self.windowWidth-67):
                b.resize(0, 0)
                b = None
                self.ableToFire = True
                break
            sleep(0.02)
    def keyPressEvent(self, e):
        key = e.key()
        if (key == Qt.Key_Left and self.canMoveLeft() or key==Qt.Key_A and self.canMoveLeft()):
            self.Moving = True
            self.characterX -= self.moveSize
            self.character.move(self.characterX, self.characterY)
            self.character.setStyleSheet("image: url(bbobble_left.png)")
            self.side = 'l'

        elif (key == Qt.Key_Right and self.canMoveRight()  or key==Qt.Key_D and self.canMoveRight()):
            self.Moving = True
            self.characterX += self.moveSize
            self.character.move(self.characterX, self.characterY)
            self.character.setStyleSheet("image: url(bbobble.png)")
            self.side = 'r'

        elif (key == Qt.Key_Up and self.canMoveUp() or key==Qt.Key_W and self.canMoveUp()):
            self.characterY -= self.jumpSize
            self.character.move(self.characterX, self.characterY)

        elif (key == Qt.Key_Down and self.canMoveDown() or key==Qt.Key_S and self.canMoveDown()):
            self.characterY += self.jumpSize
            self.character.move(self.characterX, self.characterY)

        elif (key == Qt.Key_Space):
            try:
                if self.ableToFire:
                    self.Fiering = True
                    self.ableToFire = False
                    self.fireSide = self.side
                    self.initBubble()
                    thread = Thread(target=self.fire, args=[self.bubble, self.bubbleX, self.bubbleY, self.fireSide], daemon=True)
                    thread.start()
            except:
                self.Fiering = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = Example()
    example.show()
    sys.exit(app.exec_())
