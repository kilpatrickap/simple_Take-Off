import sys
from PyQt6.QtWidgets import QMainWindow, QDialog
from MainGUI import Ui_MainWindow
from NewProject import NewProject_Dialog


class TakeOffSystem(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.actionNew.triggered.connect(self.new_project)

    def new_project(self):
        dialog = QDialog()
        ui = NewProject_Dialog()

        ui.setupUi(dialog)
        dialog.exec()

        # sys.exit(dialog.exec())
