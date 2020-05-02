# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QUrl, QDir
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from ui.welcome_ui import Ui_WelcomeWindow


class WelcomeWindow(QMainWindow, Ui_WelcomeWindow):

    def __init__(self, welcomeVid):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        BaseUrl = QUrl("file://" + QDir.currentPath() + "/")
        UrlMedia = QUrl(welcomeVid)
        FullMedia = BaseUrl.resolved(UrlMedia)
        self.player.setMedia(QMediaContent(FullMedia))

    def play(self):
        print("play")
        try:
            self.player.setVideoOutput(self.welcomeVideo)
            self.player.play()
        except:
            print("error")

    def pause(self):
        self.player.pause()

    def stop(self):
        self.player.stop()
