import sys
from PyQt6.QtWidgets import QMainWindow, QDialog
from MainGUI import Ui_MainWindow
from NewProject import NewProject_Dialog
from ProjectTreeWidget import Project_Widget
from TakeOffList import TakeOffList_Widget
from Tab_m import Tab_m_Widget


class TakeOffSystem(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        # Insert Project_Widget() class and add widget
        self.projectWidgetTree = Project_Widget()
        self.horizontalLayout_2.addWidget(self.projectWidgetTree)

        # Insert TakeOffList_Widget() class and add widget
        self.takeOffListWidget = TakeOffList_Widget()
        self.horizontalLayout_2.addWidget(self.takeOffListWidget)

        # Insert Tab_m_Widget() class and add widget
        self.tab_m_widget = Tab_m_Widget()
        # self.tab_m_widget.show()

        # Connect signal of new_project
        self.actionNew.triggered.connect(self.new_project)

    def new_project(self):  # When new is clicked, run a new project
        dialog = QDialog()
        ui = NewProject_Dialog()
        ui.setupUi(dialog)
        dialog.exec()
