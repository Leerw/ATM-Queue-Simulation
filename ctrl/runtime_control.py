import sys
sys.path.append("..")
from view.running_times import *
from ctrl.once_run_ctrl import *
from ctrl.repeat_control import *
class Runningtime(Ui_Dialog):
    def setupUi(self, Dialog):
        Ui_Dialog.setupUi(self,Dialog)
        self.RunOnce.clicked.connect(self.jump_to_once)
        self.RepeatedRun.clicked.connect(self.jump_to_repeat)
        self.Dialog = Dialog

    def jump_to_once(self):
       # self.Dialog.hide()
        form = QtWidgets.QDialog()
        ui = OnceRunCtrl()
        ui.setupUi(form)
        ui.set_function()
        ui.get_data(self.num,self.max,self.min,self.probabilities)
        form.show()
        form.exec()
       # self.Dialog.show()

    def jump_to_repeat(self):
        form = QtWidgets.QDialog()
        ui = RepeatControl()
        ui.setupUi(form)
        ui.setup_function(form)
        ui.get_data(self.num, self.max, self.min, self.probabilities)
        form.show()
        form.exec()
        self.Dialog.show()

    def get_data(self, num, max, min, probabilities):
        self.num = num
        self.max = max
        self.min = min
        self.probabilities = probabilities
