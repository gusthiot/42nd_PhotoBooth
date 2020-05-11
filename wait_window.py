# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QUrl, QDir
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from ui.wait_ui import Ui_WaitWindow


class WaitWindow(QMainWindow, Ui_WaitWindow):

    def __init__(self, waitVid):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.pList = QMediaPlaylist()
        baseUrl = QUrl("file://" + QDir.currentPath() + "/")
        urlMedia = QUrl(waitVid)
        fullMedia = baseUrl.resolved(urlMedia)
        self.pList.addMedia(QMediaContent(fullMedia))
        self.player.setPlaylist(self.pList)
        self.pList.setPlaybackMode(QMediaPlaylist.CurrentItemInLoop)
        self.player.setVideoOutput(self.waitVideo)
