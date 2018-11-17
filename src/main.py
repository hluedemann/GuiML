from __future__ import with_statement

#python
import numpy as np
import sys

#qt
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication

#GuiML
from MainWindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow, QtCore.QObject):
    def __init__(self,parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)


# create the GUI application
app = QApplication(sys.argv)
# instantiate the main window
dmw = MainWindow()
# show it
dmw.showMaximized()
# start the Qt main loop execution, exiting from this script
# with the same return code of Qt application
sys.exit(app.exec_())
