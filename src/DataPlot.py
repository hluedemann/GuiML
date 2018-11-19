import numpy as np
import matplotlib.pyplot as plt

from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget

from DataPlotWidget import Ui_DataPlotWidget

class DataPlot(QWidget, Ui_DataPlotWidget, QtCore.QObject):
    def __init__(self,data,parent=None):
        super(DataPlot,self).__init__(parent)
        self.setupUi(self)
        self.m_data = data
        self.pushButtonPlot.released.connect(self.on_pushButtonPlotTriggered)
        self.m_plotStyles = ['Density', 'Scatter']
        self.m_plotStyle = self.m_plotStyles[0]
        for style in self.m_plotStyles:
            self.comboBoxOption.addItem(style)
        self.comboBoxOption.highlighted.connect(self.on_comboBoxOptionHighlighted)

    def on_pushButtonPlotTriggered(self):
        plt.clf()
        self.axes = self.matplotlibWidget.canvas.fig.add_subplot(111)
        self.axes.plot([1,2],[1,3])
        self.matplotlibWidget.canvas.draw()
        print (self.m_plotStyle)

    def on_comboBoxOptionHighlighted(self,style):
        self.m_plotStyle = self.m_plotStyles[style]
