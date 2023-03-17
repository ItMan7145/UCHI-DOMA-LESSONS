from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel
from PyQt5.QtCore import Qt


# app = QApplication([])
# window = QWidget()
# window.setWindowTitle("My program")
# window.resize(500, 500)
# window.move(50, 50)
# window.setGeometry(100, 100, 500, 500)
# # setGeometry(коорд по х, коорд по у, ширина, высота)
#
# window.show()
# app.exec_()


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setGeometry(100, 100, 300, 450)
        self.setWindowTitle("My program")
        self.setMinimumSize(150, 150)
        self.turn = "X"

        self.initUI()
        self.show()

    def initUI(self):
        # self.setGeometry(100, 100, 500, 500)
        # self.setWindowTitle("My program")
        #
        # self.button = QPushButton('button', self)
        # self.button.move(50, 50)
        # self.button.resize(self.button.sizeHint())
        # self.button.setToolTip("This is ToolTip")

        self.buttons = [[QPushButton(self) for _ in range(3)] for _ in range(3)]
        x, y = 90, 90
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].setGeometry(20 + i * x, 20 + j * y, 80, 80)
                self.buttons[i][j].clicked.connect(self.click_button)

        self.label = QLabel('Make first move', self)
        # self.label.move(110, 300)
        # self.label.resize(30, 260)
        self.label.setGeometry(20, 290, 260, 40)
        self.label.setAlignment(Qt.AlignCenter)

        self.resetButton = QPushButton('reset', self)
        self.resetButton.setGeometry(20, 350, 260, 40)

    def click_button(self):
        button = self.sender()
        type(button)
        button.setText(self.turn)
        button.setEnabled(False)
        self.turn = "0" if self.turn == "X" else "X"
        self.label.setText(f'{self.turn}')

    # def is_finished(self):
    #     if self.buttons


if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    app.exec_()
