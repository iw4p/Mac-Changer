from PyQt5 import QtWidgets, uic
import sys
import os
import subprocess
import re

def getmac(iface):
    try:
        mac = open('/sys/class/net/'+iface+'/address').readline()
    except:
        mac = "00:00:00:00:00:00"
    return mac[0:17]

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('MacChangerUi.ui', self)
        # self.changeButton
        self.buttonShow = self.findChild(QtWidgets.QPushButton, 'showButton')
        self.buttonShow.clicked.connect(self.showButtonPressed) 
        self.button = self.findChild(QtWidgets.QPushButton, 'changeButton')
        self.button.clicked.connect(self.changeButtonPressed) 
        self.interface = self.findChild(QtWidgets.QLineEdit, 'lineEdit')
        self.new_mac = self.findChild(QtWidgets.QLineEdit, 'macAddressInput')
        self.show()

    def changeButtonPressed(self):
        # print(self.new_mac.text())
        # print(self.interface.text())
        myMac = getmac(self.interface.text())
        interface = self.interface.text()
        new_mac = self.new_mac.text()
        os.system('ifconfig ' + interface + ' down')
        # subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
        os.system('ifconfig ' + interface + ' hw ether ' + new_mac)
        os.system('ifconfig ' + interface + ' up')
        print(myMac)

    def showButtonPressed(self):
        # myMac = getmac(self.interface.text())
        # interface = self.interface.text()
        # new_mac = self.new_mac.text()
        # os.system('ifconfig ' + interface + ' down')
        # os.system('ifconfig ' + interface + ' hw ether ' + new_mac)
        cmd = """ip -o link | awk '$2 != "lo:" {print $2, $(NF-2)}'"""
        output = os.system(cmd)
        print(output)
    

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()