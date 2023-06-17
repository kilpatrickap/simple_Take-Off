import sys
from PyQt6.QtWidgets import QApplication
from TakeOffSystem import TakeOffSystem

app = QApplication(sys.argv)

takeOff = TakeOffSystem()

sys.exit(app.exec())