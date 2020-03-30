# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WelcomeWindow(object):
    def setupUi(self, WelcomeWindow):
        WelcomeWindow.setObjectName("WelcomeWindow")
        WelcomeWindow.resize(840, 600)
        self.centralwidget = QtWidgets.QWidget(WelcomeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.takeButton = QtWidgets.QPushButton(self.centralwidget)
        self.takeButton.setGeometry(QtCore.QRect(120, 180, 211, 30))
        self.takeButton.setObjectName("takeButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 70, 401, 61))
        self.label.setObjectName("label")
        WelcomeWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(WelcomeWindow)
        self.statusbar.setObjectName("statusbar")
        WelcomeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(WelcomeWindow)
        QtCore.QMetaObject.connectSlotsByName(WelcomeWindow)

    def retranslateUi(self, WelcomeWindow):
        _translate = QtCore.QCoreApplication.translate
        WelcomeWindow.setWindowTitle(_translate("WelcomeWindow", "Bienvenue  !"))
        self.takeButton.setText(_translate("WelcomeWindow", "Prendre une photo"))
        self.label.setText(_translate("WelcomeWindow", "Bienvenue dans le PhotoBooth de 42nd Street !!!"))

