# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DataPlotWidget.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DataPlotWidget(object):
    def setupUi(self, DataPlotWidget):
        DataPlotWidget.setObjectName("DataPlotWidget")
        DataPlotWidget.resize(616, 478)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(DataPlotWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.matplotlibWidget = MatplotlibWidget(DataPlotWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.matplotlibWidget.sizePolicy().hasHeightForWidth())
        self.matplotlibWidget.setSizePolicy(sizePolicy)
        self.matplotlibWidget.setObjectName("matplotlibWidget")
        self.horizontalLayout.addWidget(self.matplotlibWidget)
        self.optionWidget = QtWidgets.QWidget(DataPlotWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.optionWidget.sizePolicy().hasHeightForWidth())
        self.optionWidget.setSizePolicy(sizePolicy)
        self.optionWidget.setObjectName("optionWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.optionWidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBoxOption = QtWidgets.QComboBox(self.optionWidget)
        self.comboBoxOption.setObjectName("comboBoxOption")
        self.verticalLayout.addWidget(self.comboBoxOption)
        self.currentOptionWidget = QtWidgets.QWidget(self.optionWidget)
        self.currentOptionWidget.setObjectName("currentOptionWidget")
        self.verticalLayout.addWidget(self.currentOptionWidget)
        self.pushButtonSave = QtWidgets.QPushButton(self.optionWidget)
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.verticalLayout.addWidget(self.pushButtonSave)
        self.pushButtonPlot = QtWidgets.QPushButton(self.optionWidget)
        self.pushButtonPlot.setObjectName("pushButtonPlot")
        self.verticalLayout.addWidget(self.pushButtonPlot)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout.addWidget(self.optionWidget)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(DataPlotWidget)
        QtCore.QMetaObject.connectSlotsByName(DataPlotWidget)

    def retranslateUi(self, DataPlotWidget):
        _translate = QtCore.QCoreApplication.translate
        DataPlotWidget.setWindowTitle(_translate("DataPlotWidget", "Form"))
        self.pushButtonSave.setText(_translate("DataPlotWidget", "Save"))
        self.pushButtonPlot.setText(_translate("DataPlotWidget", "Plot"))

from matplotlibWidget import MatplotlibWidget
