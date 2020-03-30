# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'intro.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_IntroWindow(object):
    def setupUi(self, IntroWindow):
        IntroWindow.setObjectName("IntroWindow")
        IntroWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(IntroWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 190, 351, 121))
        self.label.setObjectName("label")
        self.takeButton = QtWidgets.QPushButton(self.centralwidget)
        self.takeButton.setGeometry(QtCore.QRect(100, 320, 141, 30))
        self.takeButton.setObjectName("takeButton")
        IntroWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(IntroWindow)
        self.statusbar.setObjectName("statusbar")
        IntroWindow.setStatusBar(self.statusbar)

        self.retranslateUi(IntroWindow)
        QtCore.QMetaObject.connectSlotsByName(IntroWindow)

    def retranslateUi(self, IntroWindow):
        _translate = QtCore.QCoreApplication.translate
        IntroWindow.setWindowTitle(_translate("IntroWindow", "Introduction"))
        self.label.setText(_translate("IntroWindow", "Le preview va s\'afficher pendant 5 secondes \n"
" avant que la photo ne soit prise"))
        self.takeButton.setText(_translate("IntroWindow", "Prendre la photo"))

