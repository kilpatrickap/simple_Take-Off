import os.path
import sqlite3
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QTableWidgetItem, QTableWidget
from TakeOffSheet import TakeOffSheet_Widget


class Tab_m_Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.groupBox_m = QtWidgets.QGroupBox(parent=self)
        self.groupBox_m.setGeometry(QtCore.QRect(10, 10, 751, 501))
        self.groupBox_m.setObjectName("groupBox_m")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_m)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_m)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)

        self.lineEdit_desc = QtWidgets.QLineEdit(parent=self.groupBox_m)
        self.lineEdit_desc.setObjectName("lineEdit_desc")

        # Connect signal
        self.lineEdit_desc.returnPressed.connect(self.desc)

        self.horizontalLayout_7.addWidget(self.lineEdit_desc)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_m)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)

        self.comboBox = QtWidgets.QComboBox(parent=self.groupBox_m)
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
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox_m)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.label_code = QtWidgets.QLabel(parent=self.groupBox_m)
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

        self.pushButton_m_add = QtWidgets.QPushButton(parent=self.groupBox_m)

        # Add button icon with relative path
        icon1 = QtGui.QIcon()
        image_path_to_icon1 = os.path.join(os.path.dirname(__file__), "images", "plus.png")
        icon1.addPixmap(QtGui.QPixmap(image_path_to_icon1), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_m_add.setIcon(icon1)

        self.pushButton_m_add.setObjectName("pushButton_m_add")

        # Connect signal
        self.pushButton_m_add.clicked.connect(self.add_row)

        self.horizontalLayout_10.addWidget(self.pushButton_m_add)
        self.pushButton_m_ddt = QtWidgets.QPushButton(parent=self.groupBox_m)

        # Deduct button icon with relative path
        icon2 = QtGui.QIcon()
        image_path_to_icon2 = os.path.join(os.path.dirname(__file__), "images", "minus.png")
        icon2.addPixmap(QtGui.QPixmap(image_path_to_icon2), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_m_ddt.setIcon(icon2)

        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.pushButton_m_ddt.setFont(font)
        self.pushButton_m_ddt.setObjectName("pushButton_m_ddt")

        # Connect signal
        self.pushButton_m_ddt.clicked.connect(self.ddt_row)
        self.pushButton_m_ddt.setStyleSheet("color: red")

        self.horizontalLayout_10.addWidget(self.pushButton_m_ddt)
        self.pushButton_m_del = QtWidgets.QPushButton(parent=self.groupBox_m)

        # Delete button icon with relative path
        icon3 = QtGui.QIcon()
        image_path_to_icon3 = os.path.join(os.path.dirname(__file__), "images", "cross.png")
        icon3.addPixmap(QtGui.QPixmap(image_path_to_icon3), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_m_del.setIcon(icon3)

        self.pushButton_m_del.setObjectName("pushButton_m_del")

        # Connect signal
        self.pushButton_m_del.clicked.connect(self.delete_row)

        self.horizontalLayout_10.addWidget(self.pushButton_m_del)

        self.pushButton_m_sqr = QtWidgets.QPushButton(parent=self.groupBox_m)

        # Square button icon with relative path
        icon4 = QtGui.QIcon()
        image_path_to_icon4 = os.path.join(os.path.dirname(__file__), "images", "calculator.png")
        icon4.addPixmap(QtGui.QPixmap(image_path_to_icon4), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_m_sqr.setIcon(icon4)

        self.pushButton_m_sqr.setObjectName("pushButton_m_sqr")

        # Connect signal
        self.pushButton_m_sqr.clicked.connect(self.square)

        self.horizontalLayout_10.addWidget(self.pushButton_m_sqr)

        # Horizontal spacer
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)

        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.tableWidget_m = QtWidgets.QTableWidget(parent=self.groupBox_m)
        self.tableWidget_m.setObjectName("tableWidget_m")
        self.tableWidget_m.setColumnCount(9)
        self.tableWidget_m.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_m.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_m.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_m.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_m.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_m.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_m.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_m.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_m.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_m.setHorizontalHeaderItem(8, item)
        self.verticalLayout.addWidget(self.tableWidget_m)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")

        # Horizontal spacer
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem3)

        self.pushButton_m_clear = QtWidgets.QPushButton(parent=self.groupBox_m)

        # Clear button icon with relative path
        icon5 = QtGui.QIcon()
        image_path_to_icon5 = os.path.join(os.path.dirname(__file__), "images", "application-blue.png")
        icon5.addPixmap(QtGui.QPixmap(image_path_to_icon5), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_m_clear.setIcon(icon5)

        self.pushButton_m_clear.setObjectName("pushButton_m_clear")

        # Connect signal
        self.pushButton_m_clear.clicked.connect(self.clear_table)

        self.horizontalLayout_11.addWidget(self.pushButton_m_clear)
        self.pushButton_m_insert = QtWidgets.QPushButton(parent=self.groupBox_m)

        # Insert button icon with relative path
        icon6 = QtGui.QIcon()
        image_path_to_icon6 = os.path.join(os.path.dirname(__file__), "images", "table-export.png")
        icon6.addPixmap(QtGui.QPixmap(image_path_to_icon6), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_m_insert.setIcon(icon6)

        self.pushButton_m_insert.setObjectName("pushButton_m_insert")

        # Connect signals
        self.pushButton_m_insert.clicked.connect(self.insert_dialog)

        self.horizontalLayout_11.addWidget(self.pushButton_m_insert)

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
        self.tableWidget_m.setItem(0, 2, desc_item)

        # de-activate lineEdit_desc item
        self.lineEdit_desc.setEnabled(False)

    def trade(self):
        selected_item = self.comboBox.currentText()  # Retrieve the selected item from the comboBox
        first_letter = selected_item[0]  # Get the first letter of the selected item

        row_index = 0  # the row index of the selected item

        # Set the first letter in the trade column of the tableWidget_m
        trade_item = QtWidgets.QTableWidgetItem(first_letter)
        self.tableWidget_m.setItem(row_index, 1, trade_item)

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
                        AND name LIKE 'm_A%' 
                        OR name LIKE 'm_C%'
                        OR name LIKE 'm_D%'
                        OR name LIKE 'm_E%'
                        OR name LIKE 'm_F%'
                        OR name LIKE 'm_G%'
                        OR name LIKE 'm_H%'
                        OR name LIKE 'm_J%'
                        OR name LIKE 'm_K%'
                        OR name LIKE 'm_L%'
                        OR name LIKE 'm_M%'
                        OR name LIKE 'm_N%'
                        OR name LIKE 'm_P%'
                        OR name LIKE 'm_Q%'
                        OR name LIKE 'm_R%'
                        OR name LIKE 'm_S%'
                        OR name LIKE 'm_T%'
                        OR name LIKE 'm_U%'
                        OR name LIKE 'm_V%'
                        OR name LIKE 'm_W%'
                        OR name LIKE 'm_X%'
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
        code_string = f"m_{first_letter}{next_code_number}"
        self.label_code.setText(code_string)  # Update the label "code shows up here" with the generated code

        # Set the code in the code column of the tableWidget_m
        code_item = QtWidgets.QTableWidgetItem(code_string)
        self.tableWidget_m.setItem(0, 0, code_item)

        return code_string  # returns e.g m_M1, m_D1 etc as type str

    def add_row(self):
        current_row = self.tableWidget_m.currentRow()  # Get the current row index

        unit_m = "m"  # Set the unit
        unit_m_cell = QtWidgets.QTableWidgetItem(unit_m)

        new_row = self.tableWidget_m.rowCount()  # Insert one new row at the end of the table
        self.tableWidget_m.insertRow(new_row)

        flags = unit_m_cell.flags()  # Freeze cell
        flags &= ~QtCore.Qt.ItemFlag.ItemIsEditable  # set the cell as read-only
        flags &= ~QtCore.Qt.ItemFlag.ItemIsSelectable  # disable cell selection
        unit_m_cell.setFlags(flags)

        self.tableWidget_m.setItem(0, 7, unit_m_cell)  # set the unit

        # Copy the formatting and logic from the previous row to the new row
        for column in range(self.tableWidget_m.columnCount()):
            item = self.tableWidget_m.item(current_row, column)
            if item is not None:
                new_item = QtWidgets.QTableWidgetItem(item.text())
                flags = item.flags()
                new_item.setFlags(flags)
                self.tableWidget_m.setItem(new_row, column, new_item)

    def ddt_row(self):
        current_row = self.tableWidget_m.rowCount() - 1  # Get the current row index

        unit_m = "m"  # Set the unit
        unit_m_cell = QtWidgets.QTableWidgetItem(unit_m)
        unit_m_cell.setForeground(QtGui.QColor("red"))  # Set the text color to red

        new_row = self.tableWidget_m.rowCount()  # Insert one new row at the end of the table
        self.tableWidget_m.insertRow(new_row)

        flags = unit_m_cell.flags()  # Freeze cell
        flags &= ~QtCore.Qt.ItemFlag.ItemIsEditable  # set the cell as read-only
        flags &= ~QtCore.Qt.ItemFlag.ItemIsSelectable  # disable cell selection
        unit_m_cell.setFlags(flags)

        self.tableWidget_m.setItem(new_row, 7, unit_m_cell)  # set the unit

        # Copy the formatting and logic from the previous row to the new row
        for column in range(self.tableWidget_m.columnCount()):
            item = self.tableWidget_m.item(current_row, column)
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

                self.tableWidget_m.setItem(new_row, column, new_item)

    def delete_row(self):
        current_row = self.tableWidget_m.currentRow()
        self.tableWidget_m.removeRow(current_row)

        # If all rows are deleted, activate the lineEdit_desc item
        self.lineEdit_desc.setEnabled(True)

        # Activate comboBox item
        self.comboBox.setEnabled(True)

    def square(self):
        try:
            for row in range(self.tableWidget_m.rowCount()):
                times_item = self.tableWidget_m.item(row, 4)
                times_value = times_item.text()

                # Check if times value is empty
                if times_value.strip() == "":
                    times_item.setText("1.00 /")  # Set default value of "1.00 /"
                else:
                    times = float(times_value.rstrip(" /"))
                    times_item.setText("{:,.2f} /".format(times))

                dims_item = self.tableWidget_m.item(row, 5)
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
                self.tableWidget_m.setItem(row, 6, item)

            # Add a new row at the end
            last_row = self.tableWidget_m.rowCount()
            self.tableWidget_m.insertRow(last_row)

            # Insert sum_code
            sum_code = self.code()
            sum_code_item = QtWidgets.QTableWidgetItem(sum_code)
            self.tableWidget_m.setItem(last_row, 0, sum_code_item)

            # Set unit column as 'm' for the last row
            unit_item = QtWidgets.QTableWidgetItem("m")
            flags = unit_item.flags()
            flags &= ~QtCore.Qt.ItemFlag.ItemIsEditable
            flags &= ~QtCore.Qt.ItemFlag.ItemIsSelectable
            unit_item.setFlags(flags)
            self.tableWidget_m.setItem(last_row, 7, unit_item)

            # Set description column as 'sum' for the last row
            desc_item = QtWidgets.QTableWidgetItem("SUM")
            flags = desc_item.flags()
            flags &= ~QtCore.Qt.ItemFlag.ItemIsEditable
            flags &= ~QtCore.Qt.ItemFlag.ItemIsSelectable
            desc_item.setFlags(flags)
            self.tableWidget_m.setItem(last_row, 8, desc_item)

            # Sum the numbers in the square column
            total_square = 0.0
            for row in range(self.tableWidget_m.rowCount() - 1):
                square_item = self.tableWidget_m.item(row, 6)
                square_value = square_item.text().replace(",", "")
                total_square += float(square_value)

            # Set the total square in the last row's square column
            total_item = QtWidgets.QTableWidgetItem("{:,.2f}".format(total_square))
            flags = total_item.flags()
            flags &= ~QtCore.Qt.ItemFlag.ItemIsEditable
            flags &= ~QtCore.Qt.ItemFlag.ItemIsSelectable
            total_item.setFlags(flags)
            self.tableWidget_m.setItem(last_row, 6, total_item)


        except ValueError:
            return
        except AttributeError:
            return
        except UnboundLocalError:
            return

    def clear_table(self):
        self.tableWidget_m.clearContents()
        self.tableWidget_m.setRowCount(0)

        # If all rows are cleared, activate the lineEdit_desc item
        self.lineEdit_desc.clear()
        self.lineEdit_desc.setEnabled(True)

        # Reset to ---Select Trade---
        self.comboBox.setCurrentIndex(0)

        # Activate comboBox item
        self.comboBox.setEnabled(True)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("tabWidget_m", "tabWidget_m"))

        self.groupBox_m.setTitle(_translate("tabWidget_m", "Linear measurement"))

        self.label_4.setText(_translate("tabWidget_m", "Desc :"))
        self.label_5.setText(_translate("tabWidget_m", "Trade : "))
        self.comboBox.setItemText(0, _translate("tabWidget_m", "--- Select Trade ---"))
        self.comboBox.setItemText(1, _translate("tabWidget_m", "A - Preliminaries/General conditions"))
        self.comboBox.setItemText(2, _translate("tabWidget_m", "C - Existing site/buildings/services"))
        self.comboBox.setItemText(3, _translate("tabWidget_m", "D - Groundwork"))
        self.comboBox.setItemText(4, _translate("tabWidget_m", "E - In situ concrete/Large precast concrete"))
        self.comboBox.setItemText(5, _translate("tabWidget_m", "F - Masonry"))
        self.comboBox.setItemText(6, _translate("tabWidget_m", "G - Structural/Carcassing metal/timber"))
        self.comboBox.setItemText(7, _translate("tabWidget_m", "H - Cladding"))
        self.comboBox.setItemText(8, _translate("tabWidget_m", "J - Waterproofing"))
        self.comboBox.setItemText(9, _translate("tabWidget_m", "K - Linings/Sheathing/Dry partitioning"))
        self.comboBox.setItemText(10, _translate("tabWidget_m", "L - Windows/Doors/Stairs"))
        self.comboBox.setItemText(11, _translate("tabWidget_m", "M - Surface finishes"))
        self.comboBox.setItemText(12, _translate("tabWidget_m", "N - Furniture/Equipment"))
        self.comboBox.setItemText(13, _translate("tabWidget_m", "P - Building fabric sundries"))
        self.comboBox.setItemText(14, _translate("tabWidget_m", "Q - Paving/Planting/Fencing/Site furniture"))
        self.comboBox.setItemText(15, _translate("tabWidget_m", "R - Disposal systems"))
        self.comboBox.setItemText(16, _translate("tabWidget_m", "S - Piped Supply systems"))
        self.comboBox.setItemText(17, _translate("tabWidget_m", "T - Mechanical heating/Cooling/Refrigeration systems"))
        self.comboBox.setItemText(18, _translate("tabWidget_m", "U - Ventilation/Air conditioning systems"))
        self.comboBox.setItemText(19, _translate("tabWidget_m", "V - Electrical supply/power/lighting systems"))
        self.comboBox.setItemText(20, _translate("tabWidget_m", "W - Communications/Security/Control systems"))
        self.comboBox.setItemText(21, _translate("tabWidget_m", "X - Transport systems"))
        self.comboBox.setItemText(22, _translate("tabWidget_m", "Y - Mechanical and electrical services measurement"))

        self.label_6.setText(_translate("tabWidget_m", "Code :"))
        self.label_code.setText(_translate("tabWidget_m", "\"code shows up here\""))
        self.pushButton_m_add.setText(_translate("tabWidget_m", "Add"))
        self.pushButton_m_ddt.setText(_translate("tabWidget_m", "Deduct"))
        self.pushButton_m_del.setText(_translate("tabWidget_m", "Delete"))
        self.pushButton_m_sqr.setText(_translate("tabWidget_m", "Square"))
        item = self.tableWidget_m.horizontalHeaderItem(0)
        item.setText(_translate("tabWidget_m", "code"))
        self.tableWidget_m.setColumnWidth(0, 60)
        item = self.tableWidget_m.horizontalHeaderItem(1)
        item.setText(_translate("tabWidget_m", "trade"))
        self.tableWidget_m.setColumnWidth(1, 40)
        item = self.tableWidget_m.horizontalHeaderItem(2)
        item.setText(_translate("tabWidget_m", "desc"))
        self.tableWidget_m.setColumnWidth(2, 250)
        item = self.tableWidget_m.horizontalHeaderItem(3)
        item.setText(_translate("tabWidget_m", "ref"))
        self.tableWidget_m.setColumnWidth(3, 60)
        item = self.tableWidget_m.horizontalHeaderItem(4)
        item.setText(_translate("tabWidget_m", "times"))
        self.tableWidget_m.setColumnWidth(4, 60)
        item = self.tableWidget_m.horizontalHeaderItem(5)
        item.setText(_translate("tabWidget_m", "dims"))
        self.tableWidget_m.setColumnWidth(5, 60)
        item = self.tableWidget_m.horizontalHeaderItem(6)
        item.setText(_translate("tabWidget_m", "square"))
        self.tableWidget_m.setColumnWidth(6, 60)
        item = self.tableWidget_m.horizontalHeaderItem(7)
        item.setText(_translate("tabWidget_m", "unit"))
        self.tableWidget_m.setColumnWidth(7, 30)
        item = self.tableWidget_m.horizontalHeaderItem(8)
        item.setText(_translate("tabWidget_m", "sign post"))
        self.tableWidget_m.setColumnWidth(8, 100)

        self.pushButton_m_clear.setText(_translate("tabWidget_m", "Clear"))
        self.pushButton_m_insert.setText(_translate("tabWidget_m", "Insert"))

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
        num_rows = self.tableWidget_m.rowCount()
        num_columns = self.tableWidget_m.columnCount()

        # Iterate over each row in the table widget and insert the data into the database
        for row in range(num_rows):
            data = []
            for col in range(num_columns):
                item = self.tableWidget_m.item(row, col)
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
