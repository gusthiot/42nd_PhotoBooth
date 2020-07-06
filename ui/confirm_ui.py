# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'confirm.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ConfirmDialog(object):
    def setupUi(self, ConfirmDialog):
        ConfirmDialog.setObjectName("ConfirmDialog")
        ConfirmDialog.resize(400, 300)
        self.confirmLabel = QtWidgets.QLabel(ConfirmDialog)
        self.confirmLabel.setGeometry(QtCore.QRect(40, 90, 281, 22))
        self.confirmLabel.setObjectName("confirmLabel")
        self.okButton = QtWidgets.QPushButton(ConfirmDialog)
        self.okButton.setGeometry(QtCore.QRect(130, 160, 99, 30))
        self.okButton.setObjectName("okButton")

        self.retranslateUi(ConfirmDialog)
        QtCore.QMetaObject.connectSlotsByName(ConfirmDialog)

    def retranslateUi(self, ConfirmDialog):
        _translate = QtCore.QCoreApplication.translate
        ConfirmDialog.setWindowTitle(_translate("ConfirmDialog", "Dialog"))
        self.confirmLabel.setText(_translate("ConfirmDialog", "Votre demande a bien été enregistrée !"))
        self.okButton.setText(_translate("ConfirmDialog", "OK"))

