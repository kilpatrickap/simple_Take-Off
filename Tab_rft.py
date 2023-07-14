import os.path
import sqlite3
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QTableWidgetItem, QTableWidget
from TakeOffSheet import TakeOffSheet_Widget


class Tab_rft_Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.groupBox_rft = QtWidgets.QGroupBox(parent=self)
        self.groupBox_rft.setGeometry(QtCore.QRect(10, 10, 751, 501))
        self.groupBox_rft.setObjectName("groupBox_rft")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_rft)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_rft)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)

        self.lineEdit_desc = QtWidgets.QLineEdit(parent=self.groupBox_rft)
        self.lineEdit_desc.setObjectName("lineEdit_desc")

        # Connect signal
        self.lineEdit_desc.returnPressed.connect(self.desc)

        self.horizontalLayout_7.addWidget(self.lineEdit_desc)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_rft)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)

        self.comboBox = QtWidgets.QComboBox(parent=self.groupBox_rft)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        # Connect signal
        self.comboBox.currentIndexChanged.connect(self.trade)

        self.horizontalLayout.addWidget(self.comboBox)
        spacerItem1 = QtWidgets.QSpacerItem(260, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)

        # Weight Label and LineEdit inside a horizontal layout
        self.label_weight = QtWidgets.QLabel(parent=self.groupBox_rft)
        self.label_weight.setObjectName("label_weight")

        self.lineEdit_weight = QtWidgets.QLineEdit(parent=self.groupBox_rft)
        self.lineEdit_weight.setObjectName("lineEdit_weight")

        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayout.addWidget(self.label_weight)
        self.horizontalLayout.addWidget(self.lineEdit_weight)

        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox_rft)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.label_code = QtWidgets.QLabel(parent=self.groupBox_rft)
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

        self.pushButton_rft_add = QtWidgets.QPushButton(parent=self.groupBox_rft)

        # Add button icon with relative path
        icon1 = QtGui.QIcon()
        image_path_to_icon1 = os.path.join(os.path.dirname(__file__), "images", "plus.png")
        icon1.addPixmap(QtGui.QPixmap(image_path_to_icon1), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_rft_add.setIcon(icon1)

        self.pushButton_rft_add.setObjectName("pushButton_rft_add")

        # Connect signal
        self.pushButton_rft_add.clicked.connect(self.add_row)

        self.horizontalLayout_10.addWidget(self.pushButton_rft_add)
        self.pushButton_rft_ddt = QtWidgets.QPushButton(parent=self.groupBox_rft)

        # Deduct button icon with relative path
        icon2 = QtGui.QIcon()
        image_path_to_icon2 = os.path.join(os.path.dirname(__file__), "images", "minus.png")
        icon2.addPixmap(QtGui.QPixmap(image_path_to_icon2), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_rft_ddt.setIcon(icon2)

        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.pushButton_rft_ddt.setFont(font)
        self.pushButton_rft_ddt.setObjectName("pushButton_rft_ddt")

        # Connect signal
        self.pushButton_rft_ddt.clicked.connect(self.ddt_row)
        self.pushButton_rft_ddt.setStyleSheet("color: red")

        self.horizontalLayout_10.addWidget(self.pushButton_rft_ddt)
        self.pushButton_rft_del = QtWidgets.QPushButton(parent=self.groupBox_rft)

        # Delete button icon with relative path
        icon3 = QtGui.QIcon()
        image_path_to_icon3 = os.path.join(os.path.dirname(__file__), "images", "cross.png")
        icon3.addPixmap(QtGui.QPixmap(image_path_to_icon3), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_rft_del.setIcon(icon3)

        self.pushButton_rft_del.setObjectName("pushButton_rft_del")

        # Connect signal
        self.pushButton_rft_del.clicked.connect(self.delete_row)

        self.horizontalLayout_10.addWidget(self.pushButton_rft_del)

        self.pushButton_rft_sqr = QtWidgets.QPushButton(parent=self.groupBox_rft)

        # Square button icon with relative path
        icon4 = QtGui.QIcon()
        image_path_to_icon4 = os.path.join(os.path.dirname(__file__), "images", "calculator.png")
        icon4.addPixmap(QtGui.QPixmap(image_path_to_icon4), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_rft_sqr.setIcon(icon4)

        self.pushButton_rft_sqr.setObjectName("pushButton_rft_sqr")

        # Connect signal
        self.pushButton_rft_sqr.clicked.connect(self.square)

        self.horizontalLayout_10.addWidget(self.pushButton_rft_sqr)

        # Horizontal spacer
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)

        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.tableWidget_rft = QtWidgets.QTableWidget(parent=self.groupBox_rft)
        self.tableWidget_rft.setObjectName("tableWidget_rft")
        self.tableWidget_rft.setColumnCount(9)
        self.tableWidget_rft.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_rft.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_rft.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_rft.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_rft.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_rft.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_rft.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_rft.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_rft.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_rft.setHorizontalHeaderItem(8, item)
        self.verticalLayout.addWidget(self.tableWidget_rft)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")

        # Horizontal spacer
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem3)

        self.pushButton_rft_clear = QtWidgets.QPushButton(parent=self.groupBox_rft)

        # Clear button icon with relative path
        icon5 = QtGui.QIcon()
        image_path_to_icon5 = os.path.join(os.path.dirname(__file__), "images", "application-blue.png")
        icon5.addPixmap(QtGui.QPixmap(image_path_to_icon5), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_rft_clear.setIcon(icon5)

        self.pushButton_rft_clear.setObjectName("pushButton_rft_clear")

        # Connect signal
        self.pushButton_rft_clear.clicked.connect(self.clear_table)

        self.horizontalLayout_11.addWidget(self.pushButton_rft_clear)
        self.pushButton_rft_insert = QtWidgets.QPushButton(parent=self.groupBox_rft)

        # Insert button icon with relative path
        icon6 = QtGui.QIcon()
        image_path_to_icon6 = os.path.join(os.path.dirname(__file__), "images", "table-export.png")
        icon6.addPixmap(QtGui.QPixmap(image_path_to_icon6), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_rft_insert.setIcon(icon6)

        self.pushButton_rft_insert.setObjectName("pushButton_rft_insert")

        # Connect signals
        self.pushButton_rft_insert.clicked.connect(self.insert_dialog)

        self.horizontalLayout_11.addWidget(self.pushButton_rft_insert)

        # Horizontal spacer
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem4)

        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def desc(self):
        desc_text = self.lineEdit_desc.text()

        # Set the entered string in the "desc" column of the new row
        desc_item = QtWidgets.QTableWidgetItem(desc_text)
        self.tableWidget_rft.setItem(0, 2, desc_item)

        # de-activate lineEdit_desc item
        self.lineEdit_desc.setEnabled(False)

    def trade(self):
        selected_item = self.comboBox.currentText()  # Retrieve the selected item from the comboBox
        first_letter = selected_item[0]  # Get the first letter of the selected item

        row_index = 0  # the row index of the selected item

        # Set the first letter in the trade column of the tableWidget_rft
        trade_item = QtWidgets.QTableWidgetItem(first_letter)
        self.tableWidget_rft.setItem(row_index, 1, trade_item)

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
                        AND name LIKE 'rft_E%'
                        OR name LIKE 'rft_G%'
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
        code_string = f"rft_{first_letter}{next_code_number}"
        self.label_code.setText(code_string)  # Update the label "code shows up here" with the generated code

        # Set the code in the code column of the tableWidget_rft
        code_item = QtWidgets.QTableWidgetItem(code_string)
        self.tableWidget_rft.setItem(0, 0, code_item)

        return code_string  # returns e.g rft_M1, rft_D1 etc as type str

    def add_row(self):
        current_row = self.tableWidget_rft.currentRow()  # Get the current row index.

        unit_rft = "m"  # Set the unit
        unit_rft_cell = QtWidgets.QTableWidgetItem(unit_rft)

        new_row = self.tableWidget_rft.rowCount()  # Insert one new row at the end of the table
        self.tableWidget_rft.insertRow(new_row)

        flags = unit_rft_cell.flags()  # Freeze cell
        flags &= ~QtCore.Qt.ItemFlag.ItemIsEditable  # set the cell as read-only
        flags &= ~QtCore.Qt.ItemFlag.ItemIsSelectable  # disable cell selection
        unit_rft_cell.setFlags(flags)

        self.tableWidget_rft.setItem(0, 7, unit_rft_cell)  # set the unit

        # Copy the formatting and logic from the previous row to the new row
        for column in range(self.tableWidget_rft.columnCount()):
            item = self.tableWidget_rft.item(current_row, column)
            if item is not None:
                new_item = QtWidgets.QTableWidgetItem(item.text())
                flags = item.flags()
                new_item.setFlags(flags)
                self.tableWidget_rft.setItem(new_row, column, new_item)

    def ddt_row(self):
        current_row = self.tableWidget_rft.rowCount() - 1  # Get the current row index

        unit_rft = "m"  # Set the unit
        unit_rft_cell = QtWidgets.QTableWidgetItem(unit_rft)
        unit_rft_cell.setForeground(QtGui.QColor("red"))  # Set the text color to red

        new_row = self.tableWidget_rft.rowCount()  # Insert one new row at the end of the table
        self.tableWidget_rft.insertRow(new_row)

        flags = unit_rft_cell.flags()  # Freeze cell
        flags &= ~QtCore.Qt.ItemFlag.ItemIsEditable  # set the cell as read-only
        flags &= ~QtCore.Qt.ItemFlag.ItemIsSelectable  # disable cell selection
        unit_rft_cell.setFlags(flags)

        self.tableWidget_rft.setItem(new_row, 7, unit_rft_cell)  # set the unit

        # Copy the formatting and logic from the previous row to the new row
        for column in range(self.tableWidget_rft.columnCount()):
            item = self.tableWidget_rft.item(current_row, column)
            if item is not None:
                new_item = QtWidgets.QTableWidgetItem(item.text())
                new_item.setForeground(QtGui.QColor("red"))  # Set the text color to red
                flags = item.flags()
                new_item.setFlags(flags)

                # Check if the current column is the square cell (column index 6)
                if column == 6:
                    try:
                        # Convert the value to a negative number
                        value = float(new_item.text())
                        formatted_value = "{:,.2f}".format(-value)  # Format the value with pattern "{:,.2f}"
                        new_item.setText(formatted_value)
                    except ValueError:
                        return

                self.tableWidget_rft.setItem(new_row, column, new_item)

    def delete_row(self):
        current_row = self.tableWidget_rft.currentRow()
        self.tableWidget_rft.removeRow(current_row)

        # If all rows are deleted, activate the lineEdit_desc item
        self.lineEdit_desc.setEnabled(True)

        # Activate comboBox item
        self.comboBox.setEnabled(True)

    def square(self):
        try:
            for row in range(self.tableWidget_rft.rowCount()):
                times_item = self.tableWidget_rft.item(row, 4)
                times_value = times_item.text()

                """ When times and dims is >= 1,000.00 in any of the rows, tableWidget can't square"""

                # Check if times value is empty
                if times_value.strip() == "":
                    times_item.setText("1.00 /")  # Set default value of "1.00 /"
                else:
                    times = float(times_value.rstrip(" /"))
                    times_item.setText("{:,.2f} /".format(times))

                dims_item = self.tableWidget_rft.item(row, 5)
                dims = float(dims_item.text())
                dims_item.setText("{:,.2f}".format(dims))

                # Calculate square
                square = round(times * dims, 2)

                # Check if times and dims values are colored red
                if times_item.foreground().color().name() == "#ff0000" and dims_item.foreground().color().name() == "#ff0000":
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

                # Set the square for row and col
                self.tableWidget_rft.setItem(row, 6, item)

            # Add a new row at the end
            last_row = self.tableWidget_rft.rowCount()
            self.tableWidget_rft.insertRow(last_row)

            # Insert sum_code
            sum_code = self.code()
            sum_code_item = QtWidgets.QTableWidgetItem(sum_code)
            self.tableWidget_rft.setItem(last_row, 0, sum_code_item)

            # Insert Trade letter
            trade_letter = self.code()[4]  # indexing to the 5th letter of the code.
            trade_letter_item = QtWidgets.QTableWidgetItem(trade_letter)
            self.tableWidget_rft.setItem(last_row, 1, trade_letter_item)

            # Set unit column as 'm' for the last row
            unit_item = QtWidgets.QTableWidgetItem("m")
            flags = unit_item.flags()
            flags &= ~QtCore.Qt.ItemFlag.ItemIsEditable
            flags &= ~QtCore.Qt.ItemFlag.ItemIsSelectable
            unit_item.setFlags(flags)
            self.tableWidget_rft.setItem(last_row, 7, unit_item)

            # Set description column as 'sum' for the last row
            desc_item = QtWidgets.QTableWidgetItem("SUM")
            flags = desc_item.flags()
            flags &= ~QtCore.Qt.ItemFlag.ItemIsEditable
            flags &= ~QtCore.Qt.ItemFlag.ItemIsSelectable
            desc_item.setFlags(flags)
            self.tableWidget_rft.setItem(last_row, 8, desc_item)

            # Sum the numbers in the square column
            total_square = 0.0
            for row in range(self.tableWidget_rft.rowCount() - 1):
                square_item = self.tableWidget_rft.item(row, 6)
                square_value = square_item.text().replace(",", "")
                total_square += float(square_value)     # Sum the square col

            # Set the total square in the last row's square column
            total_item = QtWidgets.QTableWidgetItem("{:,.2f}".format(total_square))
            flags = total_item.flags()
            flags &= ~QtCore.Qt.ItemFlag.ItemIsEditable
            flags &= ~QtCore.Qt.ItemFlag.ItemIsSelectable
            total_item.setFlags(flags)
            self.tableWidget_rft.setItem(last_row, 6, total_item)

            #--- CREATE A NEW ROW FOR TONNAGE CONVERSION ---

            # Add a new row at the end
            last_row = self.tableWidget_rft.rowCount()
            self.tableWidget_rft.insertRow(last_row)

            # Insert sum_code
            sum_code = self.code()
            sum_code_item = QtWidgets.QTableWidgetItem(sum_code)
            self.tableWidget_rft.setItem(last_row, 0, sum_code_item)

            # Insert Trade letter
            trade_letter = self.code()[4]  # indexing to the 5th letter of the code.
            trade_letter_item = QtWidgets.QTableWidgetItem(trade_letter)
            self.tableWidget_rft.setItem(last_row, 1, trade_letter_item)

            # Set weight for the last row
            entered_weight = self.lineEdit_weight.text()
            entered_weight_item = QtWidgets.QTableWidgetItem(entered_weight)
            self.tableWidget_rft.setItem(last_row, 5, entered_weight_item)

            # Set unit column as 'm' for the last row
            unit_item = QtWidgets.QTableWidgetItem("t")
            flags = unit_item.flags()
            flags &= ~QtCore.Qt.ItemFlag.ItemIsEditable
            flags &= ~QtCore.Qt.ItemFlag.ItemIsSelectable
            unit_item.setFlags(flags)
            self.tableWidget_rft.setItem(last_row, 7, unit_item)

            # Set description column as 'sum' for the last row
            desc_item = QtWidgets.QTableWidgetItem("TONNAGE")
            flags = desc_item.flags()
            flags &= ~QtCore.Qt.ItemFlag.ItemIsEditable
            flags &= ~QtCore.Qt.ItemFlag.ItemIsSelectable
            desc_item.setFlags(flags)
            self.tableWidget_rft.setItem(last_row, 8, desc_item)

            # Convert to Tonnage
            weight = float(entered_weight)
            total_square *= weight / 1000.0

            # Set the total square in the last row's square column
            total_item = QtWidgets.QTableWidgetItem("{:,.2f}".format(total_square))
            flags = total_item.flags()
            flags &= ~QtCore.Qt.ItemFlag.ItemIsEditable
            flags &= ~QtCore.Qt.ItemFlag.ItemIsSelectable
            total_item.setFlags(flags)
            self.tableWidget_rft.setItem(last_row, 6, total_item)

        except ValueError:
            return
        except AttributeError:
            return
        except UnboundLocalError:
            return

    def clear_table(self):
        self.tableWidget_rft.clearContents()
        self.tableWidget_rft.setRowCount(0)

        # If all rows are cleared, activate the lineEdit_desc item
        self.lineEdit_desc.clear()
        self.lineEdit_desc.setEnabled(True)

        # Reset to ---Select Trade---
        self.comboBox.setCurrentIndex(0)

        # Activate comboBox item
        self.comboBox.setEnabled(True)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("tabWidget_rft", "tabWidget_rft"))

        self.groupBox_rft.setTitle(_translate("tabWidget_rft", "Reinforcement measurement"))

        self.label_4.setText(_translate("tabWidget_rft", "Desc :"))
        self.label_5.setText(_translate("tabWidget_rft", "Trade : "))
        self.comboBox.setItemText(0, _translate("tabWidget_rft", "--- Select Trade ---"))
        self.comboBox.setItemText(1, _translate("tabWidget_rft", "E - In situ concrete/Large precast concrete"))
        self.comboBox.setItemText(2, _translate("tabWidget_rft", "G - Structural/Carcassing metal/timber"))

        self.label_6.setText(_translate("tabWidget_rft", "Code :"))
        self.label_weight.setText(_translate("tabWidget_rft", "Weight (kg/m):"))
        self.lineEdit_weight.setPlaceholderText(_translate("tabWidget_rft", "e.g 0.888"))
        self.label_code.setText(_translate("tabWidget_rft", "\"code shows up here\""))
        self.pushButton_rft_add.setText(_translate("tabWidget_rft", "Add"))
        self.pushButton_rft_ddt.setText(_translate("tabWidget_rft", "Deduct"))
        self.pushButton_rft_del.setText(_translate("tabWidget_rft", "Delete"))
        self.pushButton_rft_sqr.setText(_translate("tabWidget_rft", "Square"))
        item = self.tableWidget_rft.horizontalHeaderItem(0)
        item.setText(_translate("tabWidget_rft", "code"))
        self.tableWidget_rft.setColumnWidth(0, 60)
        item = self.tableWidget_rft.horizontalHeaderItem(1)
        item.setText(_translate("tabWidget_rft", "trade"))
        self.tableWidget_rft.setColumnWidth(1, 40)
        item = self.tableWidget_rft.horizontalHeaderItem(2)
        item.setText(_translate("tabWidget_rft", "desc"))
        self.tableWidget_rft.setColumnWidth(2, 250)
        item = self.tableWidget_rft.horizontalHeaderItem(3)
        item.setText(_translate("tabWidget_rft", "ref"))
        self.tableWidget_rft.setColumnWidth(3, 60)
        item = self.tableWidget_rft.horizontalHeaderItem(4)
        item.setText(_translate("tabWidget_rft", "times"))
        self.tableWidget_rft.setColumnWidth(4, 60)
        item = self.tableWidget_rft.horizontalHeaderItem(5)
        item.setText(_translate("tabWidget_rft", "dims"))
        self.tableWidget_rft.setColumnWidth(5, 60)
        item = self.tableWidget_rft.horizontalHeaderItem(6)
        item.setText(_translate("tabWidget_rft", "square"))
        self.tableWidget_rft.setColumnWidth(6, 60)
        item = self.tableWidget_rft.horizontalHeaderItem(7)
        item.setText(_translate("tabWidget_rft", "unit"))
        self.tableWidget_rft.setColumnWidth(7, 30)
        item = self.tableWidget_rft.horizontalHeaderItem(8)
        item.setText(_translate("tabWidget_rft", "sign post"))
        self.tableWidget_rft.setColumnWidth(8, 100)

        self.pushButton_rft_clear.setText(_translate("tabWidget_rft", "Clear"))
        self.pushButton_rft_insert.setText(_translate("tabWidget_rft", "Insert"))

    def save_table_data(self):
        # Import the return of self.code here as code_string
        code_string = self.code()

        # Check if code_string is valid
        if not code_string:
            print("Invalid table name")
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
        num_rows = self.tableWidget_rft.rowCount()
        num_columns = self.tableWidget_rft.columnCount()

        # Iterate over each row in the table widget and insert the data into the database
        for row in range(num_rows):
            data = []
            for col in range(num_columns):
                item = self.tableWidget_rft.item(row, col)
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

        # Add button icon with relative path
        icon_path = os.path.join(os.path.dirname(__file__), "images", "information.png")
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
            self.save_takeOff_database()

        else:
            # User clicked Cancel, do nothing or perform any desired action
            pass

    def load_table_data(self):
        take_off_sheet = TakeOffSheet_Widget()  # Create an instance of TakeOffSheet_Widget
        take_off_sheet.load_table_data()  # Call the method to load data from table

    def save_takeOff_database(self):
        take_off_sheet = TakeOffSheet_Widget()  # Create an instance of TakeOffSheet_Widget
        take_off_sheet.save_takeOff_database()  # Call the method to save data from table
