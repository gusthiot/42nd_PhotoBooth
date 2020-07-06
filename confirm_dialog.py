# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QDialog
from ui.confirm_ui import Ui_ConfirmDialog


class ConfirmDialog(QDialog, Ui_ConfirmDialog):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)