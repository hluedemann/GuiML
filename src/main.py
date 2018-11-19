from __future__ import with_statement

#python
import numpy as np
import sys
import os

#qt
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog

#GuiML
from MainWindow import Ui_MainWindow
from DataManagement import DataOverview
from DataPlot import DataPlot


class MainWindow(QMainWindow, Ui_MainWindow, QtCore.QObject):
    def __init__(self,parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.actionOpen.triggered.connect(self.on_actionOpen)
        self.dataOverview = ""
        self.MainTabWidget.clear()

    def on_actionOpen(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                  "CSV files (*.csv)", options=options)
        if fileName:
            self.dataOverview = DataOverview(fileName)
            self.MainTabWidget.addTab(self.dataOverview.getDataTable(),self.dataOverview.getData().getFilename())
            dataPlot = DataPlot(self.dataOverview.getData())
            self.MainTabWidget.addTab(dataPlot,'Plot')


# create the GUI application
app = QApplication(sys.argv)
# instantiate the main window
dmw = MainWindow()
# show it
dmw.showMaximized()
# start the Qt main loop execution, exiting from this script
# with the same return code of Qt application
sys.exit(app.exec_())
