# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sys_help.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_syshelp(object):
    def setupUi(self, syshelp):
        syshelp.setObjectName("syshelp")
        syshelp.resize(400, 300)
        self.label = QtWidgets.QLabel(syshelp)
        self.label.setGeometry(QtCore.QRect(10, -20, 391, 241))
        self.label.setObjectName("label")
        self.verify = QtWidgets.QPushButton(syshelp)
        self.verify.setGeometry(QtCore.QRect(140, 230, 93, 28))
        self.verify.setObjectName("verify")

        self.retranslateUi(syshelp)
        QtCore.QMetaObject.connectSlotsByName(syshelp)

    def retranslateUi(self, syshelp):
        _translate = QtCore.QCoreApplication.translate
        syshelp.setWindowTitle(_translate("syshelp", "帮助"))
        self.label.setText(_translate("syshelp", "<html><head/><body><p>数据要求如下:</p><p>概率p：0&lt;= p &lt;=1 p为保留一位的小数，6个概率p之和为1</p><p>到达间隔时间最小值min：min &gt;= 0</p><p>到达间隔时间最小值max：max &gt;= 0 且 max &gt; min</p><p>人数num： num &gt; 0</p></body></html>"))
        self.verify.setText(_translate("syshelp", "确定"))

