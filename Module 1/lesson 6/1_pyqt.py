from PyQt5.QtWidgets import QApplication, QAction, QMainWindow


class AnotherWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('New file')
        self.setGeometry(150, 150, 350, 450)
        # self.show()


class Window(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setGeometry(100, 100, 300, 450)
        self.setWindowTitle("My program")
        self.setMinimumSize(150, 150)

        self._createMenu()
        # self.initUI()
        self.show()

    def _createMenu(self) -> None:
        menubar = self.menuBar()
        file_menu = menubar.addMenu(' &File')
        edit_menu = menubar.addMenu(' &Edit')
        edit_menu.addAction(QAction('Cut', self))

        save = QAction("Save", self)
        save.triggered.connect(self._saveFile)

        new_file = QAction("New file", self)
        new_file.triggered.connect(self.showAnotherWindow)
        open_recent = file_menu.addMenu('Open Recent')
        open_recent.addAction(QAction("File 1", self))
        open_recent.addAction(QAction("File 2", self))

        file_menu.addAction(save)
        file_menu.addSeparator()
        file_menu.addAction(new_file)

        toolbar = self.addToolBar("Toolbar")
        toolbar.addAction(save)
        toolbar.addSeparator()
        toolbar.addAction(QAction('Save as', self))

    def _saveFile(self):
        print("Saved")

    def showAnotherWindow(self) -> None:
        self.anotherWindow = AnotherWindow()
        self.anotherWindow.show()


if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    app.exec_()
