import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QGraphicsView, QPushButton, QAction, qApp, \
    QStackedWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap, QTransform, QPainter, QImage
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication, Qt, QBasicTimer, QSize
from threading import Thread
from time import sleep

#top left x1,y1 bottom right x2,y2
#Blockss = [
    #[51, 593, 750, 620],
    #[125, 480, 674, 508],
   # [201, 368, 599, 394],
   # [276, 256, 524, 282]
#]

#y, x1, x2
Blocks = [
    [552, 51, 750],
    [442, 70, 649],
    [332, 160, 574],
    [218, 235, 499]
]

class Example(QMainWindow):
    EXIT_CODE_REBOOT = -2
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def checkPosition(self):
        self.xy = [self.characterX, self.characterY]
        for platform in Blocks:
            if (self.xy[1] == platform[0] and self.xy[0] > platform[1] and self.xy[0] < platform[2]):
                self.onPlatform = True
                self.charFalling = False
                break
            else:
                self.onPlatform = False
                self.charFalling = True

    def initUI(self):
        self.initWindow()
        self.setBackground()
        self.initCharacter()
        self.moveSize = 25
        self.jumpSize = 5  # 100
        self.gravityThread = Thread(target=self.checkPosition, daemon=True)
        self.show()

    def initWindow(self):
        self.windowWidth = int(800)
        self.windowHeight = int(620)
        self.setFixedSize(self.windowWidth, self.windowHeight)
        self.setWindowTitle("Bubble Bobble")
        self.setWindowIcon(QIcon('bbobble.png'))

    def setBackground(self):
        self.bacground = QLabel(self)
        self.bacground.setStyleSheet("background-image: url(level.jpg)")
        self.bacground.resize(self.windowWidth, self.windowHeight)

    def initCharacter(self):
        self.side = 'r'
        self.characterWidth = int(60)
        self.characterHeight = int(50)
        self.character = QLabel(self)
        self.characterX = int(self.windowWidth / 2) - int(self.characterWidth / 2)
        self.characterY = int(self.windowHeight - 18 - self.characterHeight)
        self.charFalling = False
        self.character.setStyleSheet("image: url(bbobble.png)")
        self.character.resize(self.characterWidth, self.characterHeight)
        self.character.move(self.characterX, self.characterY)

        self.ableToFire = True
        self.Jumping = False

    def canMoveLeft(self) -> bool:
        canMove = True

        if self.characterX - self.moveSize <= 45:
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

        if self.characterY + self.moveSize >= self.windowHeight- 10 - self.characterHeight:
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


#[552, 51, 750],
#[442, 70, 649],
#[332, 160, 574],
#[218, 235, 499]

    def fix(self):
        if self.characterX >= 70 and self.characterX <= 649 and self.characterY > 332:
            self.characterY = 442
            self.character.move(self.characterX, self.characterY)
        elif self.characterX >= 160 and self.characterX <= 574 and self.characterY > 218:
            self.characterY = 332
            self.character.move(self.characterX, self.characterY)
        elif self.characterX >= 235 and self.characterX <= 499 and self.characterY <= 218:
            self.characterY = 218
            self.character.move(self.characterX, self.characterY)
        else:
           # self.characterY = 442
           # self.character.move(self.characterX, self.characterY)
                self.characterY = 552
                self.character.move(self.characterX, self.characterY)

    def stayPlatform(self, y):
        self.Jumping = True
        cnt = 0
        # while self.characterY >= y-self.jumpSize-self.characterHeight-60:
        while cnt <= 100 + self.characterHeight / 5:
            cnt += self.jumpSize
            self.characterY -= self.jumpSize
            self.character.move(self.characterX, self.characterY)
            sleep(0.01)
        # if ( self.characterX >= 70 and self.characterX <= 160 and self.characterY==442) or (self.characterX >= 574 and self.characterX <= 649 and self.characterY==442 ) or (self.characterX >= 160 and self.characterX <= 235 and self.characterY==332) or (self.characterX >= 499 and self.characterX <= 574 and self.characterY==332):
        self.characterY= y
        self.character.move(self.characterX,self.characterY)
        self.Jumping = False

    def jump(self, y):
        self.Jumping = True
        cnt = 0
        #while self.characterY >= y-self.jumpSize-self.characterHeight-60:
        while cnt <= 100 + self.characterHeight/5:
            cnt += self.jumpSize
            self.characterY -= self.jumpSize
            self.character.move(self.characterX, self.characterY)
            sleep(0.01)
        #if ( self.characterX >= 70 and self.characterX <= 160 and self.characterY==442) or (self.characterX >= 574 and self.characterX <= 649 and self.characterY==442 ) or (self.characterX >= 160 and self.characterX <= 235 and self.characterY==332) or (self.characterX >= 499 and self.characterX <= 574 and self.characterY==332):
        self.fix()
        self.Jumping = False

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
            self.side = 'l'
            self.checkPosition()
            if self.onPlatform:
                self.character.move(self.characterX, self.characterY)
                self.character.setStyleSheet("image: url(bbobble_left.png)")
            elif self.charFalling:
                self.character.move(self.characterX, self.characterY)
                while self.charFalling:
                    self.characterY += 1
                    self.character.move(self.characterX, self.characterY)
                    #sleep(0.001)
                    self.checkPosition()
            self.Moving = False

        elif (key == Qt.Key_Right and self.canMoveRight()  or key==Qt.Key_D and self.canMoveRight()):
            self.Moving = True
            self.characterX += self.moveSize
            self.side = 'r'
            self.checkPosition()
            if self.onPlatform:
                self.character.move(self.characterX, self.characterY)
                self.character.setStyleSheet("image: url(bbobble.png)")
            elif self.charFalling:
                self.character.move(self.characterX, self.characterY)
                while self.charFalling:
                    self.characterY += 1
                    self.character.move(self.characterX, self.characterY)
                    #sleep(0.001)
                    self.checkPosition()
            self.Moving = False

        elif (key == Qt.Key_Up and self.canMoveUp() and not self.Jumping or key==Qt.Key_W and self.canMoveUp()):
            if ( self.characterX >= 70 and self.characterX <= 160 and self.characterY== 442) or (self.characterX >= 574 and self.characterX <= 649 and self.characterY== 442 ) or (self.characterX >= 160 and self.characterX <= 235 and self.characterY== 332) or (self.characterX >= 499 and self.characterX <= 574 and self.characterY== 332):
                threadStayOnPlatform = Thread(target=self.stayPlatform, args=[self.characterY], daemon=True)
                threadStayOnPlatform.start()
            else:
                threadJump = Thread(target=self.jump, args=[self.characterY], daemon=True)
                threadJump.start()
           # self.characterY -= self.jumpSize
            #self.character.move(self.characterX, self.characterY)

        elif (key == Qt.Key_Down and self.canMoveDown() or key==Qt.Key_S and self.canMoveDown()):
            self.characterY += self.moveSize
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


    def newGame(self):
        qApp.exit(self.EXIT_CODE_REBOOT)

    def initScore(self):

        self.life = QLabel(self)
        self.life.resize(30,30)
        self.life.setStyleSheet("image: url(heart.png)")
        self.life.show()
