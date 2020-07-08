# This Python file uses the following encoding: utf-8

"""
Fichier principal à lancer pour faire tourner le logiciel

Usage:
  main.py [options]

Options:

  -h   --help              Affiche le présent message
  --pc                     Utilise les paramètres pc au lieu de Raspberry Pi
"""
import sys
import os
import logging
import time
import traceback
from docopt import docopt
from PyQt5.QtWidgets import QApplication
from black_window import BlackWindow
from process import Process

arguments = docopt(__doc__)

if arguments["--pc"]:
    withCam = False
    mainDirectory = "/home/christophe/42nd_PhotoBooth/"
    photoDirectory = mainDirectory + "Photos/"
else:
    withCam = True
    mainDirectory = "/home/pi/42nd_PhotoBooth/"
    photoDirectory = "/home/pi/Photos/"

logDirectory = mainDirectory + "log"
    
waitVideo = "welcome.mp4"
welcomeVideo = "wait.webm"

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
try:
    # os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"
    # os.environ["QT_DEBUG_PLUGINS"] = "1"
    # os.environ["GST_DEBUG"] = "3"
    app = QApplication(sys.argv)
    b_w = BlackWindow()
    b_w.showFullScreen()

    process = Process(photoDirectory, remoteDirectory, welcomeVideo,
                      waitVideo, mainDirectory, withCam)
    process.start()
except:
    logger.error(traceback.format_exc())
