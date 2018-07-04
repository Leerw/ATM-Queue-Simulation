import mysql
import pymysql

class Model:

    def __init__(self):
        self.arrive_time = []
        self.interval_time = []
        self.serve_time = []
        self.serve_start_time = []
        self.wait_time = []
        self.serve_end_time = []
        self.spend_time = []
        self.sys_free_time = []
        self.avg_wait_time = []
        self.sys_util = 0
        self.run_time = 0
        pass

    def data_gen(self):
        pass

    def result_cal(self, times):
        pass

    