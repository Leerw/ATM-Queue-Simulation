from PyQt5.QtWidgets import QTableWidgetItem, QDialog
from view.once_run_view import Ui_OnceRun
from model.Model import Model


class OnceRunCtrl(Ui_OnceRun):
    def set_function(self):
        self.clr_cache_btn.clicked.connect(self.clr_cache)
        self.finish_btn.clicked.connect(self.finish)
        self.once_run_btn.clicked.connect(self.once_run)
        self.help_btn.clicked.connect(self.help)

    def clr_cache(self):
        while self.once_run_table.rowCount() != 0:
            self.once_run_table.removeRow(0)
        self.once_run_table.insertRow(0)
        item = QTableWidgetItem()
        item.setText("**")
        self.once_run_table.setVerticalHeaderItem(0, item)
        self.sys_use_txt.clear()
        self.avg_txt.clear()

    def finish(self):
        self.close()
        exit(0)

    def once_run(self):
        self.clr_cache()
        m = Model()
        m.data_gen(10, 5, 12, [0.1, 0.1, 0.2, 0.2, 0.2, 0.2])
        m.result_cal(10)
        r = m.data_pool()
        col_count = self.once_run_table.columnCount()
        self.once_run_table.removeRow(0)
        for j in range(len(r[0]) - 1):
            self.once_run_table.insertRow(j)
            item = QTableWidgetItem()
            item.setText(str(j + 1))
            self.once_run_table.setVerticalHeaderItem(j, item)
            item = QTableWidgetItem()
            item.setText(str(j + 1))
            self.once_run_table.setItem(j, 0, item)
            for i in range(1, col_count):
                item = QTableWidgetItem()
                item.setText(str(r[i - 1][j]))
                self.once_run_table.setItem(j, i, item)
        self.avg_txt.setText(str(r[8]))
        self.sys_use_txt.setText(str(r[9]))

    def help(self):
        d = QDialog()
        d.show()

        d.exec_()
