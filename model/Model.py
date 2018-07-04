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
        # arrive_time[i] = sum(interval_time[0..i-1])
        for i in range(0, )
        pass

    def data_pool(self):
        return {self.arrive_time, self.interval_time,
                self.serve_time, self.serve_start_time,
                self.wait_time, self.serve_end_time,
                self.spend_time, self.sys_free_time,
                self.avg_wait_time, self.sys_util}

    def connect_db(self):
        return pymysql.connect(host='127.0.0.1',
                               port=3306,
                               user='root',
                               password='Qaz520..',
                               database='xxq',
                               charset='utf8')
