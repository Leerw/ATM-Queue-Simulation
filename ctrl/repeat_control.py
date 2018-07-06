from view.repeat_run import *
from model.Model import *

class RepeatControl(Ui_RepeatRun):

    def __init__(self):
        super.__init__()
        model = Model()

    def setupUi(self, Dialog):
        Ui_RepeatRun.setupUi(self, Dialog)
        self.Verify.clicked.connect(self.verify())
        self.Reset.clicked.connect(self.reset())
        self.Finish.clicked.connect(self.finish())
        self.Help.clicked.connect(self.help())

    def verify(self):
        """
        Show all the result in the two widgets at top-left and bottom
        :return:
        """
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
