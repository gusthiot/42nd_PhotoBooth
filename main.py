# -*- coding: utf-8 -*-

import sys
import os
import logging
import time
from PyQt5.QtWidgets import QApplication
from black_window import BlackWindow
from process import Process

# photoDirectory = "/home/pi/Photos/"
photoDirectory = "/home/christophe/42nd_PhotoBooth/Photos/"
waitVideo = "wait.webm"
welcomeVideo = "welcome.mp4"
# logDirectory = "/home/pi/42nd_PhotoBooth/log"
logDirectory = "/home/christophe/42nd_PhotoBooth/log"
remoteDirectory = "/photobooth/"

if not os.path.exists(photoDirectory):
    os.mkdir(photoDirectory)

if not os.path.exists(logDirectory):
    os.mkdir(logDirectory)

filename = logDirectory + "/photobooth_" + time.strftime("%y%m%d") + ".log"
logging.basicConfig(filename=filename, format='%(asctime)s - %(name)s(%(levelname)s) : %(message)s',
                    level=logging.INFO, datefmt='%m/%d/%Y %I:%M:%S')
logger = logging.getLogger(__name__)
logger.info('Programme lancé')

os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"
app = QApplication(sys.argv)
b_w = BlackWindow()
b_w.showFullScreen()

process = Process(photoDirectory, remoteDirectory, welcomeVideo, waitVideo)
process.start()
sys.exit(app.exec_())
