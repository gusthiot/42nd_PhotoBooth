# -*- coding: utf-8 -*-

import sys
import os
from PyQt5.QtWidgets import QApplication
from black_window import BlackWindow
from process import Process

ldir = "/home/pi/Photos/"
veilleVideo = "veille.mp4"
welcomeVideo = "welcome.mp4"

os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"
app = QApplication(sys.argv)
b_w = BlackWindow()
b_w.showFullScreen()
process = Process(ldir, welcomeVideo)
process.start()
sys.exit(app.exec_())
