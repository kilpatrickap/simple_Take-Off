import os
import sys

from PyQt6 import QtGui, QtWidgets, QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QDialog
from MainGUI import Ui_MainWindow
from NewProject import NewProject_Dialog
from ProjectTreeWidget import Project_Widget
from TakeOffList import TakeOffList_Widget
from Tab_m import Tab_m_Widget
from Tab_nr import Tab_nr_Widget
from TakeOffSheet import TakeOffSheet_Widget
from Edit import Edit_Dialog

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

        # Insert Tab_m_Widget() class and add widget to tabWidget
        self.tab_m_widget = Tab_m_Widget()
        icon1 = QtGui.QIcon()  # Add button icon with relative path
        image_path_to_icon1 = os.path.join(os.path.dirname(__file__), "images", "len.png")
        icon1.addPixmap(QtGui.QPixmap(image_path_to_icon1), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tabWidget.addTab(self.tab_m_widget, icon1, "m")

        # Insert Tab_nr_Widget() class and add widget to tabWidget
        self.tab_nr_widget = Tab_nr_Widget()
        icon2 = QtGui.QIcon()  # Add button icon with relative path
        image_path_to_icon2 = os.path.join(os.path.dirname(__file__), "images", "nr.png")
        icon2.addPixmap(QtGui.QPixmap(image_path_to_icon2), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tabWidget.addTab(self.tab_nr_widget, icon2, "nr")


        # Create an instance of the TakeOffSheet_Widget() class
        self.takeOff_sheet_widget = TakeOffSheet_Widget()
        self.verticalLayout_1.addWidget(self.takeOff_sheet_widget)

        # Connect signal of new_project
        self.actionNew.triggered.connect(self.new_project)

        # Connect signal of edit
        self.takeOff_sheet_widget.pushButton_edit.clicked.connect(self.edit_msmt)

    def new_project(self):  # When new is clicked, run a new project
        dialog = QDialog()
        ui = NewProject_Dialog()
        ui.setupUi(dialog)
        dialog.exec()

    def edit_msmt(self):
        dialog = QDialog()

        # Set the window flags to make the dialog stay on top
        dialog.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)

        # entered_code is a class argument of the Edit_Dialog() class, extending from TakeOffSheet() class
        ui = Edit_Dialog(entered_code=self.takeOff_sheet_widget.lineEdit_code.text())

        ui.setupUi(dialog)
        dialog.exec()
