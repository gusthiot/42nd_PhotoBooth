# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow
from ui.number_ui import Ui_NumberWindow


class NumberWindow(QMainWindow, Ui_NumberWindow):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

    def setNumber(self, number):
        self.numberLabel.setText(number)
