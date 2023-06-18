# self implementation generated from reading ui file 'TakeOffList_App.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import json
import os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QTreeWidgetItem, QTreeWidget, QLineEdit


class TakeOffList_Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.data = []

        self.setupUi()

    def setupUi(self):
        # self.setObjectName("self")
        self.setObjectName("TakeOffList_Widget")
        self.resize(400, 600)
        icon = QtGui.QIcon()
        image_path_icon = os.path.join(os.path.dirname(__file__), "images", "TakeOffList.png")
        icon.addPixmap(QtGui.QPixmap(image_path_icon), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.treeWidget = QtWidgets.QTreeWidget(parent=self)
        self.treeWidget.setObjectName("treeWidget")

        # Alternate the colors of the rows for better User Experience (UX)
        self.treeWidget.setAlternatingRowColors(True)

        # connect the double click event to a method that
        # gets the currently selected item and replaces it
        # with a QLineEdit Widget
        self.treeWidget.itemDoubleClicked.connect(self.edit_item)

        # Add root item to treeWidget
        self.root_item = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.root_item.setText(0, "Work items :")
        self.root_item.setExpanded(True)

        # Load database in treeWidget when App runs.
        self.load_database()

        self.verticalLayout.addWidget(self.treeWidget)
        self.lineEdit = QtWidgets.QLineEdit(parent=self)
        self.lineEdit.setObjectName("lineEdit")

        # Connect signal
        self.lineEdit.returnPressed.connect(self.insert_data)

        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_insertSubItem = QtWidgets.QPushButton(parent=self)
        icon1 = QtGui.QIcon()
        image_path_icon1 = os.path.join(os.path.dirname(__file__), "images", "node-insert-previous.png")
        icon1.addPixmap(QtGui.QPixmap(image_path_icon1), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_insertSubItem.setIcon(icon1)
        self.pushButton_insertSubItem.setObjectName("pushButton_insertSubItem")

        # Connect signal
        self.pushButton_insertSubItem.clicked.connect(self.new_sub_item)

        self.horizontalLayout.addWidget(self.pushButton_insertSubItem)
        spacerItem = QtWidgets.QSpacerItem(58, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_delete = QtWidgets.QPushButton(parent=self)
        icon2 = QtGui.QIcon()
        image_path_icon2 = os.path.join(os.path.dirname(__file__), "images", "cross.png")
        icon2.addPixmap(QtGui.QPixmap(image_path_icon2), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_delete.setIcon(icon2)
        self.pushButton_delete.setObjectName("pushButton_delete")

        # Connect signal
        self.pushButton_delete.clicked.connect(self.delete_item)

        self.horizontalLayout.addWidget(self.pushButton_delete)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def insert_data(self):
        # Take input from lineEdit
        text = self.lineEdit.text()

        # Only add non-empty strings
        if text.strip() != '':
            # Add the text as a child item of the parent root_item
            child_item = QtWidgets.QTreeWidgetItem(self.root_item)
            child_item.setText(0, text)

            # Clear lineEdit
            self.lineEdit.clear()

            # Update the database
            self.update_database()

    def delete_item(self):
        # Get the selected item(s)
        items = self.treeWidget.selectedItems()

        # Remove each selected item from the tree widget and the data list
        for item in items:
            if item == self.root_item:  # Skip deleting the root_item
                continue

            parent_item = item.parent()
            is_last_child = parent_item.childCount() == 1  # Check if the item is the last child of its parent

            # Remove the item from the tree widget
            parent_item.removeChild(item)

            # Remove the item from the data list if it exists
            if item.text(0) in self.data:
                self.data.remove(item.text(0))

            # Delete the item object to avoid runtime errors
            del item

            # If the item was the last child, remove the parent item from the tree widget as well
            if is_last_child:
                self.treeWidget.takeTopLevelItem(self.treeWidget.indexOfTopLevelItem(parent_item))

        # Update the database
        self.update_database()

    def update_database(self, file_name='takeOffList_DB.json'):
        # Create a dictionary representing the current state of the tree widget
        tree_data = {}
        for i in range(self.root_item.childCount()):
            parent_item = self.root_item.child(i)
            parent_text = parent_item.text(0)
            child_items = [parent_item.child(j).text(0) for j in range(parent_item.childCount())]
            tree_data[parent_text] = child_items

        # Print the updated tree_data dict
        print(tree_data)

        # Get the current directory
        current_dir = os.getcwd()

        # Construct the file path relative to the current directory
        file_path = os.path.join(current_dir, file_name)    #TODO write to project folder

        # Write the tree data to the JSON file
        with open(file_path, 'w') as file:
            json.dump(tree_data, file)

    def update_tree_widget(self):
        self.root_item.takeChildren()  # Remove all previous child items

        # Add data items to tree widget
        for key, value in self.data.items():  # Iterate over key-value pairs using items()
            parent_item = QtWidgets.QTreeWidgetItem(self.root_item)
            parent_item.setText(0, str(key))  # Convert key to string before setting it as the text

            if isinstance(value, list):
                for item in value:
                    child_item = QtWidgets.QTreeWidgetItem(parent_item)
                    child_item.setText(0, str(item))  # Convert item to string before setting it as the text
            else:
                child_item = QtWidgets.QTreeWidgetItem(parent_item)
                child_item.setText(0, str(value))  # Convert value to string before setting it as the text

            parent_item.setExpanded(True)  # Expand the parent item to show child items

    def load_database(self, file_name='takeOffList_DB.json'):   #TODO Load from project folder
        # Get the current directory
        current_dir = os.getcwd()

        # Construct the file path relative to the current directory
        file_path = os.path.join(current_dir, file_name)

        try:
            with open(file_path, 'r') as file:
                tree_data = json.load(file)

            # Replace data list with parent items from tree_data
            self.data = list(tree_data.keys())

            # Clear the tree widget
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

    def edit_item(self):
        item = self.treeWidget.itemFromIndex(self.treeWidget.selectedIndexes()[0])
        column = self.treeWidget.currentColumn()
        edit = QLineEdit()
        edit.returnPressed.connect(lambda: self.update_item(item, column, edit.text()))
        self.treeWidget.setItemWidget(item, column, edit)

        # Update the database
        self.update_database()

    def update_item(self, item, column, text):
        if text.strip():  # Check if text is not empty or contains only whitespace
            item.setText(column, text)
        self.treeWidget.setItemWidget(item, column, None)

        # Update the database
        self.update_database()

        # Load the database
        self.load_database()

    def new_sub_item(self):
        # Get the currently selected item in the tree widget
        selected_item = self.treeWidget.currentItem()

        # Only add a new sub-item if a child item is selected
        if selected_item and selected_item.parent():

            # Create a new child item
            child_item = QtWidgets.QTreeWidgetItem(selected_item)
            child_item.setText(0, "New Sub-Item")

            # Expand the parent item to show the new sub-item
            selected_item.setExpanded(True)

            # Update the database
            self.update_database()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("TakeOffList_Widget", "Take-Off List"))
        self.treeWidget.headerItem().setText(0, _translate("TakeOffList_Widget", "Take-Off List"))
        self.lineEdit.setPlaceholderText(_translate("TakeOffList_Widget", "Type in work item and hit enter."))
        self.pushButton_insertSubItem.setText(_translate("TakeOffList_Widget", "Insert Sub-Item"))
        self.pushButton_delete.setText(_translate("TakeOffList_Widget", "    Delete Item    "))


# if __name__ == "__main__":
#     import sys
#
#     app = QtWidgets.QApplication(sys.argv)
#     self = QtWidgets.QWidget()
#     ui = Ui_self()
#     ui.setupUi(self)
#     self.show()
#     sys.exit(app.exec())