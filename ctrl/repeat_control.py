from view.repeat_run import *
from model.Model import *
from .sys_control import Systemdatasetting

class RepeatControl(Ui_RepeatRun):

    def __init__(self):
        self.model = Model()
        self.sys_settings = Systemdatasetting()
        self.repeat_time = 0
        self.num_people = 0

    def setupFun(self, Dialog):
        self.Verify.clicked.connect(self.verify())
        self.Reset.clicked.connect(self.reset())
        self.Finish.clicked.connect(self.finish())
        self.Help.clicked.connect(self.help())

    def verify(self):
        """
        Show all the result in the two widgets at top-left and bottom
        :return:
        """
        self.repeat_time = self.Repetitions.text()
        self.num_people = self.sys_settings.num_people

        pass

    def reset(self):
        """
        Clear all data and back to initial status
        :return:
        """
        pass

    def finish(self):
        """
        Close the window and turn off
        :return:
        """
        pass

    def help(self):
        """
        Show the manual help
        :return:
        """
        pass
