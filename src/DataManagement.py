import pandas as pd
import numpy as np
import os

from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QHeaderView, QAbstractScrollArea

from DataTable import Ui_DataTable

class Data():
    def __init__(self,m_filepath):
        self.m_filepath = m_filepath
        self.m_filename = os.path.basename(self.m_filepath)
        self.m_dataFrame = pd.read_csv(m_filepath)
        self.m_description = self.m_dataFrame.describe(include='all')

    def getFilename(self):
        return self.m_filename

    def getIndexes(self):
        return self.m_dataFrame.index

    def getColumns(self):
        return self.m_dataFrame.columns

    def getDataFrame(self):
        return self.m_dataFrame

    def getDescription(self):
        return self.m_description

class DataTable(QWidget,Ui_DataTable,QtCore.QObject):
    def __init__(self,parent=None):
        super(DataTable,self).__init__(parent)
        self.setupUi(self)
        self.tableData.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableDataDescription.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableDataDescription.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

class DataTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data, parent=None):
        QtCore.QAbstractTableModel.__init__(self,parent)
        self.m_data = data

    def rowCount(self, parent=None):
        return self.m_data.getIndexes().size

    def columnCount(self, parent=None):
        return self.m_data.getColumns().size

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole:
                return str(self.m_data.getDataFrame().iloc[index.row(),index.column()])

        return None

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.m_data.getColumns()[col]
        return None

class DataDescriptionModel(QtCore.QAbstractTableModel):
    def __init__(self, data, parent=None):
        QtCore.QAbstractTableModel.__init__(self,parent)
        self.m_data = data
        self.m_header = np.array(['Description'])
        self.m_header = np.append(self.m_header, self.m_data.getDescription().columns)

    def rowCount(self, parent=None):
        return self.m_data.getDescription().index.size

    def columnCount(self, parent=None):
        return self.m_data.getDescription().columns.size + 1

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole:
                if index.column() != 0:
                    return str(self.m_data.getDescription().iloc[index.row(),index.column()-1])
                else:
                    return str(self.m_data.getDescription().index[index.row()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.m_header[col]
        return None




class DataOverview():
    def __init__(self,m_filepath):
        self.m_data = Data(m_filepath)
        self.setupTable()

    def setupTable(self):
        self.m_dataTable = DataTable()
        self.m_dataTableModel = DataTableModel(self.m_data)
        self.m_dataDescriptionModel = DataDescriptionModel(self.m_data)
        self.m_proxyModel = QtCore.QSortFilterProxyModel()
        self.m_proxyModel.setSourceModel(self.m_dataTableModel)
        self.m_dataTable.tableData.setModel(self.m_proxyModel)
        self.m_dataTable.tableData.setSortingEnabled(True)
        for column in self.m_data.getColumns():
            self.m_dataTable.comboBoxFeature.addItem(column)
        self.m_dataTable.lineEditFilter.textChanged.connect(self.on_lineEditFilterChanged)
        self.m_dataTable.tableDataDescription.setModel(self.m_dataDescriptionModel)

    def on_lineEditFilterChanged(self,string):
        self.m_proxyModel.setFilterRegExp(QtCore.QRegExp(string,QtCore.Qt.CaseInsensitive, QtCore.QRegExp.FixedString))
        self.m_proxyModel.setFilterKeyColumn(self.m_dataTable.comboBoxFeature.currentIndex())

    def getDataTable(self):
        return self.m_dataTable

    def getData(self):
        return self.m_data



