# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DataTable.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DataTable(object):
    def setupUi(self, DataTable):
        DataTable.setObjectName("DataTable")
        DataTable.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(DataTable)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableData = QtWidgets.QTableView(DataTable)
        self.tableData.setObjectName("tableData")
        self.verticalLayout.addWidget(self.tableData)
        self.tableDataDescription = QtWidgets.QTableView(DataTable)
        self.tableDataDescription.setObjectName("tableDataDescription")
        self.verticalLayout.addWidget(self.tableDataDescription)

        self.retranslateUi(DataTable)
        QtCore.QMetaObject.connectSlotsByName(DataTable)

    def retranslateUi(self, DataTable):
        _translate = QtCore.QCoreApplication.translate
        DataTable.setWindowTitle(_translate("DataTable", "Form"))
