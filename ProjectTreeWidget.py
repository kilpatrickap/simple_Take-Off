from PyQt6 import QtWidgets


class Project_Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.treeWidget_project = QtWidgets.QTreeWidget(self)
        self.treeWidget_project.setObjectName("treeWidget_project")
        self.treeWidget_project.setHeaderLabels(["Project Folder"])

        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.addWidget(self.treeWidget_project)
