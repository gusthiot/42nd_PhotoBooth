# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'thanks.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ThanksWindow(object):
    def setupUi(self, ThanksWindow):
        ThanksWindow.setObjectName("ThanksWindow")
        ThanksWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(ThanksWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.thanksLabel = QtWidgets.QLabel(self.centralwidget)
        self.thanksLabel.setGeometry(QtCore.QRect(20, 20, 201, 71))
        self.thanksLabel.setObjectName("thanksLabel")
        self.socialLabel = QtWidgets.QLabel(self.centralwidget)
        self.socialLabel.setGeometry(QtCore.QRect(20, 100, 401, 41))
        self.socialLabel.setObjectName("socialLabel")
        self.emailLabel = QtWidgets.QLabel(self.centralwidget)
        self.emailLabel.setGeometry(QtCore.QRect(20, 190, 311, 17))
        self.emailLabel.setObjectName("emailLabel")
        self.adressEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.adressEdit.setGeometry(QtCore.QRect(260, 250, 291, 25))
        self.adressEdit.setObjectName("adressEdit")
        self.adressLabel = QtWidgets.QLabel(self.centralwidget)
        self.adressLabel.setGeometry(QtCore.QRect(80, 250, 141, 20))
        self.adressLabel.setObjectName("adressLabel")
        self.okButton = QtWidgets.QPushButton(self.centralwidget)
        self.okButton.setGeometry(QtCore.QRect(180, 350, 89, 25))
        self.okButton.setObjectName("okButton")
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(350, 350, 89, 25))
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(460, 80, 160, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.socialLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.socialLayout.setContentsMargins(0, 0, 0, 0)
        self.socialLayout.setObjectName("socialLayout")
        self.socialYesButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.socialYesButton.setChecked(True)
        self.socialYesButton.setObjectName("socialYesButton")
        self.socialLayout.addWidget(self.socialYesButton)
        self.socialNoButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.socialNoButton.setChecked(False)
        self.socialNoButton.setObjectName("socialNoButton")
        self.socialLayout.addWidget(self.socialNoButton)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(460, 160, 160, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.emailLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.emailLayout.setContentsMargins(0, 0, 0, 0)
        self.emailLayout.setObjectName("emailLayout")
        self.emailYesButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.emailYesButton.setChecked(False)
        self.emailYesButton.setObjectName("emailYesButton")
        self.emailLayout.addWidget(self.emailYesButton)
        self.emailNoButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.emailNoButton.setChecked(True)
        self.emailNoButton.setObjectName("emailNoButton")
        self.emailLayout.addWidget(self.emailNoButton)
        ThanksWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ThanksWindow)
        self.statusbar.setObjectName("statusbar")
        ThanksWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ThanksWindow)
        QtCore.QMetaObject.connectSlotsByName(ThanksWindow)

    def retranslateUi(self, ThanksWindow):
        _translate = QtCore.QCoreApplication.translate
        ThanksWindow.setWindowTitle(_translate("ThanksWindow", "Thanks"))
        self.thanksLabel.setText(_translate("ThanksWindow", " Merci pour votre photo !"))
        self.socialLabel.setText(_translate("ThanksWindow", "Voulez-vous qu\'elle soit visible sur les réseaux sociaux ?"))
        self.emailLabel.setText(_translate("ThanksWindow", "Voulez-vous la recevoir par e-mail ?"))
        self.adressLabel.setText(_translate("ThanksWindow", "Adresse e-mail :"))
        self.okButton.setText(_translate("ThanksWindow", "Ok"))
        self.cancelButton.setText(_translate("ThanksWindow", "Annuler"))
        self.socialYesButton.setText(_translate("ThanksWindow", "Oui"))
        self.socialNoButton.setText(_translate("ThanksWindow", "Non"))
        self.emailYesButton.setText(_translate("ThanksWindow", "Oui"))
        self.emailNoButton.setText(_translate("ThanksWindow", "Non"))

