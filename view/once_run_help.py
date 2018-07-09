# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'once_run_help.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(150, 90, 72, 15))
        self.label.setObjectName("label")
        self.verifty = QtWidgets.QPushButton(Dialog)
        self.verifty.setGeometry(QtCore.QRect(130, 190, 93, 28))
        self.verifty.setObjectName("verifty")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "TextLabel"))
        self.verifty.setText(_translate("Dialog", "确定"))

