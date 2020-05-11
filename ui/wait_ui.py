# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wait.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WaitWindow(object):
    def setupUi(self, WaitWindow):
        WaitWindow.setObjectName("WaitWindow")
        WaitWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(WaitWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.waitVideo = QVideoWidget(self.centralwidget)
        self.waitVideo.setGeometry(QtCore.QRect(-170, -10, 1021, 701))
        self.waitVideo.setObjectName("waitVideo")
        WaitWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(WaitWindow)
        self.statusbar.setObjectName("statusbar")
        WaitWindow.setStatusBar(self.statusbar)

        self.retranslateUi(WaitWindow)
        QtCore.QMetaObject.connectSlotsByName(WaitWindow)

    def retranslateUi(self, WaitWindow):
        _translate = QtCore.QCoreApplication.translate
        WaitWindow.setWindowTitle(_translate("WaitWindow", "MainWindow"))

from PyQt5.QtMultimediaWidgets import QVideoWidget
