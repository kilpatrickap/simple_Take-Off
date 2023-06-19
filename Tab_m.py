import os.path
import sqlite3
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QTableWidgetItem


class Tab_m_Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

    # def setupUi(self, MainWindow):
        # MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(600, 450)
        # font = QtGui.QFont()
        # font.setFamily("Helvetica")
        # font.setPointSize(12)
        # MainWindow.setFont(font)


        # self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        # self.centralwidget.setObjectName("centralwidget")
        #

        # self.tabWidget_m = QtWidgets.QTabWidget(parent=self.centralwidget)


        # self.tabWidget_m = QtWidgets.QTabWidget(self)
        # self.tabWidget_m.setGeometry(QtCore.QRect(10, 10, 571, 421))
        # self.tabWidget_m.setObjectName("tabWidget_m")
        #
        #
        # self.tab_m = QtWidgets.QWidget()
        # self.tab_m.setObjectName("tab_m")

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
        self.pushButton_m_clear = QtWidgets.QPushButton(parent=self.groupBox_m)
        self.pushButton_m_clear.setObjectName("pushButton_m_clear")

        # Connect signal
        self.pushButton_m_clear.clicked.connect(self.clear_table)

        self.horizontalLayout_11.addWidget(self.pushButton_m_clear)
        self.pushButton_m_insert = QtWidgets.QPushButton(parent=self.groupBox_m)
        self.pushButton_m_insert.setObjectName("pushButton_m_insert")

        # Connect signals
        # self.pushButton_m_insert.clicked.connect(self.save_table_data)
        # self.pushButton_m_insert.clicked.connect(self.load_table_data)
        # self.pushButton_m_insert.clicked.connect(self.save_takeOff_database)

        self.horizontalLayout_11.addWidget(self.pushButton_m_insert)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        # self.tabWidget_m.addTab(self.tab_m, "")

        #---TAB_2 REMOVED---

        # self.tab_2 = QtWidgets.QWidget()
        # self.tab_2.setObjectName("tab_2")
        # self.tabWidget_m.addTab(self.tab_2, "")


        # MainWindow.setCentralWidget(self.centralwidget)
        # MainWindow.setCentralWidget(self)
        # self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 1375, 17))
        # self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

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
        conn = sqlite3.connect('m_data.db')
        cursor = conn.cursor()

        # Execute query to retrieve table names ending with a number
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'm_M%' OR name LIKE 'm_D%'")
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

        tab_name = self.tabWidget_m.currentWidget().objectName()  # Get the name of the current tab
        last_letter = tab_name[-1]  # Get the last letter of the tab name

        # Retrieve the current highest code number for the given tab and increment it by 1
        next_code_number = self.get_highest_code_number() + 1

        # Concatenate the tab name, first letter, last letter, and the incremented code number
        code_string = f"{last_letter}_{first_letter}{next_code_number}"
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
        self.lineEdit_desc.setEnabled(True)

        # Activate comboBox item
        self.comboBox.setEnabled(True)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("tabWidget_m", "tabWidget_m"))



        self.groupBox_m.setTitle(_translate("tabWidget_m", "m"))
        self.label_4.setText(_translate("tabWidget_m", "Desc :"))
        self.label_5.setText(_translate("tabWidget_m", "Trade : "))
        self.comboBox.setItemText(0, _translate("tabWidget_m", "--- Select Trade ---"))
        self.comboBox.setItemText(1, _translate("tabWidget_m", "D - GROUNDWORK"))
        self.comboBox.setItemText(2, _translate("tabWidget_m", "M - SURFACE FINISHES"))
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
        self.tableWidget_m.setColumnWidth(2, 160)
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
        self.tableWidget_m.setColumnWidth(8, 160)

        self.pushButton_m_clear.setText(_translate("tabWidget_m", "Clear"))
        self.pushButton_m_insert.setText(_translate("tabWidget_m", "Insert"))
        # self.tabWidget_m.setTabText(self.tabWidget_m.indexOf(self.tab_m), _translate("tabWidget_m", "m"))
        # self.tabWidget_m.setTabText(self.tabWidget_m.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))

    def save_table_data(self):
        # Import the return of self.code here as code_string
        code_string = self.code()

        # Check if code_string is valid
        if not code_string:
            print("Invalid table name")
            return

        # Connect to the SQLite database
        conn = sqlite3.connect('m_data.db')
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

    def load_table_data(self):
        # Connect to the SQLite database
        conn = sqlite3.connect('m_data.db')
        cursor = conn.cursor()

        # Get the list of table names from the database
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()

        # Extract table names from the fetched data and store them in a list
        table_list = [table[0] for table in tables[1:]]  # Exclude the first table 'sqlite_sequence'

        print(table_list)

        # Initialize an empty list to store all the retrieved data
        all_data = []

        # Iterate over each table in table_list
        for table_name in table_list:
            # Retrieve the data from the table
            cursor.execute(f'SELECT * FROM {table_name}')
            data = cursor.fetchall()

            # Append the retrieved data to the all_data list
            all_data.extend(data)

        print(all_data)

        # Check if the all_data list is empty
        if not all_data:
            return

        # Set the number of rows and columns in the QTableWidget
        self.tableWidget_takeOff.setRowCount(len(all_data))
        self.tableWidget_takeOff.setColumnCount(len(all_data[9]) - 1)  # Exclude ID

        # Populate the QTableWidget with the retrieved data
        for row_num, row_data in enumerate(all_data):
            square_value = 0.0  # Initialize square_value
            sign_post_value = None  # Initialize sign_post_value

            for col_num, col_data in enumerate(row_data):
                if col_num == 0:  # Exclude ID column
                    continue

                item = QtWidgets.QTableWidgetItem()

                if col_num == 7:  # "square" column is at index 7
                    try:
                        square_value = float(col_data)
                        formatted_value = '{:,.2f}'.format(square_value)
                    except ValueError:
                        formatted_value = str(col_data)
                else:
                    formatted_value = str(col_data)

                item.setText(formatted_value)
                self.tableWidget_takeOff.setItem(row_num, col_num - 1, item)  # Adjust column index

                if col_num == 9:  # "sign_post" column is at index 9
                    sign_post_value = str(col_data)  # Store the value of the sign_post column

            # Check if square value is negative and set row color to red
            if square_value < 0:
                for col in range(self.tableWidget_takeOff.columnCount()):
                    cell_item = self.tableWidget_takeOff.item(row_num, col)
                    cell_item.setForeground(QtGui.QColor('red'))

            # Check if sign_post_value == "SUM", set row foreground to blue
            if sign_post_value == "SUM":
                for col in range(self.tableWidget_takeOff.columnCount()):
                    cell_item = self.tableWidget_takeOff.item(row_num, col)
                    cell_item.setForeground(QtGui.QColor('blue'))

        # Close the database connection
        conn.close()

