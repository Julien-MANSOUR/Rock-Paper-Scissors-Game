#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap,QFont
from PyQt5.QtCore import QTimer
from random import randint
textFont=QFont("Times",16)
buttonFont=QFont("Arial",12)
PlayerScore = 0
ComputerScore = 0
class Window (QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300,300,550,500)
        self.setWindowTitle("mosso")
        self.UI()

    def UI(self):
        ########################Score########################
        self.scoreComputerText=QLabel("Computer Score : ",self)
        self.scoreComputerText.move(30,20)
        self.scoreComputerText.setFont(textFont)
        self.scoreComputerText.setStyleSheet("background-color:red")
        self.scorePlayerText=QLabel("Your Score : ",self)
        self.scorePlayerText.move(330,20)
        self.scorePlayerText.setFont(textFont)
        self.scorePlayerText.setStyleSheet("background-color:blue")
        ########################Image########################
        self.ComputerImage=QLabel(self)
        self.ComputerImage.setPixmap(QPixmap("images/rock.png"))
        self.ComputerImage.move(50,100)

        self.PlayerImage=QLabel(self)
        self.PlayerImage.setPixmap(QPixmap("images/rock.png"))
        self.PlayerImage.move(330,100)

        self.GameImage=QLabel(self)
        self.GameImage.setPixmap(QPixmap("images/game.png"))
        self.GameImage.move(235,160)
        ########################Image########################
        self.StartButton=QPushButton("Start",self)
        self.StartButton.setFont(buttonFont)
        self.StartButton.move(160,300)
        self.StartButton.clicked.connect(self.start)
        self.StopButton=QPushButton("Stop",self)
        self.StopButton.setFont(buttonFont)
        self.StopButton.move(250,300)
        self.StopButton.clicked.connect(self.stop)
        self.RestartButton=QPushButton("Restart",self)
        self.RestartButton.move(340,300)
        self.RestartButton.clicked.connect(self.restart)
        ########################################################
        self.timer=QTimer(self)
        self.timer.setInterval(100)#en ms
        self.timer.timeout.connect(self.PlayGame)
        self.show()

    def restart(self):
        global PlayerScore
        global ComputerScore
        PlayerScore = 0
        ComputerScore = 0
        self.scoreComputerText.setText("Computer Score : {}".format(ComputerScore))
        self.scorePlayerText.setText("Your Score : {}".format(PlayerScore))

    def start(self):
        self.timer.start()

    def PlayGame(self):
        self.randComputerNmb=randint(1,3)#rock,paper,sicors
        self.randPlayerNmb=randint(1,3)
        print(self.randComputerNmb,self.randPlayerNmb)
        if self.randComputerNmb == 1:
            self.ComputerImage.setPixmap(QPixmap("images/rock.png"))
        elif self.randComputerNmb == 2:
            self.ComputerImage.setPixmap(QPixmap("images/paper.png"))
        else:
            self.ComputerImage.setPixmap(QPixmap("images/scissors.png"))


        if self.randPlayerNmb==1:
            self.PlayerImage.setPixmap(QPixmap("images/rock.png"))
        elif self.randPlayerNmb==2:
            self.PlayerImage.setPixmap(QPixmap("images/paper.png"))
        else:
            self.PlayerImage.setPixmap(QPixmap("images/scissors.png"))

    def stop(self):
        global PlayerScore
        global ComputerScore

        self.timer.stop()
        if self.randComputerNmb == self.randPlayerNmb:
            msg=QMessageBox.information(self,"Information","It is a Draw")
        elif self.randComputerNmb == 1 and self.randPlayerNmb == 2:  #rock vs paper
            msg=QMessageBox.information(self,"Information","you Win !")
            PlayerScore += 1
            self.scorePlayerText.setText("Your Score : {}".format(PlayerScore))
            self.scorePlayerText.resize(150,30)
        elif self.randComputerNmb == 1 and self.randPlayerNmb == 3:  #rock vs scissor
            msg=QMessageBox.information(self,"Information","Computer Wins !")
            ComputerScore += 1
            self.scoreComputerText.setText("Computer Score : {}".format(ComputerScore))
            self.scoreComputerText.resize(200,30)
        elif self.randComputerNmb == 2 and self.randPlayerNmb == 1: #paper vs rock
            msg=QMessageBox.information(self,"Information","Computer Wins !")
            ComputerScore += 1
            self.scoreComputerText.setText("Computer Score : {}".format(ComputerScore))
            self.scoreComputerText.resize(200,30)
        elif self.randComputerNmb == 2 and self.randPlayerNmb == 3: #paper vs scissours
            msg=QMessageBox.information(self,"Information","you Win !")
            PlayerScore += 1
            self.scorePlayerText.setText("Your Score : {}".format(PlayerScore))
            self.scorePlayerText.resize(150,30)
        elif self.randComputerNmb == 3 and self.randPlayerNmb== 1:  #scisours vs rock
            msg=QMessageBox.information(self,"Information","you Win !")
            PlayerScore += 1
            self.scorePlayerText.setText("Your Score : {}".format(PlayerScore))
            self.scorePlayerText.resize(150,30)
        elif  self.randComputerNmb == 3 and self.randPlayerNmb == 2: #scissors vs paper
            msg=QMessageBox.information(self,"Information","Computer Wins !")
            ComputerScore += 1
            self.scoreComputerText.setText("Computer Score : {}".format(ComputerScore))
            self.scoreComputerText.resize(200,30)

        if PlayerScore == 3 or ComputerScore == 3 :
            if PlayerScore == 3:
                msg=QMessageBox.information(self,"Information","You Won ! \n CONGRATS!!")
            else:
                msg=QMessageBox.information(self,"Information","Computer WINS !! \n Game over!!")
            sys.exit(1)




def main():
    App=QApplication(sys.argv)
    window=Window()
    #window.start()
    sys.exit(App.exec_())

if __name__=="__main__":
    main()
