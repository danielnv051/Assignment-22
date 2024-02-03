import sys
from typing import Optional
from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from main_window import Ui_MainWindow
from database import Database


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db = Database()
        self.read_from_db()
        self.ui.pushButton.clicked.connect(self.new_task)

    def read_from_db(self):
        tasks = self.db.get_tasks()
        for i in range(len(tasks)):
            new_check_box = QCheckBox()
            new_label = QLabel()
            new_label_2 = QLabel()
            new_label.setText(tasks[i][1])
            new_label_2.setText(tasks[i][2])

            self.ui.gl_tasks.addWidget(new_check_box, i, 0)
            self.ui.gl_tasks.addWidget(new_label, i, 1)
            self.ui.gl_tasks.addWidget(new_label_2, i, 2)
            self.ui.tb_new_task.setText('')
            self.ui.tb_new_desc.setText('')

    def new_task(self): 
        msgbox = QMessageBox()
        new_title = self.ui.tb_new_task.text()
        new_desc = self.ui.tb_new_desc.toPlainText()
        feedback = self.db.add_new_task(new_title, new_desc)
        if feedback == True:
            self.read_from_db()
        else:
            msgbox.setText("مشکلی رخ داده است")
            msgbox.exec()
        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec()
