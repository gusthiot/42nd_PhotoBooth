# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication
# from PyQt5.QtCore import QTimer
from welcome_window import WelcomeWindow
from display_window import DisplayWindow
from thanks_window import ThanksWindow
# from camera import Camera
# from sftp import Sftp


class Process:

    def __init__(self, ldir, welcomeVid):
        self.ldir = ldir
        # cam = Camera(ldir)
        self.w_w = WelcomeWindow(welcomeVid)
        self.t_w = None
        self.d_w = None
        self.num = 0
        self.sendSocial = False

    def start(self):
        self.w_w.takeButton.clicked.connect(self.takePicture)
        self.w_w.showFullScreen()
        self.w_w.play()

    def takePicture(self):
        self.w_w.pause()
    #    img = self.cam.takePicture()
        # self.thanks.showFullScreen()
        #  Sftp.put(img, ldir)
        # QTimer.singleShot(5000, self.closeThanks)
        self.num = self.num + 1
        self.d_w = DisplayWindow(self.num)  # img)
        self.d_w.redoButton.clicked.connect(self.redoPicture)
        self.d_w.okButton.clicked.connect(self.okPicture)
        self.d_w.cancelButton.clicked.connect(self.cancelPicture)
        self.d_w.showFullScreen()

    def redoPicture(self):
        self.d_w.close()
        self.d_w = None
        self.takePicture()

    def cancelPicture(self):
        self.num = 0
        self.d_w.close()
        self.d_w = None
        self.w_w.play()

    def okPicture(self):
        self.num = 0
        self.d_w.close()
        self.d_w = None
        self.t_w = ThanksWindow()
        self.t_w.okButton.clicked.connect(self.okThanks)
        self.t_w.cancelButton.clicked.connect(self.cancelThanks)
        self.t_w.emailYesButton.clicked.connect(self.yesEmail)
        self.t_w.emailNoButton.clicked.connect(self.noEmail)
        self.t_w.socialYesButton.clicked.connect(self.yesSocial)
        self.t_w.socialNoButton.clicked.connect(self.noSocial)
        self.t_w.showFullScreen()

    def okThanks(self):
        self.t_w.close()
        self.t_w = None

    def cancelThanks(self):
        self.t_w.close()
        self.t_w = None

    def yesEmail(self):
        self.t_w.adressLabel.setVisible(True)
        self.t_w.adressEdit.setVisible(True)
    def noEmail(self):
        self.t_w.adressLabel.setVisible(False)
        self.t_w.adressEdit.setVisible(False)

    def yesSocial(self):
        self.sendSocial = True

    def noSocial(self):
        self.sendSocial = False
