import sys
from model.Model import *
from ctrl.Control import *
from view.View import *

class App():

    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.model = Model()
        self.ctrl = Control(self.model)
        self.view = View(self.model, self.ctrl)
        self.view.show()

if __name__ == '__main__':
    app = App(sys.argv)