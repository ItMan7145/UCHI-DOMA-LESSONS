from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QAction, QStatusBar, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence, QCloseEvent


class MainWindow(QMainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.resize(400, 200)
        self.setWindowTitle("Our awesome app")
        self.label = QLabel("This is an app with menu toolbar", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.label)
        self._createMenu()

    def _createMenu(self) -> None:
        menubar = self.menuBar()

        fileMenu = menubar.addMenu(' &File')
        editMenu = menubar.addMenu(' &Edit')

        editMenu.addAction(QAction("Cut", self))
        newFile = QAction("New", self)

        save = QAction("Save", self)
        save.triggered.connect(self._save)
        save.setShortcut(QKeySequence('Ctrl+p'))
        save.setStatusTip('This is a save button')
        fileMenu.addAction(newFile)

        openRecent = fileMenu.addMenu('Open Recent')
        openRecent.addAction(QAction("File 1", self))
        openRecent.addAction(QAction("File 2", self))

        fileMenu.addSeparator()
        fileMenu.addAction(save)

        saveAs = QAction('Save As', self)
        saveAs.setStatusTip('This is a save as button')

        toolbar = self.addToolBar("My toolbar")
        toolbar.addAction(save)
        toolbar.addSeparator()
        toolbar.addAction(saveAs)

        self.setStatusBar(QStatusBar(self))

    def _save(self) -> None:
        print("Saved!!!")

    def closeEvent(self, event: QCloseEvent) -> None:
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
