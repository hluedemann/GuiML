# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OpenDialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.pathLineEdit = QtWidgets.QLineEdit(Dialog)
        self.pathLineEdit.setObjectName("pathLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.pathLineEdit)
        self.searchButton = QtWidgets.QPushButton(Dialog)
        self.searchButton.setObjectName("searchButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.searchButton)
        self.selectedColor = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectedColor.sizePolicy().hasHeightForWidth())
        self.selectedColor.setSizePolicy(sizePolicy)
        self.selectedColor.setMinimumSize(QtCore.QSize(145, 0))
        self.selectedColor.setText("")
        self.selectedColor.setObjectName("selectedColor")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.selectedColor)
        self.colorButton = QtWidgets.QPushButton(Dialog)
        self.colorButton.setObjectName("colorButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.colorButton)
        self.nameLineEdit = QtWidgets.QLineEdit(Dialog)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.nameLineEdit)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label)
        self.verticalLayout.addLayout(self.formLayout)
        self.drawButton = QtWidgets.QPushButton(Dialog)
        self.drawButton.setObjectName("drawButton")
        self.verticalLayout.addWidget(self.drawButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.searchButton.setText(_translate("Dialog", "Search"))
        self.colorButton.setText(_translate("Dialog", "Color"))
        self.label.setText(_translate("Dialog", "Name"))
        self.drawButton.setText(_translate("Dialog", "Draw"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

