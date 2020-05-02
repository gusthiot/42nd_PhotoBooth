# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow
from ui.thanks_ui import Ui_ThanksWindow


class ThanksWindow(QMainWindow, Ui_ThanksWindow):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.adressLabel.setVisible(False)
        self.adressEdit.setVisible(False)
