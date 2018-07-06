# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RunningTimes.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(560, 392)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(110, 100, 331, 31))
        self.label.setObjectName("label")
        self.RunOnce = QtWidgets.QPushButton(Dialog)
        self.RunOnce.setGeometry(QtCore.QRect(140, 220, 93, 28))
        self.RunOnce.setObjectName("RunOnce")
        self.RepeatedRun = QtWidgets.QPushButton(Dialog)
        self.RepeatedRun.setGeometry(QtCore.QRect(310, 220, 93, 28))
        self.RepeatedRun.setObjectName("RepeatedRun")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "选择运行次数"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">数据检查正确，请选择运行次数：</span></p></body></html>"))
        self.RunOnce.setText(_translate("Dialog", "运行一次"))
        self.RepeatedRun.setText(_translate("Dialog", "重复实验"))

