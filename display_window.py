# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow
from ui.display_ui import Ui_DisplayWindow


class DisplayWindow(QMainWindow, Ui_DisplayWindow):

    def __init__(self, num):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        if num > 3:
            self.redoButton.setVisible(False)
            self.triesLabel.setVisible(True)
        else:
            self.redoButton.setVisible(True)
            self.triesLabel.setVisible(False)
