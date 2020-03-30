# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'thanks.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ThanksWindow(object):
    def setupUi(self, ThanksWindow):
        ThanksWindow.setObjectName("ThanksWindow")
        ThanksWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(ThanksWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 190, 461, 121))
        self.label.setObjectName("label")
        ThanksWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ThanksWindow)
        self.statusbar.setObjectName("statusbar")
        ThanksWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ThanksWindow)
        QtCore.QMetaObject.connectSlotsByName(ThanksWindow)

    def retranslateUi(self, ThanksWindow):
        _translate = QtCore.QCoreApplication.translate
        ThanksWindow.setWindowTitle(_translate("ThanksWindow", "Thanks"))
        self.label.setText(_translate("ThanksWindow", " Merci pour votre photo ! \n"
" Vous pourrez la voir prochainement sur nos réseaux sociaux."))

