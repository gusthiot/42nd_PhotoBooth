# -*- coding: utf-8 -*-


import logging
from PyQt5.QtCore import pyqtSignal, QThread, QTimer
from wait_window import WaitWindow


class Watcher (QThread):

    standbySignal = pyqtSignal()

    def __init__(self, waitVid):
        QThread.__init__(self)
        self.logger = logging.getLogger(__name__)
        self.w_w = WaitWindow(waitVid)
        self.running = False

    def setRunning(self):
        print("running")
        self.running = True

    def run(self):
        print("run")
        self.logger.info("Surveillant démarré")
        minutes = 0
        while True:
            print(minutes)
            timer = QTimer()
            timer.start(1000)
            if not self.running:
                if minutes < 5:
                    minutes += 1
                else:
                    break
            else:
                minutes = 0
                self.running = False
        self.w_w.player.play()
        self.standbySignal.emit()
        print("broken")