#     def save_takeOff_database(self):
#         conn = sqlite3.connect('takeOff.db')  # Create or connect to the "takeOff.db" database
#         cursor = conn.cursor()
#
#         # Create the "takeOff" table if it doesn't exist
#         cursor.execute("""
#             CREATE TABLE IF NOT EXISTS takeOff (
#                 id     INTEGER PRIMARY KEY AUTOINCREMENT,
#                 code   TEXT,
#                 trade  TEXT,
#                 desc   TEXT,
#                 ref    TEXT,
#                 times  TEXT,
#                 dims   TEXT,
#                 square INTEGER,
#                 unit   TEXT,
#                 sign_post TEXT,
#                 UNIQUE(id)
#             )
#         """)
#
#         rows = self.tableWidget_takeOff.rowCount()
#         for row in range(rows):
#             code = self.tableWidget_takeOff.item(row, 0).text()
#             trade = self.tableWidget_takeOff.item(row, 1).text()
#             desc = self.tableWidget_takeOff.item(row, 2).text()
#             ref = self.tableWidget_takeOff.item(row, 3).text()
#             times = self.tableWidget_takeOff.item(row, 4).text()
#             dims = self.tableWidget_takeOff.item(row, 5).text()
#             square = self.tableWidget_takeOff.item(row, 6).text()
#             unit = self.tableWidget_takeOff.item(row, 7).text()
#             sign_post = self.tableWidget_takeOff.item(row, 8).text()
#
#             # Check if the row already exists in the table
#             cursor.execute("""
#                 SELECT * FROM takeOff WHERE code = ? AND trade = ? AND desc = ? AND ref = ? AND times = ? AND dims = ?
#                 AND square = ? AND unit = ? AND sign_post = ?
#             """, (code, trade, desc, ref, times, dims, square, unit, sign_post))
#
#             existing_row = cursor.fetchone()
#             if existing_row is None:
#                 # Row does not exist, insert it into the table
#                 cursor.execute("""
#                     INSERT INTO takeOff (code, trade, desc, ref, times, dims, square, unit, sign_post)
#                     VALUES (?,?,?,?,?,?,?,?,?)
#                 """, (code, trade, desc, ref, times, dims, square, unit, sign_post))
#
#         conn.commit()  # Save the changes
#         conn.close()  # Close the connection
#
#         print("Data is saved to takeOff.db")
#
#     # def search_code(self):
#     #     entered_code = self.lineEdit_code.text()
#     #     print(entered_code)
#     #
#     #     conn = sqlite3.connect('takeOff.db')  # Connect to the "takeOff.db" database
#     #     cursor = conn.cursor()
#     #
#     #     # Execute a query to search for the entered code in all the columns of the 'takeOff' table
#     #     cursor.execute("SELECT * FROM takeOff WHERE code=?", (entered_code,))
#     #     rows = cursor.fetchall()
#     #
#     #     # Slice the id column returned from the takeOff.db using list comprehension. [1:] starts from 2nd element
#     #     rows = [row[1:] for row in rows]
#     #
#     #     # Clear the existing data in the tableWidget_takeOff
#     #     self.tableWidget_takeOff.clearContents()
#     #     self.tableWidget_takeOff.setRowCount(0)
#     #
#     #     if rows:
#     #         print("Matching rows:")
#     #         for row in rows:
#     #             print(row)
#     #             # Add a new row to the tableWidget_takeOff
#     #             self.tableWidget_takeOff.insertRow(self.tableWidget_takeOff.rowCount())
#     #
#     #             # # Populate the cells of the new row with the fetched data
#     #             for column, value in enumerate(row):
#     #                 item = QTableWidgetItem(str(value))
#     #                 self.tableWidget_takeOff.setItem(self.tableWidget_takeOff.rowCount() - 1, column, item)
#     #     else:
#     #         print("No matching rows")
#     #
#     #     conn.close()
#
# #     def edit_code(self):  # TODO edit_code() should be in a separate tableWidget window
# #         entered_code = self.lineEdit_code.text()
# #         print("Entered code:", entered_code)
# #
# #         # Connect to the 'takeOff.db' database
# #         conn = sqlite3.connect('takeOff.db')  # TODO only edit tables in (m_data, m2_data, m3_data, item_data etc)
# #         cursor = conn.cursor()
# #
# #         # Execute a query to search for the entered code in the 'takeOff' table
# #         cursor.execute("SELECT * FROM takeOff WHERE code=?", (entered_code,))
# #         rows = cursor.fetchall()
# #
# #         # Slice the id column returned from the takeOff.db using list comprehension. [1:] starts from 2nd element
# #         rows = [row[1:] for row in rows]
# #
# #         if rows:
# #             print(f"Code '{entered_code}' found:")
# #
# #             # Set the label_code text to the entered code
# #             self.label_code.setText(entered_code)
# #
# #             for row in rows:
# #                 print(row)
# #                 # Add a new row to the tableWidget_m
# #                 self.tableWidget_m.insertRow(self.tableWidget_m.rowCount())
# #
# #                 # Populate the cells of the new row with the fetched data
# #                 for column, value in enumerate(row):
# #                     item = QTableWidgetItem(str(value))
# #                     self.tableWidget_m.setItem(self.tableWidget_m.rowCount() - 1, column, item)
# #         else:
# #             print(f"Code '{entered_code}' not found")
# #
# #             # Clear the label_code text
# #             self.label_code.setText(f"'{entered_code}' not found!")
# #
# #         conn.close()
# #
# #
# # # if __name__ == "__main__":
# # #     import sys
# # #
# # #     app = QtWidgets.QApplication(sys.argv)
# # #     MainWindow = QtWidgets.QMainWindow()
# # #     ui = Tab_m_Widget()
# # #     # ui.setupUi(MainWindow)
# # #     MainWindow.show()
# # #     sys.exit(app.exec())
