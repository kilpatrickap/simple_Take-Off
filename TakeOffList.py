import json
import os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QTreeWidgetItem, QTreeWidget, QLineEdit, QMenu, QCheckBox


class TakeOffList_Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.data = []

        self.setupUi()

        # # Load the saved item states from the JSON file
        # self.load_check_state()

    def setupUi(self):
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

        # Connect the double click event to a method that
        # gets the currently selected item and replaces it
        # with a QLineEdit Widget
        self.treeWidget.itemDoubleClicked.connect(self.edit_item)

        # Add root item to treeWidget
        self.root_item = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.root_item.setText(0, "Work items :")
        self.root_item.setExpanded(True)

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
        image_path_icon2 = os.path.join(os.path.dirname(__file__), "images", "node-delete.png")
        icon2.addPixmap(QtGui.QPixmap(image_path_icon2), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_delete.setIcon(icon2)
        self.pushButton_delete.setObjectName("pushButton_delete")

        # Connect signal
        self.pushButton_delete.clicked.connect(self.delete_item)

        self.horizontalLayout.addWidget(self.pushButton_delete)
        self.verticalLayout.addLayout(self.horizontalLayout)

        # Create a context menu for right-click actions
        context_menu = QMenu(self)
        mark_completed_action = context_menu.addAction("Tick as Completed")
        mark_uncompleted_action = context_menu.addAction("Tick as Uncompleted")

        # Connect context menu actions to methods
        mark_completed_action.triggered.connect(self.mark_completed)
        mark_uncompleted_action.triggered.connect(self.mark_uncompleted)

        # Set the context menu for the tree widget
        self.treeWidget.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.treeWidget.customContextMenuRequested.connect(self.show_context_menu)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def insert_data(self):
        # Take input from lineEdit
        text = self.lineEdit.text()

        # Only add non-empty strings
        if text.strip() != '':
            # Create a new QTreeWidgetItem
            child_item = QTreeWidgetItem(self.root_item, [text])

            # Set the item's flags to make it checkable
            child_item.setFlags(child_item.flags() | QtCore.Qt.ItemFlag.ItemIsUserCheckable)
            child_item.setCheckState(0, QtCore.Qt.CheckState.Unchecked)

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

        # Get the current directory
        current_dir = os.getcwd()

        # Construct the file path relative to the current directory
        file_path = os.path.join(current_dir, file_name)

        # Debugging
        # print("file_path from update_database(): ", file_path)

        # Write the tree data to the JSON file
        with open(file_path, 'w') as file:
            json.dump(tree_data, file)

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

            # Set the item's flags to make it checkable
            child_item.setFlags(child_item.flags() | QtCore.Qt.ItemFlag.ItemIsUserCheckable)
            child_item.setCheckState(0, QtCore.Qt.CheckState.Unchecked)

            # Update the database
            self.update_database()

    def clear_data(self):
        # Clear the data list
        self.data = []

        # Clear the tree widget
        self.root_item.takeChildren()

        # Update the database to reflect the cleared data
        self.update_database()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("TakeOffList_Widget", "Take-Off List"))
        self.treeWidget.headerItem().setText(0, _translate("TakeOffList_Widget", "Take-Off List"))
        self.lineEdit.setPlaceholderText(_translate("TakeOffList_Widget", "Type in work item and hit enter."))
        self.pushButton_insertSubItem.setText(_translate("TakeOffList_Widget", "Insert Sub-Item"))
        self.pushButton_delete.setText(_translate("TakeOffList_Widget", "    Delete Item    "))

    def show_context_menu(self, position):
        # Show the context menu at the cursor's position
        context_menu = QMenu(self)
        mark_completed_action = context_menu.addAction("Tick as Completed")
        mark_uncompleted_action = context_menu.addAction("Tick as Uncompleted")

        # Connect context menu actions to methods
        mark_completed_action.triggered.connect(self.mark_completed)
        mark_uncompleted_action.triggered.connect(self.mark_uncompleted)

        # Execute the context menu at the specified position
        action = context_menu.exec(self.treeWidget.mapToGlobal(position))

        # Handle the selected action
        if action == mark_completed_action:
            self.mark_completed()
        elif action == mark_uncompleted_action:
            self.mark_uncompleted()

    def mark_completed(self):
        item = self.treeWidget.currentItem()
        if item:
            item.setFlags(item.flags() | QtCore.Qt.ItemFlag.ItemIsUserCheckable)
            item.setCheckState(0, QtCore.Qt.CheckState.Checked)

            # Save check state
            self.save_check_state()

    def mark_uncompleted(self):
        item = self.treeWidget.currentItem()
        if item:
            item.setFlags(item.flags() | QtCore.Qt.ItemFlag.ItemIsUserCheckable)
            item.setCheckState(0, QtCore.Qt.CheckState.Unchecked)

            # Save check state
            self.save_check_state()

    def save_check_state(self):
        # Create a list to store item data
        item_data_list = []

        # Start the recursive traversal from the root item
        self.collect_item_data(self.root_item, item_data_list)

        # File name
        file_name = 'Items_checked_states.json'

        # Get the current directory
        current_dir = os.getcwd()

        # Construct the file path relative to the current directory
        file_path = os.path.join(current_dir, file_name)

        try:
            with open(file_path, 'w') as file:
                json.dump(item_data_list, file)
        except Exception as e:
            print(f"Error writing to file: {e}")

    def collect_item_data(self, parent_item, item_data_list):
        # Iterate through all child items of the parent_item
        for i in range(parent_item.childCount()):
            item = parent_item.child(i)
            checked_state = item.checkState(0) == QtCore.Qt.CheckState.Checked
            text = item.text(0)
            item_data = {'text': text, 'checked_state': checked_state}
            item_data_list.append(item_data)

            # If the item has sub-items, recursively collect their data
            if item.childCount() > 0:
                self.collect_item_data(item, item_data_list)

