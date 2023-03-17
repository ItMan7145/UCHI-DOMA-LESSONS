from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QVBoxLayout, QHBoxLayout, QLabel, QListWidget, QLineEdit
import sqlite3
import sys


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setGeometry(100, 100, 300, 450)
        self.setWindowTitle("My program")
        self.setMinimumSize(150, 150)

        self.btn_all_tasks = QPushButton("btn_all_tasks", self)
        self.btn_active_tasks = QPushButton("btn_active_tasks", self)
        self.btn_compiled_tasks = QPushButton("btn_compiled_tasks", self)
        # button1.setGeometry(100, 100, 100, 40)
        # button1.clicked.connect(self.click_button)

        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()
        self.hbox_2 = QHBoxLayout()

        self.label = QLabel("Список задач", self)
        self.label_task_name = QLabel("Название задачи", self)
        self.line_task_name = QLineEdit()
        self.task_list = QListWidget()

        self.setStructure()
        self.show()

    def click_button(self):
        self.btn_all_tasks.clicked.connect()
        self.btn_active_tasks.clicked.connect()
        self.btn_compiled_tasks.clicked.connect()

    def setStructure(self):
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.task_list)

        self.hbox.addWidget(self.btn_all_tasks)
        self.hbox.addWidget(self.btn_active_tasks)
        self.hbox.addWidget(self.btn_compiled_tasks)
        self.vbox.addLayout(self.hbox)

        self.hbox_2.addWidget(self.label_task_name)
        self.hbox_2.addWidget(self.line_task_name)
        self.vbox.addLayout(self.hbox_2)

        self.setLayout(self.vbox)


if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    app.exec_()
