# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow
from ui.black_ui import Ui_BlackWindow


class BlackWindow(QMainWindow, Ui_BlackWindow):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)