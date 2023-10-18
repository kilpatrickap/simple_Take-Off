import json
import os
import sys
from PyQt6 import QtGui, QtWidgets, QtCore
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtGui import QDesktopServices
from PyQt6.QtWidgets import QMainWindow, QDialog
from MainGUI import Ui_MainWindow
from NewProject import NewProject_Dialog
from ProjectTreeWidget import Project_Widget
from TakeOffList import TakeOffList_Widget
from Tab_m import Tab_m_Widget
from Tab_m2 import Tab_m2_Widget
from Tab_m3 import Tab_m3_Widget
from Tab_nr import Tab_nr_Widget
from Tab_rft import Tab_rft_Widget
from TakeOffSheet import TakeOffSheet_Widget
from Edit_m import Edit_m_Dialog
from Edit_nr import Edit_nr_Dialog
from Edit_m2 import Edit_m2_Dialog
from Edit_m3 import Edit_m3_Dialog
from Edit_rft import Edit_rft_Dialog
from Abstract import Abstract_Dialog
from User_license import User_license


class TakeOffSystem(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        # Show the User_license dialog when app loads
        self.user_license_validation()

        # Show the main window
        self.setupUi(self)
        self.show()

        # Store the initial directory when the application is launched
        self.initial_directory = os.getcwd()

        # Create an instance of TakeOffSheet_Widget
        self.takeOffSheetWidget = TakeOffSheet_Widget()

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

        # Insert Tab_m2_Widget() class and add widget to tabWidget
        self.tab_m2_widget = Tab_m2_Widget()
        icon4 = QtGui.QIcon()  # Add button icon with relative path
        image_path_to_icon4 = os.path.join(os.path.dirname(__file__), "images", "area.png")
        icon4.addPixmap(QtGui.QPixmap(image_path_to_icon4), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tabWidget.addTab(self.tab_m2_widget, icon4, "m2")

        # Insert Tab_m3_Widget() class and add widget to tabWidget
        self.tab_m3_widget = Tab_m3_Widget()
        icon5 = QtGui.QIcon()  # Add button icon with relative path
        image_path_to_icon5 = os.path.join(os.path.dirname(__file__), "images", "vol.png")
        icon5.addPixmap(QtGui.QPixmap(image_path_to_icon5), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tabWidget.addTab(self.tab_m3_widget, icon5, "m3")

        # Insert Tab_nr_Widget() class and add widget to tabWidget
        self.tab_nr_widget = Tab_nr_Widget()
        icon2 = QtGui.QIcon()  # Add button icon with relative path
        image_path_to_icon2 = os.path.join(os.path.dirname(__file__), "images", "nr.png")
        icon2.addPixmap(QtGui.QPixmap(image_path_to_icon2), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tabWidget.addTab(self.tab_nr_widget, icon2, "nr")

        # Insert Tab_rft_Widget() class and add widget to tabWidget
        self.tab_rft_widget = Tab_rft_Widget()
        icon3 = QtGui.QIcon()  # Add button icon with relative path
        image_path_to_icon3 = os.path.join(os.path.dirname(__file__), "images", "rft.png")
        icon3.addPixmap(QtGui.QPixmap(image_path_to_icon3), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tabWidget.addTab(self.tab_rft_widget, icon3, "rft")

        # Create an instance of the TakeOffSheet_Widget() class
        self.takeOff_sheet_widget = TakeOffSheet_Widget()
        self.verticalLayout_1.addWidget(self.takeOff_sheet_widget)

        # Connect signal of new_project
        self.actionNew.triggered.connect(self.new_project)

        # Connect signal to open_folder_dialog
        self.actionOpen.triggered.connect(self.open_folder_dialog)
        self.actionOpen.triggered.connect(self.load_check_state)  # Load the check_states in the TreeWidget

        # Connect signal to close_project
        self.actionClose.triggered.connect(self.close_project)

        # Connect signal to close main window
        self.actionExit.triggered.connect(self.close_main_window)

        # Connect signal of edit
        self.takeOff_sheet_widget.pushButton_edit.clicked.connect(self.switch_msmt)

        # Connect signal of Abstract
        self.takeOff_sheet_widget.pushButton_abstract.clicked.connect(self.abstract)

    def new_project(self):

        # Check if a project is already open
        if os.getcwd() != self.initial_directory:
            QtWidgets.QMessageBox.critical(self, "Cannot Create New Project",
                                           "Please close the current project before creating a new one.")
            return

        # Create a new project dialog
        dialog = QDialog()
        ui = NewProject_Dialog()

        # Setup the new project dialog
        ui.setupUi(dialog)

        # Execute the dialog and wait for user interaction
        dialog.exec()

        # Get the project details from the dialog
        project_details = ui.get_project_details()

        # Extract the project name and new folder path from the project details
        project_name = project_details.get("Project Name")
        new_folder_path = project_details.get("Project Folder")

        # Append the project name to the new folder path
        new_folder_path = os.path.join(new_folder_path, project_name)

        # Create the new project folder
        os.makedirs(new_folder_path, exist_ok=True)

        # Set the new folder path as the current working directory for the TakeOffList_Widget
        os.chdir(new_folder_path)

        # Update the displayed folder after the dialog is closed
        self.projectWidgetTree.update_displayed_folder(new_folder_path)

        # Create the path for the takeOffList_DB.json file
        db_file_path = os.path.join(new_folder_path, "takeOffList_DB.json")

        # Initialize an empty tree data dictionary
        tree_data = {}

        # Write the empty tree data to the takeOffList_DB.json file
        with open(db_file_path, 'w') as file:
            json.dump(tree_data, file)

    def close_project(self):
        # Check if a project is currently open
        if os.getcwd() == self.initial_directory:
            QtWidgets.QMessageBox.warning(self, "No Project Open", "No project is currently open.")
            return

        # Reset the current working directory to the initial directory
        os.chdir(self.initial_directory)

        # Update the displayed folder in the UI
        self.projectWidgetTree.update_displayed_folder(self.initial_directory)

        # Clear the take-off list data and update the tree widget
        self.takeOffListWidget.clear_data()

    def close_main_window(self):
        # Close the main window
        self.close()

    def switch_msmt(self):

        # entered_code from TakeOffSheet
        entered_code = self.takeOff_sheet_widget.lineEdit_code.text()

        # Condition to edit msmts based on msmt modes.
        if entered_code.startswith("m_"):  # If entered_code starts with "m"
            self.edit_m_msmt()

        elif entered_code.startswith("m2_"):  # If entered_code starts with "m2"
            self.edit_m2_msmt()

        elif entered_code.startswith("m3_"):  # If entered_code starts with "m2"
            self.edit_m3_msmt()

        elif entered_code.startswith("nr_"):  # If entered_code starts with "nr"
            self.edit_nr_msmt()

        elif entered_code.startswith("rft_"):  # If entered_code starts with "nr"
            self.edit_rft_msmt()
            # pass

    def edit_m_msmt(self):
        dialog = QDialog()

        # Set the window flags to make the dialog stay on top
        dialog.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)

        # entered_code is a class argument of the Edit_Dialog() class, extending from TakeOffSheet() class
        ui = Edit_m_Dialog(entered_code=self.takeOff_sheet_widget.lineEdit_code.text())

        ui.setupUi(dialog)
        dialog.exec()

    def edit_m2_msmt(self):
        dialog = QDialog()

        # Set the window flags to make the dialog stay on top
        dialog.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)

        # entered_code is a class argument of the Edit_Dialog() class, extending from TakeOffSheet() class
        ui = Edit_m2_Dialog(entered_code=self.takeOff_sheet_widget.lineEdit_code.text())

        ui.setupUi(dialog)
        dialog.exec()

    def edit_m3_msmt(self):
        dialog = QDialog()

        # Set the window flags to make the dialog stay on top
        dialog.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)

        # entered_code is a class argument of the Edit_Dialog() class, extending from TakeOffSheet() class
        ui = Edit_m3_Dialog(entered_code=self.takeOff_sheet_widget.lineEdit_code.text())

        ui.setupUi(dialog)
        dialog.exec()

    def edit_nr_msmt(self):
        dialog = QDialog()

        # Set the window flags to make the dialog stay on top
        dialog.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)

        # entered_code is a class argument of the Edit_Dialog() class, extending from TakeOffSheet() class
        ui = Edit_nr_Dialog(entered_code=self.takeOff_sheet_widget.lineEdit_code.text())

        ui.setupUi(dialog)
        dialog.exec()

    def edit_rft_msmt(self):
        dialog = QDialog()

        # Set the window flags to make the dialog stay on top
        dialog.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)

        # entered_code is a class argument of the Edit_Dialog() class, extending from TakeOffSheet() class
        ui = Edit_rft_Dialog(entered_code=self.takeOff_sheet_widget.lineEdit_code.text())

        ui.setupUi(dialog)
        dialog.exec()

    def abstract(self):
        dialog = QDialog()
        ui = Abstract_Dialog()
        ui.setupUi(dialog)
        dialog.exec()

    def open_folder_dialog(self):
        """
        Opens a folder dialog to select the desired job directory and sets it as the current working directory.
        If the selected folder is already the current working directory, print a message to the console.

        :return: None
        """
        dialog = QtWidgets.QFileDialog()
        dialog.setFileMode(QtWidgets.QFileDialog.FileMode.Directory)
        dialog.setOption(QtWidgets.QFileDialog.Option.ShowDirsOnly, True)
        dialog.setDirectory(os.path.join(os.getcwd(), "Data", "Storages", "Local", "Jobs"))

        if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            selected_directory = dialog.selectedFiles()[0]
            # print("cwd from open_folder_dialog(): ", selected_directory)

            # Load takeOffList_widget
            file_name = 'takeOffList_DB.json'
            file_path = os.path.join(selected_directory, file_name)
            # print("file_path from open_folder_dialog(): ", file_path)

            # Set the new folder path as the current working directory for the TakeOffList_Widget
            try:
                with open(file_path, 'r') as file:
                    tree_data = json.load(file)

                    # Replace data list with parent items from tree_data
                    self.data = list(tree_data.keys())

                    # Clear the tree widget
                    self.root_item = self.takeOffListWidget.root_item
                    self.root_item.takeChildren()

                    # Add data items to tree widget
                    for parent_text, child_items in tree_data.items():
                        parent_item = QtWidgets.QTreeWidgetItem(self.root_item)
                        parent_item.setText(0, parent_text)
                        for child_text in child_items:
                            child_item = QtWidgets.QTreeWidgetItem(parent_item)
                            child_item.setText(0, child_text)
                            parent_item.addChild(child_item)

                        # Expand all the parent items when app loads
                        parent_item.setExpanded(True)
            except Exception:
                pass

            if selected_directory == os.getcwd():
                print("Selected folder is already the current working directory.")
            else:
                os.chdir(selected_directory)  # Set the selected directory as the current working directory

                # Update the displayed folder in the UI
                self.projectWidgetTree.update_displayed_folder(selected_directory)

                # Update the label with the current working directory
                self.update_cwd_label("   " + selected_directory)

    def user_license_validation(self):
        dialog = QDialog()
        ui = User_license(dialog)

        # Show the User_license dialog when app loads
        ui.setupUi(dialog)
        ui.cancelClicked.connect(self.close_system)  # Connect signal to close main window

        dialog.exec()

    def close_system(self):
        # Close the main window
        sys.exit()

    def load_check_state(self):
        # File name
        file_name = 'Items_checked_states.json'

        # Get the current directory
        current_dir = os.getcwd()

        # Construct the file path relative to the current directory
        file_path = os.path.join(current_dir, file_name)

        # Debugging
        # print("file_path from load_check_state(): ", file_path)

        try:
            with open(file_path, 'r') as file:
                item_data_list = json.load(file)

                # Call a recursive method to update the tree widget
                self.update_tree_widget_with_checked_states(self.root_item, item_data_list)
        except Exception as e:
            print(f"Error reading from file: {e}")

    def update_tree_widget_with_checked_states(self, parent_item, item_data_list):
        for i in range(parent_item.childCount()):
            item = parent_item.child(i)
            text = item.text(0)

            # Find a matching item in the loaded data
            matching_data = next((data for data in item_data_list if data['text'] == text), None)

            if matching_data:
                checked_state = matching_data['checked_state']
                if checked_state:
                    item.setFlags(item.flags() | QtCore.Qt.ItemFlag.ItemIsUserCheckable)
                    item.setCheckState(0, QtCore.Qt.CheckState.Checked)
                else:
                    item.setFlags(item.flags() | QtCore.Qt.ItemFlag.ItemIsUserCheckable)
                    item.setCheckState(0, QtCore.Qt.CheckState.Unchecked)

            # Recursively update sub-items
            if item.childCount() > 0:
                self.update_tree_widget_with_checked_states(item, item_data_list)
