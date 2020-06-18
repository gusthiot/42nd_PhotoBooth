# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from ui.welcome_ui import Ui_WelcomeWindow


class WelcomeWindow(QMainWindow, Ui_WelcomeWindow):

    def __init__(self, welcomeVid):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.pList = QMediaPlaylist()
        media = QUrl("file://" + welcomeVid)
        self.pList.addMedia(QMediaContent(media))
        self.player.setPlaylist(self.pList)
        self.pList.setPlaybackMode(QMediaPlaylist.CurrentItemInLoop)
        self.player.setVideoOutput(self.welcomeVideo)