from threading import Thread

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QMessageBox, QVBoxLayout

from Tournament import Tournament
from TournamentSrednja import start_tournament


class TournamentWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window")
        layout.addWidget(self.label)
        self.setFixedSize(800, 620)
        self.setWindowTitle("Tournament")
        self.setLayout(layout)
        self.winner = None
        self.initUI()


    def initUI(self):
        self.initWindow()
        self.imeIgraca()
        self.labels()
        self.buttonPlay()
        self.show()


    def initWindow(self):
        self.BackGround = QPixmap("Pictures/prijavaZaTurnir.png")
        self.BackGroundLabel = QtWidgets.QLabel(self)
        self.BackGroundLabel.setPixmap(self.BackGround)
        self.BackGroundLabel.setGeometry(0, 0, 500, 500)

    def imeIgraca(self):
        self.labela2T = QtWidgets.QLabel(self)
        self.labela2T.setText("Enter name")
        self.labela2T.setGeometry(250, 30, 200, 60)
        self.labela2T.setStyleSheet(" color: rgb(0, 0, 0);font-size: 26px; font-family: Playbill;")

        self.imePvogIgraca = QLineEdit(self)
        self.imePvogIgraca.setGeometry(200, 100, 200, 40)
        self.imeDrugogIgraca = QLineEdit(self)
        self.imeDrugogIgraca.setGeometry(200, 200, 200, 40)
        self.imeTrecegIgraca = QLineEdit(self)
        self.imeTrecegIgraca.setGeometry(200, 300, 200, 40)
        self.imeCetvrtogIgraca = QLineEdit(self)
        self.imeCetvrtogIgraca.setGeometry(200, 400, 200, 40)



    def labels(self):
        self.labela3T = QtWidgets.QLabel(self)
        self.labela3T.setText("First player")
        self.labela3T.setGeometry(50, 100, 200, 40)
        self.labela3T.setStyleSheet("color: rgb(0, 0, 0); font-size: 26px; font-family: Playbill;")

        self.labela4T = QtWidgets.QLabel(self)
        self.labela4T.setText("Second player")
        self.labela4T.setGeometry(50, 200, 200, 40)
        self.labela4T.setStyleSheet("color: rgb(0, 0, 0);font-size: 26px; font-family: Playbill;")

        self.labela5T = QtWidgets.QLabel(self)
        self.labela5T.setText("Third player")
        self.labela5T.setGeometry(50, 300, 200, 40)
        self.labela5T.setStyleSheet(" color: rgb(0, 0, 0);font-size: 26px; font-family: Playbill;")

        self.labela6T = QtWidgets.QLabel(self)
        self.labela6T.setText("Fourth player")
        self.labela6T.setGeometry(50, 400, 200, 40)
        self.labela6T.setStyleSheet("color: rgb(0, 0, 0);font-size: 26px; font-family: Playbill;")

    def buttonPlay(self):
        self.playButton = QtWidgets.QPushButton(self)
        self.playButton.setText("PLAY")
        self.playButton.setGeometry(200, 450, 200, 40)
        self.playButton.setStyleSheet("border:2px solid rgb(64, 39, 36); color: rgb(0, 0, 0); font-size: 26px; font-family: Playbill;")
        self.playButton.clicked.connect(self.onPlayButtonClicked)

    def onPlayButtonClicked(self):
        if self.imePvogIgraca.text() == "" or self.imeDrugogIgraca.text() == "" or self.imeTrecegIgraca.text() == "" or self.imeCetvrtogIgraca.text() == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.NoIcon)
            msg.setText("Enter your username")
            msg.setWindowTitle("Error")
            msg.exec_()

        elif self.imePvogIgraca.text() == self.imeDrugogIgraca.text() \
                or self.imePvogIgraca.text() == self.imeTrecegIgraca.text() \
                or self.imePvogIgraca.text() == self.imeCetvrtogIgraca.text() \
                or self.imeDrugogIgraca.text() == self.imeTrecegIgraca.text() \
                or self.imeDrugogIgraca.text() == self.imeCetvrtogIgraca.text() \
                or self.imeTrecegIgraca.text() == self.imeCetvrtogIgraca.text():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.NoIcon)
            msg.setText("Username must be unique")
            msg.setWindowTitle("Error")
            msg.exec_()

        else:
            player1_input = self.imePvogIgraca.text()
            player2_input = self.imeDrugogIgraca.text()
            player3_input = self.imeTrecegIgraca.text()
            player4_input = self.imeCetvrtogIgraca.text()

            #start_tournament(player1_input,player2_input,player3_input,player4_input)
            thread = Thread(target=start_tournament, args=(player1_input, player2_input, player3_input, player4_input))
            thread.daemon = True
            thread.start()
            self.hide()
            self.imePvogIgraca.setText("")
            self.imeDrugogIgraca.setText("")
            self.imeTrecegIgraca.setText("")
            self.imeCetvrtogIgraca.setText("")

