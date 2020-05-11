# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'display.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DisplayWindow(object):
    def setupUi(self, DisplayWindow):
        DisplayWindow.setObjectName("DisplayWindow")
        DisplayWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(DisplayWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.displayLabel = QtWidgets.QLabel(self.centralwidget)
        self.displayLabel.setGeometry(QtCore.QRect(110, 70, 451, 41))
        self.displayLabel.setObjectName("displayLabel")
        self.okButton = QtWidgets.QPushButton(self.centralwidget)
        self.okButton.setGeometry(QtCore.QRect(60, 510, 89, 25))
        self.okButton.setObjectName("okButton")
        self.redoButton = QtWidgets.QPushButton(self.centralwidget)
        self.redoButton.setGeometry(QtCore.QRect(200, 510, 191, 25))
        self.redoButton.setObjectName("redoButton")
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(450, 510, 89, 25))
        self.cancelButton.setObjectName("cancelButton")
        self.triesLabel = QtWidgets.QLabel(self.centralwidget)
        self.triesLabel.setGeometry(QtCore.QRect(180, 550, 361, 20))
        self.triesLabel.setObjectName("triesLabel")
        self.imageLabel = QtWidgets.QLabel(self.centralwidget)
        self.imageLabel.setGeometry(QtCore.QRect(230, 150, 411, 291))
        self.imageLabel.setText("")
        self.imageLabel.setObjectName("imageLabel")
        DisplayWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(DisplayWindow)
        self.statusbar.setObjectName("statusbar")
        DisplayWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DisplayWindow)
        QtCore.QMetaObject.connectSlotsByName(DisplayWindow)

    def retranslateUi(self, DisplayWindow):
        _translate = QtCore.QCoreApplication.translate
        DisplayWindow.setWindowTitle(_translate("DisplayWindow", "Affichage"))
        self.displayLabel.setText(_translate("DisplayWindow", "Est-ce que cela vous plaît ?"))
        self.okButton.setText(_translate("DisplayWindow", "Oui !"))
        self.redoButton.setText(_translate("DisplayWindow", "Non ! On veut la refaire !"))
        self.cancelButton.setText(_translate("DisplayWindow", "Annuler"))
        self.triesLabel.setText(_translate("DisplayWindow", "Vous avez fait assez d\'essais, acceptez ou annulez !"))

