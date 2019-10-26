from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Ui_MacChanger(object):
    def setupUi(self, MacChanger):
        MacChanger.setObjectName("MacChanger")
        MacChanger.resize(278, 244)
        self.centralwidget = QtWidgets.QWidget(MacChanger)
        self.centralwidget.setObjectName("centralwidget")
        self.changeButton = QtWidgets.QPushButton(self.centralwidget)
        self.changeButton.setGeometry(QtCore.QRect(100, 170, 80, 25))
        self.changeButton.setObjectName("changeButton")
        self.changeButton.clicked.connect(on_button_clicked)

        self.interfaceComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.interfaceComboBox.setGeometry(QtCore.QRect(40, 20, 201, 25))
        self.interfaceComboBox.setObjectName("interfaceComboBox")
        self.macAddressInput = QtWidgets.QLineEdit(self.centralwidget)
        self.macAddressInput.setGeometry(QtCore.QRect(40, 60, 201, 25))
        self.macAddressInput.setInputMethodHints(QtCore.Qt.ImhNone)
        self.macAddressInput.setPlaceholderText("")
        self.macAddressInput.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.macAddressInput.setClearButtonEnabled(True)
        self.macAddressInput.setObjectName("macAddressInput")
        self.resultLabel = QtWidgets.QLabel(self.centralwidget)
        self.resultLabel.setGeometry(QtCore.QRect(40, 90, 201, 71))
        self.resultLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.resultLabel.setWordWrap(True)
        self.resultLabel.setObjectName("resultLabel")
        MacChanger.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MacChanger)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 278, 22))
        self.menubar.setObjectName("menubar")
        self.menuAbout_Me = QtWidgets.QMenu(self.menubar)
        self.menuAbout_Me.setObjectName("menuAbout_Me")
        MacChanger.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MacChanger)
        self.statusbar.setObjectName("statusbar")
        MacChanger.setStatusBar(self.statusbar)
        self.actionAbout_me = QtWidgets.QAction(MacChanger)
        self.actionAbout_me.setObjectName("actionAbout_me")
        self.actionClose = QtWidgets.QAction(MacChanger)
        self.actionClose.setObjectName("actionClose")
        self.menuAbout_Me.addAction(self.actionAbout_me)
        self.menuAbout_Me.addSeparator()
        self.menuAbout_Me.addAction(self.actionClose)
        self.menubar.addAction(self.menuAbout_Me.menuAction())

        self.retranslateUi(MacChanger)
        QtCore.QMetaObject.connectSlotsByName(MacChanger)

    def retranslateUi(self, MacChanger):
        _translate = QtCore.QCoreApplication.translate
        MacChanger.setWindowTitle(_translate("MacChanger", "Mac Changer"))
        self.changeButton.setText(_translate("MacChanger", "Change"))
        self.macAddressInput.setInputMask(_translate("MacChanger", "xx:xx:xx:xx:xx:xx"))
        self.resultLabel.setText(_translate("MacChanger", "I\'m waiting for you"))
        self.menuAbout_Me.setTitle(_translate("MacChanger", "About Me"))
        self.actionAbout_me.setText(_translate("MacChanger", "About me"))
        self.actionClose.setText(_translate("MacChanger", "Close"))


def on_button_clicked():
    alert = QMessageBox()
    alert.setText('You clicked the button!')
    alert.exec_()