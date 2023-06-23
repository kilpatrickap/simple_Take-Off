import os
import sys

from PyQt6 import QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QDialog
from MainGUI import Ui_MainWindow
from NewProject import NewProject_Dialog
from ProjectTreeWidget import Project_Widget
from TakeOffList import TakeOffList_Widget
from Tab_m import Tab_m_Widget
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

        # # Insert Tab_m2_Widget() class and add widget to tabWidget
        # self.tab_m_widget = Tab_m_Widget()
        # icon1 = QtGui.QIcon()  # Add button icon with relative path
        # image_path_to_icon1 = os.path.join(os.path.dirname(__file__), "images", "len.png")
        # icon1.addPixmap(QtGui.QPixmap(image_path_to_icon1), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        # self.tabWidget.addTab(self.tab_m_widget, icon1, "m2")


        # Create an instance of the TakeOffSheet_Widget() class
        self.takeOff_sheet_widget = TakeOffSheet_Widget()
        self.verticalLayout_1.addWidget(self.takeOff_sheet_widget)

        # Connect signal of new_project
        self.actionNew.triggered.connect(self.new_project)

        # Connect signal of edit
        self.takeOff_sheet_widget.pushButton_edit.clicked.connect(self.edit_msmt)

        # Create an instance of the Edit_Widget() class
        self.edit_dialog = Edit_Dialog()

    def new_project(self):  # When new is clicked, run a new project
        dialog = QDialog()
        ui = NewProject_Dialog()
        ui.setupUi(dialog)
        dialog.exec()

    def edit_msmt(self):    # When edit is clicked in TakeOffSheet, run this code.
        dialog = QDialog()
        ui = Edit_Dialog()
        ui.setupUi(dialog)

        # Access the entered_code from TakeOffSheet_Widget() class
        entered_code = self.takeOff_sheet_widget.lineEdit_code.text()
        print(entered_code)

        # # Make the entered_code accessible to Edit_Dialog()
        # edit_dialog_label_code = self.edit_dialog.label_code.text()
        # print(edit_dialog_label_code)

        dialog.exec()

        return entered_code
