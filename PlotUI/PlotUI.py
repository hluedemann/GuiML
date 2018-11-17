# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PlotUI.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PlotUIWindow(object):
    def setupUi(self, PlotUIWindow):
        PlotUIWindow.setObjectName("PlotUIWindow")
        PlotUIWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(PlotUIWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.x_label = QtWidgets.QLabel(self.centralwidget)
        self.x_label.setObjectName("x_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.x_label)
        self.y_label = QtWidgets.QLabel(self.centralwidget)
        self.y_label.setObjectName("y_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.y_label)
        self.x_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.x_lineEdit.setObjectName("x_lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.x_lineEdit)
        self.y_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.y_lineEdit.setObjectName("y_lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.y_lineEdit)
        self.applyButton = QtWidgets.QPushButton(self.centralwidget)
        self.applyButton.setObjectName("applyButton")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.applyButton)
        self.legendCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.legendCheckBox.setObjectName("legendCheckBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.legendCheckBox)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.mpl = MatplotlibWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mpl.sizePolicy().hasHeightForWidth())
        self.mpl.setSizePolicy(sizePolicy)
        self.mpl.setObjectName("mpl")
        self.horizontalLayout_2.addWidget(self.mpl)
        PlotUIWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PlotUIWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        PlotUIWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PlotUIWindow)
        self.statusbar.setObjectName("statusbar")
        PlotUIWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(PlotUIWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(PlotUIWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSaveAs = QtWidgets.QAction(PlotUIWindow)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(PlotUIWindow)
        QtCore.QMetaObject.connectSlotsByName(PlotUIWindow)

    def retranslateUi(self, PlotUIWindow):
        _translate = QtCore.QCoreApplication.translate
        PlotUIWindow.setWindowTitle(_translate("PlotUIWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("PlotUIWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("PlotUIWindow", "Tab 2"))
        self.x_label.setText(_translate("PlotUIWindow", "X-Achse"))
        self.y_label.setText(_translate("PlotUIWindow", "Y-Achse"))
        self.applyButton.setText(_translate("PlotUIWindow", "Apply"))
        self.legendCheckBox.setText(_translate("PlotUIWindow", "Legend"))
        self.menuFile.setTitle(_translate("PlotUIWindow", "File"))
        self.actionOpen.setText(_translate("PlotUIWindow", "Open..."))
        self.actionSave.setText(_translate("PlotUIWindow", "Save"))
        self.actionSaveAs.setText(_translate("PlotUIWindow", "Save AS.."))

from matplotlibWidget import MatplotlibWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PlotUIWindow = QtWidgets.QMainWindow()
    ui = Ui_PlotUIWindow()
    ui.setupUi(PlotUIWindow)
    PlotUIWindow.show()
    sys.exit(app.exec_())

