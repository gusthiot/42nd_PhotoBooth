# -*- coding: utf-8 -*-

import json
import time
import re
import logging
from PyQt5.QtCore import pyqtSignal, QObject, QTimer
from welcome_window import WelcomeWindow
from display_window import DisplayWindow
from thanks_window import ThanksWindow
# from camera import Camera
# from sftp import Sftp


class Process(QObject):

    activitySignal = pyqtSignal()

    def __init__(self, ldir, welcomeVid, waitVid):
        QObject.__init__(self)
        self.logger = logging.getLogger(__name__)
        self.ldir = ldir
        # cam = Camera(ldir)
        self.w_w = WelcomeWindow(welcomeVid)
        self.watcher = Watcher(waitVid)
        self.activitySignal.connect(self.watcher.setRunning)
        self.watcher.standbySignal.connect(self.reinit)
        self.t_w = None
        self.d_w = None
        self.num = 0
        self.img = "20200501_132612"

    def reinit(self):
        self.t_w = None
        self.d_w = None
        self.num = 0

    def start(self):
        self.noteActivity("Processus central démarré")
        self.w_w.takeButton.clicked.connect(self.takePicture)
        self.w_w.showFullScreen()
        self.w_w.player.play()
        self.noteActivity("Ecran de bienvenue affiché")
        QTimer.singleShot(10000, self.p)

    def takePicture(self):
        self.w_w.player.pause()
        self.noteActivity("Bouton 'Prendre une photo' appuyé")
        self.picture()

    def picture(self):
        #  img = self.cam.takePicture()
        self.noteActivity("Photo prise")
        #  Sftp.put(img, ldir)
        self.num = self.num + 1
        self.d_w = DisplayWindow(self.num, self.img, self.ldir)
        self.d_w.redoButton.clicked.connect(self.redoPicture)
        self.d_w.okButton.clicked.connect(self.okPicture)
        self.d_w.cancelButton.clicked.connect(self.cancelPicture)
        self.d_w.showFullScreen()
        self.noteActivity("Ecran d'affichage affiché")

    def redoPicture(self):
        self.noteActivity("Nouvelle photo demandée")
        self.d_w.close()
        self.d_w = None
        self.picture()

    def cancelPicture(self):
        self.noteActivity("Processus de photo annulé")
        self.d_w.close()
        self.reinit()
        self.w_w.player.play()

    def okPicture(self):
        self.noteActivity("Photo acceptée")
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
        self.noteActivity("Ecran d'envoi affiché")

    def okThanks(self):
        self.noteActivity("Bouton ok envoi appuyé")
        if self.t_w.sendEmail() and not re.match(r"[^@]+@[^@]+\.[^@]+", self.t_w.getEmail()):
            self.noteActivity("Mauvais format d'adresse e-mail : ok non-soumis, message d'erreur affiché")
            self.t_w.setErrorMessage("Mauvais format d'adresse e-mail")
        else:
            data = {'date': time.strftime("%d-%m-%y"), 'heure': time.strftime("%H:%M")}
            if self.t_w.sendSocial():
                data['social media'] = "yes"
            else:
                data['social media'] = "no"
            if self.t_w.sendEmail():
                data['email'] = self.t_w.getEmail()
            else:
                data['email'] = "no"
            with open(self.ldir + self.img + '.json', mode='w') as outfile:
                json.dump(data, outfile, indent=4)
            self.noteActivity("JSON sauvegardé")
            self.t_w.close()
            self.reinit()
            self.w_w.player.play()
            self.noteActivity("Processus réinitialisé")

    def cancelThanks(self):
        self.noteActivity("Processus de photo annulé")
        self.t_w.close()
        self.reinit()
        self.w_w.player.play()

    def yesEmail(self):
        self.noteActivity("Demande d'envoi par e-mail")
        self.t_w.adressLabel.setVisible(True)
        self.t_w.adressEdit.setVisible(True)

    def noEmail(self):
        self.noteActivity("Refus d'envoi par e-mail")
        self.t_w.adressLabel.setVisible(False)
        self.t_w.adressEdit.setVisible(False)

    def yesSocial(self):
        self.noteActivity("Demande de mise sur les réseaux sociaux")
        self.sendSocial = True

    def noSocial(self):
        self.noteActivity("Refus de mise sur les réseaux sociaux")
        self.sendSocial = False

    def noteActivity(self, message):
        self.logger.info(message)
        self.activitySignal.emit()
