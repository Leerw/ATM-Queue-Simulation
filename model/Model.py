import random


import numpy as np



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
        self.avg_wait_time = 0
        self.sys_util = 0
        pass

    def data_gen(self, num, max, min, probabilities):
        #下面是生成到达时间的随机值
        tmp = True
        y = []
        lam = (max + min) / 2
        while (tmp):
            time_list = np.random.poisson(lam, size=num).tolist()
            for i in time_list:
                if (i > max or i < min):
                    time_list.remove(i)
            y = y + time_list
            if len(y) >= num:
                tmp = False

        if (len(y) > num):
            for i in range(num, len(y)):
                y.remove(i)

        y.sort()
        self.arrive_time = y

        #下面是生成服务时间的随机值
        seq = [1,2,3,4,5,6]
        while(len(self.serve_time)!=num):
            z = random.uniform(0, 1)
            cumprob = 0.0
            for item, item_pro in zip(seq, probabilities):
                cumprob += item_pro
                if z < cumprob:
                    break
            self.serve_time.append(item)





    def result_cal(self,num):
        #对第一次进行数据添加
        self.wait_time.append(0)
        self.serve_end_time.append(self.serve_time[0]+self.arrive_time[0])
        self.interval_time.append(0)
        self.serve_start_time.append(0)
        #对后面的进行数据添加
        for i in range(1,num):
            wait_time = self.serve_end_time[i- 1] - self.arrive_time[i]#等待时间=上一次的结束时间-到达时间
            if wait_time < 0:
                self.sys_free_time.append(wait_time)#等待时间如果为0，第i个顾客的系统空闲时间就不为0
                wait_time = 0
            else:
                self.sys_free_time.append(0)
            self.wait_time.append(wait_time)
            self.serve_end_time.append(self.arrive_time[i]+self.wait_time[i]+self
                                       .serve_time[i])#结束时间=等待时间+到达时间+服务时间
        wait_time = 0
        serve_time = self.serve_time[0]
        for i in range(1,num):
            self.serve_start_time.append(self.arrive_time[i]+ self.wait_time[i])#开始时间=到达时间+等待时间
            self.spend_time.append(self.wait_time[i]+self.serve_time[i])#花费时间 = 等待时间+服务时间
            self.interval_time.append(self.arrive_time[i] - self.arrive_time[i-1])#间隔时间 = 这次到达时间-上次到达时间
            wait_time = wait_time + self.wait_time[i]
            serve_time =serve_time + self.serve_time[i]
        self.avg_wait_time = wait_time / num  #系统平均等待时间是等待时间之和除以人数
        all_time = self.serve_end_time[num-1] - self.arrive_time[0] #系统总运行时间 = 最后一个人的结束时间 - 第一个人的到达时间
        self.sys_util = serve_time /all_time #系统利用率 = 系统服务总时间 / 系统总运行时间



    def data_pool(self):
        return {self.arrive_time, self.interval_time,
                self.serve_time, self.serve_start_time,
                self.wait_time, self.serve_end_time,
                self.spend_time, self.sys_free_time,
                self.avg_wait_time, self.sys_util}

    # def connect_db(self):
    #     return pymysql.connect(host='127.0.0.1',
    #                            port=3306,
    #                            user='root',
    #                            password='Qaz520..',
    #                            database='xxq',
    #                            charset='utf8')
