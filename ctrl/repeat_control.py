from view.repeat_run import *
from model.Model import *
from PyQt5.QtWidgets import QTableWidgetItem, QDialog
import numpy as np


class RepeatControl(Ui_RepeatRun):

    def __init__(self):
        self.model = Model()
        self.repeat_time = 0
        self.num_people = 0
        self.max = 0
        self.min = 0
        self.probabilities = []

    def setup_function(self, Dialog):
        self.Verify.clicked.connect(self.verify)
        self.Reset.clicked.connect(self.reset)
        self.Finish.clicked.connect(self.finish)
        self.Help.clicked.connect(self.help)

    def get_data(self, num_people, max, min, probabilities):
        self.num_people = int(num_people)
        self.max = int(max)
        self.min = int(min)
        self.probabilities = probabilities


    def verify(self):
        """
        Calculate all results and show all the result in the two widgets at top-left and bottom
        :return:
        """
        self.reset()
        self.repeat_time = int(self.Repetitions.text())
        # r is result for each calculate
        # [self.interval_time, self.arrive_time,
        #  self.serve_time, self.serve_start_time,
        #  self.wait_time, self.serve_end_time,
        #  self.spend_time, self.sys_free_time,
        #  self.avg_wait_time, self.sys_util]
        r = []
        lab_avg = {}
        lab_result = {}
        for time in range(1, self.repeat_time + 1):
            self.model.data_gen(self.num_people, self.max, self.min, self.probabilities)
            self.model.result_cal(self.num_people)
            r = self.model.data_pool()
            lab_avg[time] = r[-2]
            lab_result[time] = r
        lab_avg_keys = lab_avg.keys()
        lab_avg_values = lab_avg.values()
        lab_final_result = lab_result[self.repeat_time]
        final_avg = np.mean(lab_avg_values)
        final_min = np.min(lab_avg_values)
        final_max = np.max(lab_avg_values)
        # show the results
        # insert [lab_avg_keys, lab_avg_values] into tableWidget_avg_wait
        # insert lab_final_result into tableWidget_last_result
        # show final_avg in AverageDate
        # show final_min in MinData
        # show final_max in MaxData
        
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
