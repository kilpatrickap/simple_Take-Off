import os.path
import sqlite3
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox

from TakeOffSheet import TakeOffSheet_Widget


class Tab_m3_Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.groupBox_m3 = QtWidgets.QGroupBox(parent=self)
        self.groupBox_m3.setGeometry(QtCore.QRect(10, 10, 790, 501))
        self.groupBox_m3.setObjectName("groupBox_m3")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_m3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_m3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)

        self.lineEdit_desc = QtWidgets.QLineEdit(parent=self.groupBox_m3)
        self.lineEdit_desc.setObjectName("lineEdit_desc")

        # Connect signal
        self.lineEdit_desc.returnPressed.connect(self.desc)

        self.horizontalLayout_7.addWidget(self.lineEdit_desc)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_m3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)

        self.comboBox = QtWidgets.QComboBox(parent=self.groupBox_m3)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        # Connect signal
        self.comboBox.currentIndexChanged.connect(self.trade)

        self.horizontalLayout.addWidget(self.comboBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox_m3)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.label_code = QtWidgets.QLabel(parent=self.groupBox_m3)
        self.label_code.setObjectName("label_code")
        self.horizontalLayout_3.addWidget(self.label_code)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")

        # Horizontal spacer
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)

        self.pushButton_m3_add = QtWidgets.QPushButton(parent=self.groupBox_m3)

        # Add button icon with relative path
        icon1 = QtGui.QIcon()
        image_path_to_icon1 = os.path.join(os.path.dirname(__file__), "images", "plus.png")
        icon1.addPixmap(QtGui.QPixmap(image_path_to_icon1), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_m3_add.setIcon(icon1)

        self.pushButton_m3_add.setObjectName("pushButton_m3_add")

        # Connect signal
        self.pushButton_m3_add.clicked.connect(self.add_row)

        self.horizontalLayout_10.addWidget(self.pushButton_m3_add)
        self.pushButton_m3_ddt = QtWidgets.QPushButton(parent=self.groupBox_m3)

        # Deduct button icon with relative path
        icon2 = QtGui.QIcon()
        image_path_to_icon2 = os.path.join(os.path.dirname(__file__), "images", "minus.png")
        icon2.addPixmap(QtGui.QPixmap(image_path_to_icon2), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_m3_ddt.setIcon(icon2)

        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.pushButton_m3_ddt.setFont(font)
        self.pushButton_m3_ddt.setObjectName("pushButton_m3_ddt")

        # Connect signal
        self.pushButton_m3_ddt.clicked.connect(self.ddt_row)
        self.pushButton_m3_ddt.setStyleSheet("color: red")

        self.horizontalLayout_10.addWidget(self.pushButton_m3_ddt)
        self.pushButton_m3_del = QtWidgets.QPushButton(parent=self.groupBox_m3)

        # Delete button icon with relative path
        icon3 = QtGui.QIcon()
        image_path_to_icon3 = os.path.join(os.path.dirname(__file__), "images", "cross.png")
        icon3.addPixmap(QtGui.QPixmap(image_path_to_icon3), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_m3_del.setIcon(icon3)

        self.pushButton_m3_del.setObjectName("pushButton_m3_del")

        # Connect signal
        self.pushButton_m3_del.clicked.connect(self.delete_row)

        self.horizontalLayout_10.addWidget(self.pushButton_m3_del)

        self.pushButton_m3_sqr = QtWidgets.QPushButton(parent=self.groupBox_m3)

        # Square button icon with relative path
        icon4 = QtGui.QIcon()
        image_path_to_icon4 = os.path.join(os.path.dirname(__file__), "images", "calculator.png")
        icon4.addPixmap(QtGui.QPixmap(image_path_to_icon4), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_m3_sqr.setIcon(icon4)

        self.pushButton_m3_sqr.setObjectName("pushButton_m3_sqr")

        # Connect signal
        self.pushButton_m3_sqr.clicked.connect(self.square)

        self.horizontalLayout_10.addWidget(self.pushButton_m3_sqr)

        # Horizontal spacer
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)

        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.tableWidget_m3 = QtWidgets.QTableWidget(parent=self.groupBox_m3)
        self.tableWidget_m3.setObjectName("tableWidget_m3")

        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.tableWidget_m3.setFont(font)

        self.tableWidget_m3.setColumnCount(9)
        self.tableWidget_m3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_m3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_m3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_m3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_m3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_m3.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_m3.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_m3.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_m3.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_m3.setHorizontalHeaderItem(8, item)
        self.verticalLayout.addWidget(self.tableWidget_m3)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")

        # Connect the resize event to the method for dynamic column widths
        self.resizeEvent = self.on_resize

        # Horizontal spacer
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem3)

        self.pushButton_m3_clear = QtWidgets.QPushButton(parent=self.groupBox_m3)

        # Clear button icon with relative path
        icon5 = QtGui.QIcon()
        image_path_to_icon5 = os.path.join(os.path.dirname(__file__), "images", "application-blue.png")
        icon5.addPixmap(QtGui.QPixmap(image_path_to_icon5), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_m3_clear.setIcon(icon5)

        self.pushButton_m3_clear.setObjectName("pushButton_m3_clear")

        # Connect signal
        self.pushButton_m3_clear.clicked.connect(self.clear_table)

        self.horizontalLayout_11.addWidget(self.pushButton_m3_clear)
        self.pushButton_m3_insert = QtWidgets.QPushButton(parent=self.groupBox_m3)

        # Insert button icon with relative path
        icon6 = QtGui.QIcon()
        image_path_to_icon6 = os.path.join(os.path.dirname(__file__), "images", "table-export.png")
        icon6.addPixmap(QtGui.QPixmap(image_path_to_icon6), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_m3_insert.setIcon(icon6)

        self.pushButton_m3_insert.setObjectName("pushButton_m3_insert")

        # Connect signals
        self.pushButton_m3_insert.clicked.connect(self.insert_dialog)

        self.horizontalLayout_11.addWidget(self.pushButton_m3_insert)

        # Horizontal spacer
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem4)

        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.retranslateUi()
        # self.tabWidget_m.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

    def desc(self):
        desc_text = self.lineEdit_desc.text()

        # Set the entered string in the "desc" column of the new row
        desc_item = QtWidgets.QTableWidgetItem(desc_text)
        self.tableWidget_m3.setItem(0, 2, desc_item)

        # de-activate lineEdit_desc item
        self.lineEdit_desc.setEnabled(False)

    def trade(self):
        selected_item = self.comboBox.currentText()  # Retrieve the selected item from the comboBox
        first_letter = selected_item[0]  # Get the first letter of the selected item

        row_index = 0  # the row index of the selected item

        # Set the first letter in the trade column of the 1st row
        trade_item = QtWidgets.QTableWidgetItem(first_letter)
        self.tableWidget_m3.setItem(row_index, 1, trade_item)

        #  Set the first letter in the trade column of 2nd row
        row_index += 1
        trade_item_clone = QtWidgets.QTableWidgetItem(first_letter)
        self.tableWidget_m3.setItem(row_index, 1, trade_item_clone)

        #  Set the first letter in the trade column of 3rd row
        row_index += 1
        trade_item_clone = QtWidgets.QTableWidgetItem(first_letter)
        self.tableWidget_m3.setItem(row_index, 1, trade_item_clone)

        # Execute the code method
        self.code()

        # de-activate comboBox item
        self.comboBox.setEnabled(False)

    def get_highest_code_number(self):
        # Connect to the SQLite database
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()

        # Execute query to retrieve table names ending with a number
        cursor.execute("""SELECT name FROM sqlite_master WHERE type='table' 
                        AND name LIKE 'm3_A%' 
                        OR name LIKE 'm3_C%'
                        OR name LIKE 'm3_D%'
                        OR name LIKE 'm3_E%'
                        OR name LIKE 'm3_F%'
                        OR name LIKE 'm3_G%'
                        OR name LIKE 'm3_H%'
                        OR name LIKE 'm3_J%'
                        OR name LIKE 'm3_K%'
                        OR name LIKE 'm3_L%'
                        OR name LIKE 'm3_M%'
                        OR name LIKE 'm3_N%'
                        OR name LIKE 'm3_P%'
                        OR name LIKE 'm3_Q%'
                        OR name LIKE 'm3_R%'
                        OR name LIKE 'm3_S%'
                        OR name LIKE 'm3_T%'
                        OR name LIKE 'm3_U%'
                        OR name LIKE 'm3_V%'
                        OR name LIKE 'm3_W%'
                        OR name LIKE 'm3_X%'
                        """)
        tables = cursor.fetchall()

        # Find the table with the highest number
        highest_number = 0
        for table in tables:
            table_name = table[0]
            number = int(table_name.split('_')[-1][1:])
            if number > highest_number:
                highest_number = number

        # Close the database connection
        conn.close()

        return highest_number

    def code(self):
        selected_item = self.comboBox.currentText()  # Retrieve the selected item from the comboBox
        first_letter = selected_item[0]  # Get the first letter of the selected item

        # Retrieve the current highest code number for the given tab and increment it by 1
        next_code_number = self.get_highest_code_number() + 1

        # Concatenate the tab name, first letter, last letter, and the incremented code number
        code_string = f"m3_{first_letter}{next_code_number}"
        self.label_code.setText(code_string)  # Update the label "code shows up here" with the generated code

        # Set the code in the code column of the tableWidget_m3
        code_item = QtWidgets.QTableWidgetItem(code_string)

        row = 0     # Initialize row for first row
        self.tableWidget_m3.setItem(row, 0, code_item)  # set row

        row += 1    # Increment row by 1 and set it at the 2nd row
        code_item_clone = code_item.clone()     # Create a clone of code_item
        self.tableWidget_m3.setItem(row, 0, code_item_clone)  # set row

        row += 1  # Increment row by 1 and set it at the 3rd row
        code_item_clone = code_item.clone()  # Create a clone of code_item
        self.tableWidget_m3.setItem(row, 0, code_item_clone)  # set row

        return code_string  # returns e.g m2_M1, m2_D1 etc as type str

    def add_row(self):
        """
        Adds 3 new rows to the table and copies data from existing rows.

        This method adds three new rows at the end of the table and copies data from the first three rows to the new rows.
        It also sets a special unit (m3) value in one of the cells of the second newly inserted row.

        :parameter: None

        :return: None
        """
        unit_m3 = "m3"  # Set the unit

        last_row = self.tableWidget_m3.rowCount() - 1

        if last_row >= 2:
            for i in range(3):  # Set number of rows to be added (m2 = 2; m3 = 3)
                source_row = i  # Iterate over the first three rows
                destination_row = last_row + i + 1

                for column in range(self.tableWidget_m3.columnCount()):
                    item = self.tableWidget_m3.item(source_row, column)
                    if item is not None:
                        new_item = QtWidgets.QTableWidgetItem(item)
                        flags = item.flags()
                        new_item.setFlags(flags)
                        self.tableWidget_m3.setItem(destination_row, column, new_item)

        self.tableWidget_m3.insertRow(last_row + 1)
        self.tableWidget_m3.insertRow(last_row + 2)
        self.tableWidget_m3.insertRow(last_row + 3)  # Insert 3rd row

        # Copy items and formatting from the first 3 rows to the new rows
        for row in range(3):  # Iterate over the first three rows
            for column in range(self.tableWidget_m3.columnCount()):
                item = self.tableWidget_m3.item(row, column)
                if item is not None:
                    new_item = QtWidgets.QTableWidgetItem(item)
                    flags = item.flags()
                    new_item.setFlags(flags)
                    self.tableWidget_m3.setItem(row + last_row + 1, column, new_item)

        # Set the unit in the new rows
        unit_m3_item = QtWidgets.QTableWidgetItem(unit_m3)
        flags = unit_m3_item.flags()
        flags &= ~QtCore.Qt.ItemFlag.ItemIsEditable  # Set the cell as read-only
        flags &= ~QtCore.Qt.ItemFlag.ItemIsSelectable  # Disable cell selection
        unit_m3_item.setFlags(flags)

        self.tableWidget_m3.setItem(last_row + 3, 7, unit_m3_item)  # Set the unit item on the second newly inserted row

    def ddt_row(self):
        """
        Adds 3 new rows to the table and copies data from existing rows.

        This method adds three new rows at the end of the table and copies data from the first three rows to the new rows.
        It also sets a special unit (m3) value in one of the cells of the second newly inserted row.

        :parameter: None

        :return: None
        """
        unit_m3 = "m3"  # Set the unit

        last_row = self.tableWidget_m3.rowCount() - 1

        if last_row >= 2:
            for i in range(3):  # Set number of rows to be added (m2 = 2; m3 = 3)
                source_row = i  # Iterate over the first three rows
                destination_row = last_row + i + 1

                for column in range(self.tableWidget_m3.columnCount()):
                    item = self.tableWidget_m3.item(source_row, column)
                    if item is not None:
                        new_item = QtWidgets.QTableWidgetItem(item)
                        flags = item.flags()
                        new_item.setFlags(flags)

                        # Set the text color to red
                        new_item.setForeground(QtGui.QColor("red"))

                        self.tableWidget_m3.setItem(destination_row, column, new_item)

        self.tableWidget_m3.insertRow(last_row + 1)
        self.tableWidget_m3.insertRow(last_row + 2)
        self.tableWidget_m3.insertRow(last_row + 3)  # Insert 3rd row

        # Copy items and formatting from the first 3 rows to the new rows
        for row in range(3):  # Iterate over the first three rows
            for column in range(self.tableWidget_m3.columnCount()):
                item = self.tableWidget_m3.item(row, column)
                if item is not None:
                    new_item = QtWidgets.QTableWidgetItem(item)
                    flags = item.flags()
                    new_item.setFlags(flags)

                    # Set the text color to red
                    new_item.setForeground(QtGui.QColor("red"))

                    self.tableWidget_m3.setItem(row + last_row + 1, column, new_item)

        # Set the unit in the new rows
        unit_m3_item = QtWidgets.QTableWidgetItem(unit_m3)
        flags = unit_m3_item.flags()
        flags &= ~QtCore.Qt.ItemFlag.ItemIsEditable  # Set the cell as read-only
        flags &= ~QtCore.Qt.ItemFlag.ItemIsSelectable  # Disable cell selection
        unit_m3_item.setFlags(flags)

        # Set the color of unit_m3_item to red
        unit_m3_item.setForeground(QtGui.QColor("red"))

        self.tableWidget_m3.setItem(last_row + 3, 7, unit_m3_item)  # Set the unit item on the second newly inserted row

    def delete_row(self):
        current_row = self.tableWidget_m3.currentRow()
        self.tableWidget_m3.removeRow(current_row)

        # If all rows are deleted, activate the lineEdit_desc item
        self.lineEdit_desc.setEnabled(True)

        # Activate comboBox item
        self.comboBox.setEnabled(True)

    def square(self, start_row=0):
        """
        Recursively calculates and updates square values in a table widget.

        This method recursively processes pairs of rows in a table widget, updating the necessary column values
        to calculate the square. If the relevant values are colored red, the square is negated; otherwise,
        it is calculated by multiplying the values. The resulting square is formatted and assigned to the square
        column of the second row in each pair. Additionally, the method handles adding a new row, calculates the sum
        of square values, and sets the total square in the last row of the table.

        :parameter start_row: The starting row index for processing. Default is 0.

        :raises
            - ValueError: If a value conversion error occurs during calculations.
            - AttributeError: If an attribute error occurs while accessing table widget items.
            - UnboundLocalError: If a local variable is referenced before assignment.

        :return: None
        """

        try:
            if start_row >= self.tableWidget_m3.rowCount():

                # Add a new row at the end of the table
                last_row = self.tableWidget_m3.rowCount()
                self.tableWidget_m3.insertRow(last_row)

                # Insert sum_code
                sum_code = self.code()
                sum_code_item = QtWidgets.QTableWidgetItem(sum_code)
                self.tableWidget_m3.setItem(last_row, 0, sum_code_item)

                # Insert Trade letter
                trade_letter = self.code()[3]  # indexing to the 4th letter of the code.
                trade_letter_item = QtWidgets.QTableWidgetItem(trade_letter)
                self.tableWidget_m3.setItem(last_row, 1, trade_letter_item)

                # Set unit column as 'm3' for the last row
                unit_item = QtWidgets.QTableWidgetItem("m3")
                unit_item.setForeground(QtGui.QColor("blue"))
                flags = unit_item.flags()
                flags &= ~QtCore.Qt.ItemFlag.ItemIsEditable
                flags &= ~QtCore.Qt.ItemFlag.ItemIsSelectable
                unit_item.setFlags(flags)
                self.tableWidget_m3.setItem(last_row, 7, unit_item)

                # Set sign_post column as 'sum' for the last row
                desc_item = QtWidgets.QTableWidgetItem("SUM")
                desc_item.setForeground(QtGui.QColor("blue"))
                flags = desc_item.flags()
                flags &= ~QtCore.Qt.ItemFlag.ItemIsEditable
                flags &= ~QtCore.Qt.ItemFlag.ItemIsSelectable
                desc_item.setFlags(flags)
                self.tableWidget_m3.setItem(last_row, 8, desc_item)

                # Sum the numbers in the square column
                total_square = 0.0
                for row in range(self.tableWidget_m3.rowCount()):
                    square_item = self.tableWidget_m3.item(row, 6)
                    if square_item is not None:
                        square_value = square_item.text().replace(",", "")
                        if square_value.strip() != "":
                            total_square += float(square_value)

                # print(total_square)

                # Set the total square in the last row's square column
                total_item = QtWidgets.QTableWidgetItem("{:,.2f}".format(total_square))
                total_item.setForeground(QtGui.QColor("blue"))
                flags = total_item.flags()
                flags &= ~QtCore.Qt.ItemFlag.ItemIsEditable
                flags &= ~QtCore.Qt.ItemFlag.ItemIsSelectable
                total_item.setFlags(flags)
                self.tableWidget_m3.setItem(last_row, 6, total_item)

                # Iterate through all rows and columns
                for row in range(self.tableWidget_m3.rowCount()):
                    for column in range(self.tableWidget_m3.columnCount()):
                        item = self.tableWidget_m3.item(row, column)
                        if item is not None and item.text() == "SUM":
                            # Found the cell containing "SUM", make the entire row's foreground color blue
                            for col in range(self.tableWidget_m3.columnCount()):
                                cell_item = self.tableWidget_m3.item(row, col)
                                cell_item.setForeground(QtGui.QColor("blue"))
                            break  # Exit the inner loop once "SUM" is found

                return  # Base case: stop recursion when all rows have been processed

            times_item = self.tableWidget_m3.item(start_row, 4)
            times_value = times_item.text()

            # Check if times value is empty
            if times_value.strip() == "":
                times_item.setText("1.00 /")  # Set default value of "1.00 /"
            else:
                times = float(times_value.rstrip(" /"))
                times_item.setText("{:,.2f} /".format(times))

            dims_m3_len_item = self.tableWidget_m3.item(start_row, 5)
            dims_m3_len = float(dims_m3_len_item.text())
            dims_m3_len_item.setText("{:,.2f}".format(dims_m3_len))

            # Add 1 to row for width_row increment
            width_row = start_row + 1

            dims_m3_width_item = self.tableWidget_m3.item(width_row, 5)  # width_row increments by 1
            dims_m3_width = float(dims_m3_width_item.text())
            dims_m3_width_item.setText("{:,.2f}".format(dims_m3_width))

            # Add 1 to row for depth_row increment
            depth_row = width_row + 1

            dims_m3_depth_item = self.tableWidget_m3.item(depth_row, 5)  # width_row increments by 1
            dims_m3_depth = float(dims_m3_depth_item.text())
            dims_m3_depth_item.setText("{:,.2f}".format(dims_m3_depth))

            # Calculate square
            square = round(times * dims_m3_len * dims_m3_width * dims_m3_depth, 2)

            # Check if times and dims values are colored red
            if times_item.foreground().color().name() == "#ff0000" \
                    and dims_m3_len_item.foreground().color().name() == "#ff0000" \
                    and dims_m3_width_item.foreground().color().name() == "#ff0000":

                square *= -1  # Negate square
                item = QtWidgets.QTableWidgetItem("{:,.2f}".format(square))
                item.setForeground(QtGui.QColor("red"))  # Set the foreground color to red
            else:
                item = QtWidgets.QTableWidgetItem("{:,.2f}".format(square))
                item.setForeground(QtGui.QColor("black"))  # Set the foreground color to black

            # Freeze the cell
            flags = item.flags()
            flags &= ~QtCore.Qt.ItemFlag.ItemIsEditable
            flags &= ~QtCore.Qt.ItemFlag.ItemIsSelectable
            item.setFlags(flags)

            # Set the square for row and col at width_row
            self.tableWidget_m3.setItem(depth_row, 6, item)

            # Recursive call to process the next set of rows
            self.square(start_row + 3)

        except ValueError:
            return
        except AttributeError:
            return
        except UnboundLocalError:
            return

    def clear_table(self):
        self.tableWidget_m3.clearContents()
        self.tableWidget_m3.setRowCount(0)

        # If all rows are cleared, activate the lineEdit_desc item
        self.lineEdit_desc.clear()
        self.lineEdit_desc.setEnabled(True)

        # Reset to ---Select Trade---
        self.comboBox.setCurrentIndex(0)

        # Activate comboBox item
        self.comboBox.setEnabled(True)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("tabWidget_m3", "tabWidget_m3"))

        self.groupBox_m3.setTitle(_translate("tabWidget_m3", "Cubic measurement"))

        self.label_4.setText(_translate("tabWidget_m3", "Desc :"))
        self.label_5.setText(_translate("tabWidget_m3", "Trade : "))
        self.comboBox.setItemText(0, _translate("tabWidget_m3", "--- Select Trade ---"))
        self.comboBox.setItemText(1, _translate("tabWidget_m3", "A - Preliminaries/General conditions"))
        self.comboBox.setItemText(2, _translate("tabWidget_m3", "C - Existing site/buildings/services"))
        self.comboBox.setItemText(3, _translate("tabWidget_m3", "D - Groundwork"))
        self.comboBox.setItemText(4, _translate("tabWidget_m3", "E - In situ concrete/Large precast concrete"))
        self.comboBox.setItemText(5, _translate("tabWidget_m3", "F - Masonry"))
        self.comboBox.setItemText(6, _translate("tabWidget_m3", "G - Structural/Carcassing metal/timber"))
        self.comboBox.setItemText(7, _translate("tabWidget_m3", "H - Cladding"))
        self.comboBox.setItemText(8, _translate("tabWidget_m3", "J - Waterproofing"))
        self.comboBox.setItemText(9, _translate("tabWidget_m3", "K - Linings/Sheathing/Dry partitioning"))
        self.comboBox.setItemText(10, _translate("tabWidget_m3", "L - Windows/Doors/Stairs"))
        self.comboBox.setItemText(11, _translate("tabWidget_m3", "M - Surface finishes"))
        self.comboBox.setItemText(12, _translate("tabWidget_m3", "N - Furniture/Equipment"))
        self.comboBox.setItemText(13, _translate("tabWidget_m3", "P - Building fabric sundries"))
        self.comboBox.setItemText(14, _translate("tabWidget_m3", "Q - Paving/Planting/Fencing/Site furniture"))
        self.comboBox.setItemText(15, _translate("tabWidget_m3", "R - Disposal systems"))
        self.comboBox.setItemText(16, _translate("tabWidget_m3", "S - Piped Supply systems"))
        self.comboBox.setItemText(17, _translate("tabWidget_m3", "T - Mechanical heating/Cooling/Refrigeration systems"))
        self.comboBox.setItemText(18, _translate("tabWidget_m3", "U - Ventilation/Air conditioning systems"))
        self.comboBox.setItemText(19, _translate("tabWidget_m3", "V - Electrical supply/power/lighting systems"))
        self.comboBox.setItemText(20, _translate("tabWidget_m3", "W - Communications/Security/Control systems"))
        self.comboBox.setItemText(21, _translate("tabWidget_m3", "X - Transport systems"))
        self.comboBox.setItemText(22, _translate("tabWidget_m3", "Y - Mechanical and electrical services measurement"))

        self.label_6.setText(_translate("tabWidget_m3", "Code :"))
        self.label_code.setText(_translate("tabWidget_m3", ""))
        self.pushButton_m3_add.setText(_translate("tabWidget_m3", "Add"))
        self.pushButton_m3_ddt.setText(_translate("tabWidget_m3", "Deduct"))
        self.pushButton_m3_del.setText(_translate("tabWidget_m3", "Delete"))
        self.pushButton_m3_sqr.setText(_translate("tabWidget_m3", "Square"))
        item = self.tableWidget_m3.horizontalHeaderItem(0)
        item.setText(_translate("tabWidget_m3", "code"))
        self.tableWidget_m3.setColumnWidth(0, 60)
        item = self.tableWidget_m3.horizontalHeaderItem(1)
        item.setText(_translate("tabWidget_m3", "trade"))
        self.tableWidget_m3.setColumnWidth(1, 40)
        item = self.tableWidget_m3.horizontalHeaderItem(2)
        item.setText(_translate("tabWidget_m3", "description"))
        self.tableWidget_m3.setColumnWidth(2, 250)
        item = self.tableWidget_m3.horizontalHeaderItem(3)
        item.setText(_translate("tabWidget_m3", "ref"))
        self.tableWidget_m3.setColumnWidth(3, 60)
        item = self.tableWidget_m3.horizontalHeaderItem(4)
        item.setText(_translate("tabWidget_m3", "times"))
        self.tableWidget_m3.setColumnWidth(4, 60)
        item = self.tableWidget_m3.horizontalHeaderItem(5)
        item.setText(_translate("tabWidget_m3", "dims"))
        self.tableWidget_m3.setColumnWidth(5, 60)
        item = self.tableWidget_m3.horizontalHeaderItem(6)
        item.setText(_translate("tabWidget_m3", "square"))
        self.tableWidget_m3.setColumnWidth(6, 60)
        item = self.tableWidget_m3.horizontalHeaderItem(7)
        item.setText(_translate("tabWidget_m3", "unit"))
        self.tableWidget_m3.setColumnWidth(7, 30)
        item = self.tableWidget_m3.horizontalHeaderItem(8)
        item.setText(_translate("tabWidget_m3", "sign post"))
        self.tableWidget_m3.setColumnWidth(8, 100)

        self.pushButton_m3_clear.setText(_translate("tabWidget_m3", "Clear"))
        self.pushButton_m3_insert.setText(_translate("tabWidget_m3", "Insert"))

    def on_resize(self, event):
        # Get the screen resolution
        screen = QtWidgets.QApplication.primaryScreen()
        screen_geometry = screen.geometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()

        # Define the proportions for each column (half of the original width)
        original_column_widths = [60, 40, 250, 60, 60, 60, 60, 30, 100]

        if screen_width < 1920 or screen_height < 1080:
            # Calculate the reduction factor based on screen resolution
            reduction_factor = min(screen_width / 1920, screen_height / 1080)

            # Reduce the column widths by applying the reduction factor
            column_widths = [int(width * reduction_factor * 1.15) for width in original_column_widths]

            # # Set the font size to 8
            # font = QtGui.QFont()
            # font.setPointSize(8)
            # self.tableWidget_m2.setFont(font)

            # Reduce the size of the groupBox geometry by applying the reduction factor
            current_geometry = self.groupBox_m3.geometry()
            new_width = int(current_geometry.width() * reduction_factor * 1.199)
            new_height = int(current_geometry.height() * reduction_factor * 1.11)  # TODO: To make responsive
            new_geometry = QtCore.QRect(current_geometry.x(), current_geometry.y(), new_width, new_height)
            self.groupBox_m3.setGeometry(new_geometry)

        else:
            column_widths = original_column_widths

        # Distribute the available width among columns proportionally
        for col, width in enumerate(column_widths):
            self.tableWidget_m3.setColumnWidth(col, width)

        # Call the base class's resize event handler
        super().resizeEvent(event)


    def save_table_data(self):
        # Import the return of self.code here as code_string
        code_string = self.code()

        # Check if code_string is valid
        if not code_string:
            QMessageBox.critical(self, "Invalid Table Name", "Invalid table name.")
            return

        # Determine the current working directory
        current_directory = os.getcwd()

        # Check if "/Data/Storages/Local/Jobs" is not present in the file path  => for MAC
        if "\Data\Storages\Local\Jobs" not in current_directory:  # => for PC
            QMessageBox.critical(self, "Invalid Directory", "Data can only be saved in the Jobs directory. Create a "
                                                            "new Job or open an existing one to save.")
            return

        # Connect to the SQLite database
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()

        # Create the table if it doesn't exist
        try:
            cursor.execute(f'''
                CREATE TABLE IF NOT EXISTS {code_string} (
                    id     INTEGER PRIMARY KEY AUTOINCREMENT,
                    code   TEXT,
                    trade  TEXT,
                    desc   TEXT,
                    ref    TEXT,
                    times  TEXT,
                    dims   TEXT,
                    square INTEGER,
                    unit   TEXT,
                    sign_post TEXT,
                    UNIQUE(id)
                )
            ''')
        except sqlite3.OperationalError:
            return

        # Get the number of rows and columns in the table widget
        num_rows = self.tableWidget_m3.rowCount()
        num_columns = self.tableWidget_m3.columnCount()

        # Iterate over each row in the table widget and insert the data into the database
        for row in range(num_rows):
            data = []
            for col in range(num_columns):
                item = self.tableWidget_m3.item(row, col)
                if item is not None:
                    data.append(item.text())
                else:
                    data.append('')

            # Insert the row data into the database
            try:
                cursor.execute(f'''
                    INSERT INTO {code_string} (code, trade, desc, ref, times, dims, square, unit, sign_post)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', tuple(data))
            except sqlite3.Error as e:
                print(f"Error inserting row {row}: {e}")

        # Commit the changes and close the database connection
        conn.commit()
        conn.close()

    def insert_dialog(self):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("Insert")
        msg_box.setText("Click OK to insert into the Take Off sheet and click Refresh to show.")

        # Icon with relative path
        icon1 = QtGui.QIcon()
        image_path_to_icon1 = os.path.join(os.path.dirname(__file__), "images", "STO_IconPix.png")
        icon1.addPixmap(QtGui.QPixmap(image_path_to_icon1), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        msg_box.setWindowIcon(icon1)

        # Add button icon with relative path
        icon_path = os.path.join(os.path.dirname(__file__), "images", "info.png")
        icon_pixmap = QtGui.QPixmap(icon_path)
        msg_box.setIconPixmap(icon_pixmap)

        msg_box.setStandardButtons(
            QtWidgets.QMessageBox.StandardButton.Ok | QtWidgets.QMessageBox.StandardButton.Cancel
        )
        result = msg_box.exec()

        if result == QtWidgets.QMessageBox.StandardButton.Ok:
            # Perform the insertion into the TakeOff sheet
            self.save_table_data()
            self.load_table_data()

        else:
            # User clicked Cancel, do nothing or perform any desired action
            pass

    def load_table_data(self):
        take_off_sheet = TakeOffSheet_Widget()  # Create an instance of TakeOffSheet_Widget
        take_off_sheet.load_table_data()  # Call the method to load data from table
