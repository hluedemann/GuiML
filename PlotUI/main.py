from __future__ import with_statement
import numpy as np
import matplotlib.pyplot as plt
import sys
from PyQt5 import QtCore
from PyQt5.QtCore import QRect, pyqtSignal
from PyQt5 import QtGui
from PlotUI import Ui_PlotUIWindow
from PGraph import Ui_PGraph
from OpenDialog import Ui_Dialog
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QColorDialog, QWidget

class DesignerMainWindow(QMainWindow, Ui_PlotUIWindow,QtCore.QObject):
    def __init__(self,parent=None):
        super(DesignerMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.tabWidget.clear()
        self.actionOpen.triggered.connect(self.on_actionOpen)
        self.applyButton.clicked.connect(self.on_apply)
        self.actionSave.triggered.connect(self.on_actionSave)
        self.actionSaveAs.triggered.connect(self.on_actionSaveAs)
        self.fileSaveName = ""
        self.graphDictionary = {}
        self.tabCount = 0
        self.openDialog = ""


    def on_actionOpen(self):
        self.openDialog = OpenDialog()
        self.openDialog.show()
        self.openDialog.drawSignal.connect(self.on_draw)

    def on_draw(self,fileName,name):
        graph = PGraph(fileName)
        self.tabWidget.addTab(graph,name)
        self.graphDictionary[self.tabCount] = graph
        self.plot()
        self.tabCount += 1

    def plot(self):
        for val in self.graphDictionary.values():
            x, y = np.loadtxt(val.file).T
            if val.plotStyleColor:
                self.mpl.canvas.ax.plot(x, y, color=val.plotStyleColor,label=val.label)
            else:
                self.mpl.canvas.ax.plot(x, y,label=val.label)
        if self.x_label:
            self.mpl.canvas.ax.set_xlabel(self.x_lineEdit.text())
        if self.y_label:
            self.mpl.canvas.ax.set_ylabel(self.y_lineEdit.text())
        if self.legendCheckBox.isChecked() == True:
            self.mpl.canvas.ax.legend(loc='best')
        self.mpl.canvas.draw()

    def on_apply(self):
        self.mpl.canvas.ax.clear()
        self.plot()

    def on_save(self):
        if self.fileSaveName:
            self.mpl.canvas.fig.savefig(self.fileSaveName)
        else:
            self.on_actionSaveAs()

    def on_actionSave(self):
        self.on_save()

    def on_actionSaveAs(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Images (*.png *.jpg)", options=options)
        if fileName:
            self.fileSaveName = fileName
            self.mpl.canvas.fig.savefig(self.fileSaveName)

    def on_color(self):
        color = QColorDialog.getColor()
        self.plotStyleColor = tuple(t/255 for t in color.getRgb())

class PGraph(QWidget,Ui_PGraph,QtCore.QObject):
    def __init__(self, fileName, parent=None):
        super(PGraph,self).__init__(parent)
        self.setupUi(self)
        self.file = fileName
        self.plotStyleColor = ""
        self.selectedColorButton.setEnabled(False)
        self.colorButton.clicked.connect(self.on_color)
        self.label = "label"

    def on_color(self):
        color = QColorDialog.getColor()
        self.selectedColorButton.setStyleSheet("background-color: " + color.name())
        self.plotStyleColor = tuple(t/255 for t in color.getRgb())

    def setPlotStyleColor(self, color):
        self.plotStyleColor = color


class OpenDialog(QWidget,Ui_Dialog,QtCore.QObject):
    drawSignal = pyqtSignal(str,str)

    def __init__(self,parent=None):
        super(OpenDialog,self).__init__(parent)
        self.setupUi(self)
        self.fileName = ""
        self.plotStyleColor = ""
        self.selectedColor.setEnabled(False)
        self.searchButton.clicked.connect(self.on_search)
        self.colorButton.clicked.connect(self.on_color)
        self.drawButton.clicked.connect(self.on_draw)



    def on_color(self):
        color = QColorDialog.getColor()
        self.selectedColor.setStyleSheet("background-color: " + color.name())
        self.plotStyleColor = tuple(t / 255 for t in color.getRgb())


    def on_search(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                    "Text files (*.txt)", options=options)
        if fileName:
            self.pathLineEdit.setText(fileName)
            self.fileName = fileName

    def on_draw(self):
        if self.nameLineEdit.text() != "":
            self.drawSignal.emit(self.fileName,self.nameLineEdit.text())
        else:
            self.drawSignal.emit(self.fileName,self.fileName)
        self.close()
















# create the GUI application
app = QApplication(sys.argv)
# instantiate the main window
dmw = DesignerMainWindow()
# show it
dmw.showMaximized()
# start the Qt main loop execution, exiting from this script
# with the same return code of Qt application
sys.exit(app.exec_())
