from PyQt5.QtWidgets import QTableWidgetItem, QDialog
from view.once_run_view import Ui_OnceRun


class OnceRunCtrl(Ui_OnceRun):
    def set_function(self):
        self.clr_cache_btn.clicked.connect(self.clr_cache)
        self.finish_btn.clicked.connect(self.finish)
        self.once_run_btn.clicked.connect(self.once_run)
        self.help_btn.clicked.connect(self.help)

    def clr_cache(self):
        self.once_run_table.clearContents()

    def finish(self):
        self.close()
        exit(0)

    def once_run(self):
        col_count = self.once_run_table.columnCount()
        for i in range(col_count):
            item = QTableWidgetItem()
            item.setText("111")
            self.once_run_table.setItem(0, i, item)
        self.avg_txt.setText("111")
        self.sys_use_txt.setText("111")

    def help(self):
        d = QDialog()
        d.show()

        d.exec_()
