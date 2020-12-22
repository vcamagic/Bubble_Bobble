import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QGraphicsView
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
        self.show()

    def initWindow(self):
        self.windowWidth = int(500)
        self.windowHeight = int(350)
        self.setFixedSize(self.windowWidth, self.windowHeight)
        self.setWindowTitle("Bubble Bobble")
        self.setWindowIcon(QIcon('bbobble.png'))

    def setBackground(self):
        self.bacground = QLabel(self)
        self.bacground.setStyleSheet("background-image: url(bckgrnd.jpg)")
        self.bacground.resize(self.windowWidth, self.windowHeight - 20)

    def initCharacter(self):
        self.side = 'r'
        self.characterWidth = int(45)
        self.characterHeight = int(40)
        self.character = QLabel(self)
        self.characterX = int(self.windowWidth / 2) - int(self.characterWidth / 2)
        self.characterY = int(self.windowHeight - 110)
        self.character.setStyleSheet("image: url(bbobble.png)")
        self.character.resize(self.characterWidth, self.characterHeight)
        self.character.move(self.characterX, self.characterY)
        self.ableToFire = True

    def canMoveLeft(self) -> bool:
        canMove = True

        if self.characterX - self.moveSize <= 0:
            canMove = False
        return canMove

    def canMoveRight(self) -> bool:
        canMove = True

        if self.characterX + self.moveSize >= self.windowWidth - self.characterWidth:
            canMove = False
        return canMove

    def canMoveUp(self) -> bool:
        canMove = True

        if self.characterY - self.moveSize <= 0:
            canMove = False
        return canMove

    def canMoveDown(self) -> bool:
        canMove = True

        if self.characterY + self.moveSize >= self.windowHeight - self.characterHeight:
            canMove = False
        return canMove

    def initBubble(self):
        self.bubble = QLabel(self)
        self.bubble.setStyleSheet("image: url(circle31.png)")
        self.bubble.resize(10, 10)
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
            if (x <= 0 or x >= self.windowWidth):
                b.resize(0, 0)
                b = None
                self.ableToFire = True
                break
            sleep(0.02)

    def keyPressEvent(self, e):
        key = e.key()
        if (key == Qt.Key_Left and self.canMoveLeft()):
            self.Moving = True
            self.characterX -= self.moveSize
            self.character.move(self.characterX, self.characterY)
            self.character.setStyleSheet("image: url(bbobble_left.png)")
            self.side = 'l'

        elif (key == Qt.Key_Right and self.canMoveRight()):
            self.Moving = True
            self.characterX += self.moveSize
            self.character.move(self.characterX, self.characterY)
            self.character.setStyleSheet("image: url(bbobble.png)")
            self.side = 'r'

        elif (key == Qt.Key_Up and self.canMoveUp()):
            self.characterY -= self.jumpSize
            self.character.move(self.characterX, self.characterY)

        elif (key == Qt.Key_Down and self.canMoveDown()):
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
