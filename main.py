import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer

from ui.welcome_ui import Ui_WelcomeWindow
from ui.intro_ui import Ui_IntroWindow
from ui.thanks_ui import Ui_ThanksWindow
from camera import Camera
from sftp import Sftp
 
class WelcomeWindow(QMainWindow, Ui_WelcomeWindow):
    
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.takeButton.clicked.connect(self.openIntroWindow)
        self.intro = IntroWindow()
        
    def openIntroWindow(self):
        self.intro.showFullScreen()
        # self.close()

class IntroWindow(QMainWindow, Ui_IntroWindow):
    
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.takeButton.clicked.connect(self.takePicture)
        self.thanks = ThanksWindow()
        
    def takePicture(self):
        img = cam.takePicture()
        self.close()
        self.thanks.showFullScreen()
        Sftp.put(img, ldir)
        QTimer.singleShot(5000, self.closeThanks)
        
    def closeThanks(self):
        self.thanks.close()      

class ThanksWindow(QMainWindow, Ui_ThanksWindow):
    
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ldir = "/home/pi/Photos/"
    cam = Camera(ldir)
    window = WelcomeWindow()
    window.showFullScreen()

    sys.exit(app.exec_())
