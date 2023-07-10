from PyQt6 import QtWidgets, QtCore
import sys
import os


class Project_Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.treeWidget_project = QtWidgets.QTreeWidget(self)
        self.treeWidget_project.setObjectName("treeWidget_project")
        self.treeWidget_project.setHeaderLabels(["Project Folder"])

        # Display folder when app loads
        self.display_folder_contents('/Users/kilpatrick/Documents/Trad Take-Off app/Simpe Take-Off')

        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.addWidget(self.treeWidget_project)

    def display_folder_contents(self, folder_path):
        """
        Populates the tree widget with the contents of the specified folder.

        This method clears the existing contents of the tree widget and adds the contents of the specified folder as
        items to the tree widget. Each item represents a file or sub folder within the specified folder.

        The specified folder path is set as the text of the root item in the tree widget. The method then calls the
        _add_folder_contents method to recursively add the contents of the folder as child items under the root item.

        :param folder_path:
        :return: None
        """

        self.treeWidget_project.clear()

        root_item = QtWidgets.QTreeWidgetItem(self.treeWidget_project)
        root_item.setText(0, folder_path)

        self._add_folder_contents(folder_path, root_item)

    def _add_folder_contents(self, folder_path, parent_item):
        for entry in os.listdir(folder_path):
            entry_path = os.path.join(folder_path, entry)

            item = QtWidgets.QTreeWidgetItem(parent_item)
            item.setText(0, entry)

            if os.path.isdir(entry_path):
                self._add_folder_contents(entry_path, item)
