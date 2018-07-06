import sys
sys.path.append("..")
from model.Model import *
from view.once_run_view import *
from view.repeat_run import *
from view.systemdatasetting import *

class Systemdatasetting(Ui_QDialog):
    def setupUi(self, QDialog2):
        Ui_QDialog.setupUi(self,QDialog2)
        self.DateInspection.clicked.connect(self.data_check_f)
        self.Reset_1.clicked.connect(self.Reset_f)
        self.Help.clicked.connect(self.Help_f)
        self.Cancel.clicked.connect(self.Cancel_f)

    def data_check_f(self):
        probability_data = [self.PCusSer1.text(), self.PCusSer2.text(), self.PCusSer3.text(),
                            self.PCusSer4.text(), self.PCusSer5.text(), self.PCusSer6.text()]
        num_people = self.NumOfPeo.text()
        time_max = self.arrive_timemax.text()
        time_min = self.arrive_timemin.text()
        # 正则表达式判断是否是浮点数
        value = re.compile(r'^[-+]?[0-9]+\.[0-9]+$')
        result = True

        for i in range(0, 6):
            tmp = value.match(probability_data[i])
            if tmp == False:
                result = False
                break
            else:
                probability_data[i] = float(probability_data[i])

        if result != False:
            for i in [time_min, time_max, num_people]:
                tmp = value.match(i)
                if tmp == False:
                    result = False
                    break

        time_max = float(time_max)
        time_min = float(time_min)
        num_people = float(num_people)

        if self.model1.data_check(probability_data, time_max, time_min, num_people) == False or result == False:
            reply = QMessageBox.warning(self,  # 使用infomation信息框
                                        "警告",
                                        "数据输入有误",
                                        QMessageBox.Cancel)
            # pass
        else:
            self.probailities_data = probability_data
            self.time_min = time_min
            self.time_max = time_max
            self.num_people = num_people

    def Help_f(self):
        pass

    def Reset_f(self):
        self.PCusSer1.setText(str(0.1))
        self.PCusSer2.setText(str(0.1))
        self.PCusSer3.setText("0.2")
        self.PCusSer4.setText("0.2")
        self.PCusSer5.setText("0.2")
        self.PCusSer6.setText("0.2")

        self.CPCusSer1.setText("0.1")
        self.CPCusSer2.setText("0.2")
        self.CPCusSer3.setText("0.4")
        self.CPCusSer4.setText("0.6")
        self.CPCusSer5.setText("0.8")
        self.CPCusSer6.setText("1.0")

        self.arrive_timemax.setText("12")
        self.arrive_timemin.setText("2")

        self.NumOfPeo.setText("10")

        self.data_check_f()

    def Cancel_f(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Systemdatasetting()
    ui.setupUi(Form)

    Form.show()
    sys.exit(app.exec())
