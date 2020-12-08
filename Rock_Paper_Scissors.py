#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap,QFont
from PyQt5.QtCore import QTimer

font=QFont("Times",12)
class Window (QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300,300,500,500)
        self.setWindowTitle("mosso")
        self.UI()

    def UI(self):
        self.show()



def main():
    App=QApplication(sys.argv)
    window=Window()
    #window.start()
    sys.exit(App.exec_())

if __name__=="__main__":
    main()
