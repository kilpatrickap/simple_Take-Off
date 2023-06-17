from PyQt6.QtWidgets import QMainWindow
from MainGUI import Ui_MainWindow


class TakeOffSystem(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()