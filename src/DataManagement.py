import pandas as pd
import numpy as np
import os

from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget

from DataTable import Ui_DataTable

class Data():
    def __init__(self,m_filepath):
        self.m_filepath = m_filepath
        self.m_filename = os.path.basename(self.m_filepath)
        self.m_dataFrame = pd.read_csv(m_filepath)
        print (self.m_dataFrame.head())

    def getFilename(self):
        return self.m_filename

    def getIndexes(self):
        return self.m_dataFrame.index

    def getColumns(self):
        return self.m_dataFrame.columns

    def getDataFrame(self):
        return self.m_dataFrame

class DataTable(QWidget,Ui_DataTable,QtCore.QObject):
    def __init__(self,parent=None):
        super(DataTable,self).__init__(parent)
        self.setupUi(self)

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




class DataOverview():
    def __init__(self,m_filepath):
        self.m_data = Data(m_filepath)
        self.m_dataTable = DataTable()
        self.m_dataTableModel = DataTableModel(self.m_data)
        self.m_dataTable.tableData.setModel(self.m_dataTableModel)


    def getDataTable(self):
        return self.m_dataTable

    def getData(self):
        return self.m_data



