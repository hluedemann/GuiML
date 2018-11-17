# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PGraph.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PGraph(object):
    def setupUi(self, PGraph):
        PGraph.setObjectName("PGraph")
        PGraph.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(PGraph)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.colorButton = QtWidgets.QPushButton(PGraph)
        self.colorButton.setObjectName("colorButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.colorButton)
        self.selectedColorButton = QtWidgets.QPushButton(PGraph)
        self.selectedColorButton.setText("")
        self.selectedColorButton.setObjectName("selectedColorButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.selectedColorButton)
        self.labelLineEdit = QtWidgets.QLineEdit(PGraph)
        self.labelLineEdit.setObjectName("labelLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelLineEdit)
        self.labelLabel = QtWidgets.QLabel(PGraph)
        self.labelLabel.setObjectName("labelLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.labelLabel)
        self.verticalLayout.addLayout(self.formLayout)

        self.retranslateUi(PGraph)
        QtCore.QMetaObject.connectSlotsByName(PGraph)

    def retranslateUi(self, PGraph):
        _translate = QtCore.QCoreApplication.translate
        PGraph.setWindowTitle(_translate("PGraph", "Form"))
        self.colorButton.setText(_translate("PGraph", "Color"))
        self.labelLabel.setText(_translate("PGraph", "Label"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PGraph = QtWidgets.QWidget()
    ui = Ui_PGraph()
    ui.setupUi(PGraph)
    PGraph.show()
    sys.exit(app.exec_())

