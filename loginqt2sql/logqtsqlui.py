# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import os

ABSOLUT_PATH1 = os.path.dirname(os.path.realpath(__file__))+'/figs/spyn.png'
ABSOLUT_PATH2 = os.path.dirname(os.path.realpath(__file__))+'/figs/splash.png'
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(414, 749)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(414, 749))
        MainWindow.setMaximumSize(QtCore.QSize(414, 749))
        icon = QtGui.QIcon()
        #icon.addPixmap(QtGui.QPixmap("figs/spyn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(ABSOLUT_PATH1), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgba(112, 124, 131,1);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-60, 0, 491, 291))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("figs/splash.png"))
        self.label.setPixmap(QtGui.QPixmap(ABSOLUT_PATH2))
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.ln_user = QtWidgets.QLineEdit(self.centralwidget)
        self.ln_user.setGeometry(QtCore.QRect(80, 320, 251, 41))
        self.ln_user.setStyleSheet("color: rgb(255, 255, 255);")
        self.ln_user.setText("")
        self.ln_user.setObjectName("ln_user")
        self.ln_password = QtWidgets.QLineEdit(self.centralwidget)
        self.ln_password.setGeometry(QtCore.QRect(80, 380, 251, 41))
        self.ln_password.setStyleSheet("color: rgb(255, 255, 255);")
        self.ln_password.setText("")
        self.ln_password.setObjectName("ln_password")
        self.btn_login = QtWidgets.QPushButton(self.centralwidget)
        self.btn_login.setGeometry(QtCore.QRect(100, 440, 211, 51))
        self.btn_login.setObjectName("btn_login")
        self.btn_register = QtWidgets.QPushButton(self.centralwidget)
        self.btn_register.setGeometry(QtCore.QRect(130, 500, 151, 31))
        self.btn_register.setObjectName("btn_register")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 414, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "loguin2SQL"))
        self.ln_user.setPlaceholderText(_translate("MainWindow", "User"))
        self.ln_password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.btn_login.setText(_translate("MainWindow", "LOGIN"))
        self.btn_register.setText(_translate("MainWindow", "Register"))
