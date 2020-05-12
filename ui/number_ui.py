# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'number.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NumberWindow(object):
    def setupUi(self, NumberWindow):
        NumberWindow.setObjectName("NumberWindow")
        NumberWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(NumberWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.numberLabel = QtWidgets.QLabel(self.centralwidget)
        self.numberLabel.setGeometry(QtCore.QRect(350, 260, 81, 61))
        self.numberLabel.setObjectName("numberLabel")
        NumberWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(NumberWindow)
        self.statusbar.setObjectName("statusbar")
        NumberWindow.setStatusBar(self.statusbar)

        self.retranslateUi(NumberWindow)
        QtCore.QMetaObject.connectSlotsByName(NumberWindow)

    def retranslateUi(self, NumberWindow):
        _translate = QtCore.QCoreApplication.translate
        NumberWindow.setWindowTitle(_translate("NumberWindow", "MainWindow"))
        self.numberLabel.setText(_translate("NumberWindow", "5"))

