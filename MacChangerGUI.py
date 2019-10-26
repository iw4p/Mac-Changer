from PyQt5 import QtWidgets, uic
import sys
import subprocess
import re

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('MacChangerUi.ui', self)
        self.changeButton
        self.button = self.findChild(QtWidgets.QPushButton, 'changeButton')
        self.button.clicked.connect(self.changeButtonPressed) 
        self.interface = self.findChild(QtWidgets.QLineEdit, 'lineEdit')
        self.new_mac = self.findChild(QtWidgets.QLineEdit, 'macAddressInput')
        self.show()

    def changeButtonPressed(self):
        print(self.new_mac.text())
        print(self.interface.text())

    

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()