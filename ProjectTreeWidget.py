from PyQt6 import QtWidgets, QtCore
import sys
import os


class Project_Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.treeWidget_project = QtWidgets.QTreeWidget(self)
        self.treeWidget_project.setObjectName("treeWidget_project")
        self.treeWidget_project.setHeaderLabels(["Project Folder"])

        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.addWidget(self.treeWidget_project)

    def display_folder_contents(self, folder_path):
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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    widget = Project_Widget()
    widget.display_folder_contents("/path/to/project/folder")
    widget.show()

    sys.exit(app.exec())
