from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class Window(QWidget):
    def __init__(self) -> None:
        self.i = 0

        super().__init__()
        self.setGeometry(100, 100, 300, 450)
        self.setWindowTitle("My program")
        self.setMinimumSize(150, 150)

        button1 = QPushButton("Btn", self)
        button1.setGeometry(100, 100, 100, 40)
        button1.clicked.connect(self.click_button)

        button2 = QPushButton("Btn", self)
        button2.setGeometry(100, 200, 100, 40)
        button2.clicked.connect(self.click_button)

        button3 = QPushButton("Btn", self)
        button3.setGeometry(100, 300, 100, 40)
        button3.clicked.connect(self.click_button)

        self.show()

    def click_button(self):
        self.i += 1
        print(self.i)


if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    app.exec_()
