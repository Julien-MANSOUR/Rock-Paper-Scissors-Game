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
input_usr = 0 #i add it for the condition : application wont start before the user input
class Window (QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300,300,550,500)
        self.setWindowTitle("Rock Paper Scissors Game")
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
        self.StartButton.move(160,400)
        self.StartButton.clicked.connect(self.start)
        self.StopButton=QPushButton("Stop",self)
        self.StopButton.setFont(buttonFont)
        self.StopButton.move(250,400)
        self.StopButton.clicked.connect(self.stop)
        self.RestartButton=QPushButton("Restart",self)
        self.RestartButton.move(340,400)
        self.RestartButton.clicked.connect(self.restart)
        ########################################################
        self.timer=QTimer(self)
        self.timer.setInterval(100)#en ms
        self.timer.timeout.connect(self.PlayGame)
        ########################user input#####################
        self.TotalScore=QLineEdit(self)
        self.TotalScore.move(160,300)
        self.TotalScore.setPlaceholderText("Enter the final Score")
        self.TotalScore.resize(200,30)
        self.submitButton = QPushButton("Submit",self)
        self.submitButton.move(160,350)
        self.submitButton.clicked.connect(self.submit)
        ##########################Signature###############################
        signature=QLabel("Julien MANSOUR",self)
        signature.setFont(QFont("Bold",8))
        signature.move(400,450)
        ##################################################################
        self.show()


    def submit(self):
        global input_usr
        self.userInput = self.TotalScore.text()
        input_usr = self.userInput #we will use it for the condition of user input
        self.TotalScore.clear()

    def restart(self):
        global PlayerScore
        global ComputerScore
        PlayerScore = 0
        ComputerScore = 0
        self.scoreComputerText.setText("Computer Score : {}/{}".format(ComputerScore,self.userInput))
        self.scorePlayerText.setText("Your Score : {}/{}".format(PlayerScore,self.userInput))

    def start(self):
        global input_usr
        if (input_usr):
            self.timer.start()
        else :
            msf=QMessageBox.warning(self,"WARNING","Please choose the total Score")
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
        global input_usr
        global PlayerScore
        global ComputerScore
        if (input_usr): #app wont start without user input
            self.timer.stop()
            if self.randComputerNmb == self.randPlayerNmb and self.randComputerNmb !=0 and self.randPlayerNmb  != 0: # i used zeros to restart the random numbers, because if i push the stop buttons tow times in a row it increase the same score
                msg=QMessageBox.information(self,"Information","It is a Draw")
            elif self.randComputerNmb == 1 and self.randPlayerNmb == 2:  #rock vs paper
                msg=QMessageBox.information(self,"Information","you Win !")
                PlayerScore += 1
                self.scorePlayerText.setText("Your Score : {}/{}".format(PlayerScore,self.userInput ))
                self.scorePlayerText.resize(150,30)
                self.randComputerNmb = 0
                self.randPlayerNmb = 0
            elif self.randComputerNmb == 1 and self.randPlayerNmb == 3:  #rock vs scissor
                msg=QMessageBox.information(self,"Information","Computer Wins !")
                ComputerScore += 1
                self.scoreComputerText.setText("Computer Score : {}/{}".format(ComputerScore,self.userInput ))
                self.scoreComputerText.resize(250,30)
                self.randComputerNmb = 0 #restart the random numbers to avoid any kind of stop problem
                self.randPlayerNmb = 0
            elif self.randComputerNmb == 2 and self.randPlayerNmb == 1: #paper vs rock
                msg=QMessageBox.information(self,"Information","Computer Wins !")
                ComputerScore += 1
                self.scoreComputerText.setText("Computer Score : {}/{}".format(ComputerScore,self.userInput ))
                self.scoreComputerText.resize(250,30)
                self.randComputerNmb = 0
                self.randPlayerNmb = 0
            elif self.randComputerNmb == 2 and self.randPlayerNmb == 3: #paper vs scissours
                msg=QMessageBox.information(self,"Information","you Win !")
                PlayerScore += 1
                self.scorePlayerText.setText("Your Score : {}/{}".format(PlayerScore,self.userInput ))
                self.scorePlayerText.resize(150,30)
                self.randComputerNmb = 0
                self.randPlayerNmb = 0
            elif self.randComputerNmb == 3 and self.randPlayerNmb== 1:  #scisours vs rock
                msg=QMessageBox.information(self,"Information","you Win !")
                PlayerScore += 1
                self.scorePlayerText.setText("Your Score : {}/{}".format(PlayerScore,self.userInput ))
                self.scorePlayerText.resize(150,30)
                self.randComputerNmb = 0
                self.randPlayerNmb = 0
            elif  self.randComputerNmb == 3 and self.randPlayerNmb == 2: #scissors vs paper
                msg=QMessageBox.information(self,"Information","Computer Wins !")
                ComputerScore += 1
                self.scoreComputerText.setText("Computer Score : {}/{}".format(ComputerScore,self.userInput ))
                self.scoreComputerText.resize(250,30)
                self.randComputerNmb = 0
                self.randPlayerNmb = 0
            if PlayerScore == int(self.userInput)  or ComputerScore == int(self.userInput)  :
                #print("doneeeeeeee")
                if PlayerScore == int(self.userInput) :
                    msg=QMessageBox.information(self,"Information","You Won ! \n CONGRATS!!")
                else:
                    msg=QMessageBox.information(self,"Information","Computer WINS !! \n Game over!!")
                sys.exit(1)
        else:
            msf=QMessageBox.warning(self,"WARNING","Please choose the total Score")



def main():
    App=QApplication(sys.argv)
    window=Window()
    #window.start()
    sys.exit(App.exec_())

if __name__=="__main__":
    main()
