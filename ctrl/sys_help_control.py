import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QCloseEvent

sys.path.append("..")

from view.sys_help import *

class Sys_help(Ui_syshelp):
    def setupUi(self, syshelp):
        self.dialog = syshelp
        Ui_syshelp.setupUi(self,syshelp)
        self.verify.clicked.connect(self.verify_f)

    def verify_f(self):
        self.dialog.close()

