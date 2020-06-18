# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap
from ui.display_ui import Ui_DisplayWindow


class DisplayWindow(QMainWindow, Ui_DisplayWindow):

    def __init__(self, num, img, ldir):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.imageLabel.setPixmap(QPixmap(ldir + img + '.jpg'))
        self.imageLabel.setScaledContents(True)
        if num > 3:
            self.redoButton.setVisible(False)
            self.triesLabel.setVisible(True)
            self.displayLabel.setText("Est-ce que cela vous plaît ?")
        else:
            self.redoButton.setVisible(True)
            self.triesLabel.setVisible(False)
            self.displayLabel.setText("Est-ce que cela vous plaît ? (Encore " + str(4-num) + " essais possibles)")
