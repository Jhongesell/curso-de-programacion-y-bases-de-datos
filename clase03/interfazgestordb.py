# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfazgestordb.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(483, 529)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setStyleSheet("background-color: rgb(138, 226, 52);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEditDBName = QtWidgets.QLineEdit(Dialog)
        self.lineEditDBName.setObjectName("lineEditDBName")
        self.verticalLayout.addWidget(self.lineEditDBName)
        self.pushButtonCreateDB = QtWidgets.QPushButton(Dialog)
        self.pushButtonCreateDB.setObjectName("pushButtonCreateDB")
        self.verticalLayout.addWidget(self.pushButtonCreateDB)
        self.labelResponse = QtWidgets.QLabel(Dialog)
        self.labelResponse.setStyleSheet("background-color: rgb(173, 127, 168);")
        self.labelResponse.setText("")
        self.labelResponse.setObjectName("labelResponse")
        self.verticalLayout.addWidget(self.labelResponse)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Creador de bases de datos"))
        self.label.setText(_translate("Dialog", "Ingrese nombre de la base de datos:"))
        self.pushButtonCreateDB.setText(_translate("Dialog", "Crear base de datos"))
