import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QGraphicsView
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication, Qt, QBasicTimer
from threading import Thread

class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()


    def initUI(self):
        self.initWindow()
        self.setBackground()
        self.initCharacter()
        self.moveSize=10
        self.jumpSize=10
        self.show()

    def initWindow(self):
        self.windowWidth = int(950)
        self.windowHeight = int(550)
        self.setFixedSize(self.windowWidth, self.windowHeight)
        self.setWindowTitle("Bubble Bobble")
        self.setWindowIcon(QIcon('bbobble.png'))

    def setBackground(self):
        self.bacground = QLabel(self)
        self.bacground.setStyleSheet("background-image: url(bckgrnd.jpg)")
        self.bacground.resize(self.windowWidth, self.windowHeight - 20)

    def initCharacter(self):
        self.side = 'r'
        self.characterWidth=int(45)
        self.characterHeight= int(40)
        self.character=QLabel(self)
        self.characterX=int(self.windowWidth/2)-int(self.characterWidth/2)
        self.characterY=int(self.windowHeight-110)
        self.character.setStyleSheet("image: url(bbobble.png)")
        self.character.resize(self.characterWidth,self.characterHeight)
        self.character.move(self.characterX,self.characterY)

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

    def initBubble(self):
        self.bubble = QLabel(self)
        self.bubble.setStyleSheet("image: url(bubble.jpg)")
        self.bubble.resize(10,10)
        self.bubbleX = int(self.characterX + self.characterWidth/3 - 1)
        self.bubbleY = int(self.characterY - 10 + 4)
        self.bubble.move(self.bubbleX,self.bubbleY)
        self.bubble.show()


    # def fire(self, b, x, y):
    #     while True:
    #         if self.side == 'r':
    #             x = x + 20
    #             b.move(x, y)
    #             if x >= self.windowWidth - self.b:
    #                 b.resize(0,0)
    #                 b = None
    #
    #     sleep(0.05)

    def keyPressEvent(self, e):
        key = e.key()
        if(key == Qt.Key_Left and self.canMoveLeft()):
            self.characterX -= self.moveSize
            self.character.move(self.characterX, self.characterY)
            self.character.setStyleSheet("image: url(bbobble_left.png)")
            self.side='l'

        elif(key == Qt.Key_Right and self.canMoveRight()):
            self.characterX += self.moveSize
            self.character.move(self.characterX, self.characterY)
            self.character.setStyleSheet("image: url(bbobble.png)")
            self.side='r'

        elif(key == Qt.Key_Up):
            self.characterY -= self.jumpSize
            self.character.move(self.characterX, self.characterY)
            
        elif (key == Qt.Key_Down):
            self.characterY += self.jumpSize
            self.character.move(self.characterX, self.characterY)

        # if(key == Qt.Key_Space):
        #     thread = Thread(target=self.fire, args=[self.bubble, self.bubbleX, self.bubbleY])
        #     thread.daemon = True
        #     thread.start()
        #     self.initBubble()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = Example()
    example.show()
    sys.exit(app.exec_())
