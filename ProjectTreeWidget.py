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

        :param folder_path: The path of the folder whose contents should be displayed.
        :return: None
        """

        self.treeWidget_project.clear()

        root_item = QtWidgets.QTreeWidgetItem(self.treeWidget_project)
        root_item.setText(0, folder_path)

        self._add_folder_contents(folder_path, root_item)

    def _add_folder_contents(self, folder_path, parent_item):
        """
        Recursively adds the contents of a folder to a tree widget.

        This private method is called by the `display_folder_contents` method to add the contents of a specified
        folder to a tree widget. It recursively traverses through the folder structure and adds each file and
        subfolder as items to the tree widget, under the provided parent item.

        :param folder_path: The path of the folder whose contents should be added.
        :param parent_item: The parent item under which the folder contents should be added.
        :return:
        """

        for entry in os.listdir(folder_path):
            entry_path = os.path.join(folder_path, entry)

            item = QtWidgets.QTreeWidgetItem(parent_item)
            item.setText(0, entry)

            if os.path.isdir(entry_path):
                self._add_folder_contents(entry_path, item)
