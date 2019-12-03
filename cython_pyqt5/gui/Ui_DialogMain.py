# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_DialogMain.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogMain(object):
    def setupUi(self, DialogMain):
        DialogMain.setObjectName("DialogMain")
        DialogMain.resize(785, 413)
        self.gridLayout = QtWidgets.QGridLayout(DialogMain)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit = QtWidgets.QTextEdit(DialogMain)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(DialogMain)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(DialogMain)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(DialogMain)
        QtCore.QMetaObject.connectSlotsByName(DialogMain)

    def retranslateUi(self, DialogMain):
        _translate = QtCore.QCoreApplication.translate
        DialogMain.setWindowTitle(_translate("DialogMain", "PyQt5 + Cython Demo"))
        self.pushButton.setText(_translate("DialogMain", "PushButton"))
