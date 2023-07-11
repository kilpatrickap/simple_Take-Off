from PyQt6 import QtWidgets, QtCore, QtGui
import sys
import os


class Project_Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.setFont(font)

        self.treeWidget_project = QtWidgets.QTreeWidget(self)
        self.treeWidget_project.setObjectName("treeWidget_project")
        self.treeWidget_project.setHeaderLabels(["Project Folder"])
        self.treeWidget_project.setAlternatingRowColors(True)

        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.addWidget(self.treeWidget_project)

        # Display the current working directory when the app loads
        current_dir = os.getcwd()
        folder_path = os.path.join(current_dir, "Data/Storages/Local/Jobs")
        self.update_displayed_folder(folder_path)

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

        if self.has_subfolders(folder_path):
            # Add button icon with relative path
            icon1 = QtGui.QIcon()
            image_path_to_icon1 = os.path.join(os.path.dirname(__file__), "images", "blue-folder-horizontal-open.png")
            icon1.addPixmap(QtGui.QPixmap(image_path_to_icon1), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            root_item.setIcon(0, icon1)

        self._add_folder_contents(folder_path, root_item)

    def has_subfolders(self, folder_path):
        """
        Checks if a folder contains any sub-folders.

        :param folder_path: The path of the folder to check.
        :return: True if the folder contains sub-folders, False otherwise.
        """
        for entry in os.listdir(folder_path):
            entry_path = os.path.join(folder_path, entry)
            if os.path.isdir(entry_path):
                return True
        return False

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
                icon1 = QtGui.QIcon()
                image_path_to_icon1 = os.path.join(os.path.dirname(__file__), "images", "blue-folder-horizontal.png")
                icon1.addPixmap(QtGui.QPixmap(image_path_to_icon1), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                item.setIcon(0, icon1)

                # Connect the tree widget's itemExpanded signal to the _folder_item_expanded method
                self.treeWidget_project.itemExpanded.connect(self._folder_item_expanded)

                self._add_folder_contents(entry_path, item)

    def _folder_item_expanded(self, item):
        """
        Slot method to handle the expanded signal of folder items.

        This method is called when a folder item is expanded. It changes the item's icon to indicate it is expanded.

        :param item: The expanded folder item.
        :return: None
        """
        # Change the icon to the open folder icon
        icon = QtGui.QIcon()
        image_path = os.path.join(os.path.dirname(__file__), "images", "blue-folder-horizontal-open.png")
        icon.addPixmap(QtGui.QPixmap(image_path), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        item.setIcon(0, icon)

    def update_displayed_folder(self, folder_path, file_name=None):
        """
        Updates the displayed folder in the tree widget.

        This method updates the displayed folder in the tree widget to the specified folder path, optionally appending
        the file name to the folder path.

        :param folder_path: The path of the folder to be displayed.
        :param file_name: Optional file name to append to the folder path.
        :return: None
        """
        if file_name:
            folder_path = os.path.join(folder_path, file_name)  # Append the file name to the folder path

        self.display_folder_contents(folder_path)  # Pass the updated folder path to display_folder_contents method

    def display_folder_contents(self, folder_path):
        """
        Populates the tree widget with the contents of the specified folder.

        This method clears the existing contents of the tree widget and adds the contents of the specified folder as
        items to the tree widget. Each item represents a file or subfolder within the specified folder.

        :param folder_path: The path of the folder whose contents should be displayed.
        :return: None
        """
        self.treeWidget_project.clear()

        root_item = QtWidgets.QTreeWidgetItem(self.treeWidget_project)
        root_item.setText(0, folder_path)  # Set the folder path as the text for the root item

        if self.has_subfolders(folder_path):
            icon1 = QtGui.QIcon()
            image_path_to_icon1 = os.path.join(os.path.dirname(__file__), "images", "blue-folder-horizontal-open.png")
            icon1.addPixmap(QtGui.QPixmap(image_path_to_icon1), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            root_item.setIcon(0, icon1)

        self._add_folder_contents(folder_path, root_item)
