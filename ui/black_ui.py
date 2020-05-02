# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'black.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BlackWindow(object):
    def setupUi(self, BlackWindow):
        BlackWindow.setObjectName("BlackWindow")
        BlackWindow.resize(800, 600)
        BlackWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(BlackWindow)
        self.centralwidget.setObjectName("centralwidget")
        BlackWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(BlackWindow)
        self.statusbar.setObjectName("statusbar")
        BlackWindow.setStatusBar(self.statusbar)

        self.retranslateUi(BlackWindow)
        QtCore.QMetaObject.connectSlotsByName(BlackWindow)

    def retranslateUi(self, BlackWindow):
        _translate = QtCore.QCoreApplication.translate
        BlackWindow.setWindowTitle(_translate("BlackWindow", "MainWindow"))

