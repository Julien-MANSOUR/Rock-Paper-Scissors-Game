#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap,QFont
from PyQt5.QtCore import QTimer

textFont=QFont("Times",16)
buttonFont=QFont("Arial",12)
class Window (QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300,300,500,500)
        self.setWindowTitle("mosso")
        self.UI()

    def UI(self):
        ########################Score########################
        self.scoreComputer=QLabel("Computer Score : ",self)
        self.scoreComputer.move(30,20)
        self.scoreComputer.setFont(textFont)
        self.scoreComputer.setStyleSheet("background-color:red")
        self.scorePlayer=QLabel("Your Score : ",self)
        self.scorePlayer.move(330,20)
        self.scorePlayer.setFont(textFont)
        self.scorePlayer.setStyleSheet("background-color:blue")
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


        self.show()



def main():
    App=QApplication(sys.argv)
    window=Window()
    #window.start()
    sys.exit(App.exec_())

if __name__=="__main__":
    main()
