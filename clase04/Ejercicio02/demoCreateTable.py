# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoCreateTable.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(583, 526)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setObjectName("label_1")
        self.verticalLayout.addWidget(self.label_1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEditDBName = QtWidgets.QLineEdit(Dialog)
        self.lineEditDBName.setObjectName("lineEditDBName")
        self.verticalLayout_2.addWidget(self.lineEditDBName)
        self.lineEditTableName = QtWidgets.QLineEdit(Dialog)
        self.lineEditTableName.setObjectName("lineEditTableName")
        self.verticalLayout_2.addWidget(self.lineEditTableName)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.lineEditColumnName = QtWidgets.QLineEdit(Dialog)
        self.lineEditColumnName.setObjectName("lineEditColumnName")
        self.verticalLayout_3.addWidget(self.lineEditColumnName)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.comboBoxDataType = QtWidgets.QComboBox(Dialog)
        self.comboBoxDataType.setObjectName("comboBoxDataType")
        self.verticalLayout_4.addWidget(self.comboBoxDataType)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.pushButtonAddColumn = QtWidgets.QPushButton(Dialog)
        self.pushButtonAddColumn.setMinimumSize(QtCore.QSize(150, 150))
        self.pushButtonAddColumn.setObjectName("pushButtonAddColumn")
        self.horizontalLayout_2.addWidget(self.pushButtonAddColumn)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.pushButtonCreateTable = QtWidgets.QPushButton(Dialog)
        self.pushButtonCreateTable.setObjectName("pushButtonCreateTable")
        self.gridLayout.addWidget(self.pushButtonCreateTable, 2, 0, 1, 1)
        self.labelResponse = QtWidgets.QLabel(Dialog)
        self.labelResponse.setMaximumSize(QtCore.QSize(16777215, 200))
        self.labelResponse.setStyleSheet("background-color: rgb(173, 127, 168);")
        self.labelResponse.setText("")
        self.labelResponse.setObjectName("labelResponse")
        self.gridLayout.addWidget(self.labelResponse, 3, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Creador de tablas de bases de datos"))
        self.label_2.setText(_translate("Dialog", "Ingresar nombre de la tabla"))
        self.label_1.setText(_translate("Dialog", "Ingresar nombre de la base de datos:"))
        self.label_3.setText(_translate("Dialog", "Nombre de la columna"))
        self.label_4.setText(_translate("Dialog", "Tipo de dato"))
        self.pushButtonAddColumn.setText(_translate("Dialog", "Agregar columna"))
        self.pushButtonCreateTable.setText(_translate("Dialog", "Insertar tabla"))
