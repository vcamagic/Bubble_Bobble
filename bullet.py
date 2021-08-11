from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

from bulletstate import BulletSate

class Bullet(QLabel):

    def __init__(self, parent, broj):
        QLabel.__init__(self, parent)
        self.koji = broj
        self.initBullet()
        self.shoot = BulletSate(broj)
        self.shoot.start()

    def initBullet(self):
        self.pix2 = QPixmap('Pictures/circle31.png')
        self.setPixmap(self.pix2.scaled(30, 30))
        self.setStyleSheet("background-image: url()")
        self.setGeometry(200, 820, 30, 30)
        self.setFixedSize(30, 30)
        self.setVisible(False)
