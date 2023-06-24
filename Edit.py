import os.path
import sqlite3
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QTableWidgetItem, QTableWidget
# from TakeOffSheet import TakeOffSheet_Widget


class Edit_Dialog(object):
    def __init__(self, entered_code):   # entered_code is initialized as an argument

        self.entered_code = entered_code    # Initialize the class attributes
        print("Entered code from TakeOff Sheet is : " + entered_code)   # test to see if it works.

    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
        Dialog.resize(770, 520)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        Dialog.setFont(font)

        self.groupBox_m = QtWidgets.QGroupBox(parent=Dialog)
        self.groupBox_m.setGeometry(QtCore.QRect(10, 10, 751, 501))
        self.groupBox_m.setObjectName("groupBox_m")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_m)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(parent=Dialog)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)

        self.label_code = QtWidgets.QLabel(parent=Dialog)
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

        self.pushButton_m_add = QtWidgets.QPushButton(parent=Dialog)

        # Add button icon with relative path
        icon1 = QtGui.QIcon()
        image_path_to_icon1 = os.path.join(os.path.dirname(__file__), "images", "plus.png")
        icon1.addPixmap(QtGui.QPixmap(image_path_to_icon1), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_m_add.setIcon(icon1)

        self.pushButton_m_add.setObjectName("pushButton_m_add")

        # Connect signal
        self.pushButton_m_add.clicked.connect(self.add_row)

        self.horizontalLayout_10.addWidget(self.pushButton_m_add)
        self.pushButton_m_ddt = QtWidgets.QPushButton(parent=Dialog)

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
        self.pushButton_m_del = QtWidgets.QPushButton(parent=Dialog)

        # Delete button icon with relative path
        icon3 = QtGui.QIcon()
        image_path_to_icon3 = os.path.join(os.path.dirname(__file__), "images", "cross.png")
        icon3.addPixmap(QtGui.QPixmap(image_path_to_icon3), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_m_del.setIcon(icon3)

        self.pushButton_m_del.setObjectName("pushButton_m_del")

        # Connect signal
        self.pushButton_m_del.clicked.connect(self.delete_row)

        self.horizontalLayout_10.addWidget(self.pushButton_m_del)

        self.pushButton_m_sqr = QtWidgets.QPushButton(parent=Dialog)

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
        self.tableWidget_m = QtWidgets.QTableWidget(parent=Dialog)
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

        self.pushButton_m_clear = QtWidgets.QPushButton(parent=Dialog)

        # Clear button icon with relative path
        icon5 = QtGui.QIcon()
        image_path_to_icon5 = os.path.join(os.path.dirname(__file__), "images", "application-blue.png")
        icon5.addPixmap(QtGui.QPixmap(image_path_to_icon5), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_m_clear.setIcon(icon5)

        self.pushButton_m_clear.setObjectName("pushButton_m_clear")

        # Connect signal
        self.pushButton_m_clear.clicked.connect(self.clear_table)

        self.horizontalLayout_11.addWidget(self.pushButton_m_clear)
        self.pushButton_m_insert = QtWidgets.QPushButton(parent=Dialog)

        # Insert button icon with relative path
        icon6 = QtGui.QIcon()
        image_path_to_icon6 = os.path.join(os.path.dirname(__file__), "images", "table-export.png")
        icon6.addPixmap(QtGui.QPixmap(image_path_to_icon6), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_m_insert.setIcon(icon6)

        self.pushButton_m_insert.setObjectName("pushButton_m_insert")

        # Connect signals
        # self.pushButton_m_insert.clicked.connect(self.insert_dialog)

        self.horizontalLayout_11.addWidget(self.pushButton_m_insert)

        # Horizontal spacer
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem4)

        self.verticalLayout.addLayout(self.horizontalLayout_11)

        # Load the entered_code database
        self.load_entered_code_data()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

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

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", self.entered_code))  # entered_code shows here
        self.groupBox_m.setTitle(_translate("Dialog", "Edit Linear measurement"))
        self.label_6.setText(_translate("Dialog", "Code :"))
        self.label_code.setText(_translate("Dialog", self.entered_code))    # entered_code shows here
        self.pushButton_m_add.setText(_translate("Dialog", "Add"))
        self.pushButton_m_ddt.setText(_translate("Dialog", "Deduct"))
        self.pushButton_m_del.setText(_translate("Dialog", "Delete"))
        self.pushButton_m_sqr.setText(_translate("Dialog", "Square"))
        item = self.tableWidget_m.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "code"))
        self.tableWidget_m.setColumnWidth(0, 60)
        item = self.tableWidget_m.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "trade"))
        self.tableWidget_m.setColumnWidth(1, 40)
        item = self.tableWidget_m.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "desc"))
        self.tableWidget_m.setColumnWidth(2, 250)
        item = self.tableWidget_m.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "ref"))
        self.tableWidget_m.setColumnWidth(3, 60)
        item = self.tableWidget_m.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "times"))
        self.tableWidget_m.setColumnWidth(4, 60)
        item = self.tableWidget_m.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "dims"))
        self.tableWidget_m.setColumnWidth(5, 60)
        item = self.tableWidget_m.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "square"))
        self.tableWidget_m.setColumnWidth(6, 60)
        item = self.tableWidget_m.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "unit"))
        self.tableWidget_m.setColumnWidth(7, 30)
        item = self.tableWidget_m.horizontalHeaderItem(8)
        item.setText(_translate("Dialog", "sign post"))
        self.tableWidget_m.setColumnWidth(8, 100)

        self.pushButton_m_clear.setText(_translate("Dialog", "Clear"))
        self.pushButton_m_insert.setText(_translate("Dialog", "Insert"))

    def code(self):
        code = self.entered_code
        return code

    def load_entered_code_data(self):
        # Connect to the SQLite database
        conn = sqlite3.connect('m_data.db')
        cursor = conn.cursor()

        # Get the list of table names from the database
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()

        # Extract table names from the fetched data and store them in a list
        table_list = [table[0] for table in tables[1:]]  # Exclude the first table 'sqlite_sequence'

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
        self.tableWidget_m.setRowCount(len(all_data))
        self.tableWidget_m.setColumnCount(9)  # Column count set to 9

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
                self.tableWidget_m.setItem(row_num, col_num - 1, item)  # Adjust column index

                if col_num == 9:  # "sign_post" column is at index 9
                    sign_post_value = str(col_data)  # Store the value of the sign_post column

            # Check if square value is negative and set row color to red
            if square_value < 0:
                for col in range(self.tableWidget_m.columnCount()):
                    cell_item = self.tableWidget_m.item(row_num, col)
                    cell_item.setForeground(QtGui.QColor('red'))

            # Check if sign_post_value == "SUM", set row foreground to blue
            if sign_post_value == "SUM":
                for col in range(self.tableWidget_m.columnCount()):
                    cell_item = self.tableWidget_m.item(row_num, col)
                    cell_item.setForeground(QtGui.QColor('blue'))

        # Close the database connection
        conn.close()

    def save_table_data(self):
        code_string = self.code()   # TakeOff sheet entered_code appears here

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

    # def insert_dialog(self):
    #     msg_box = QtWidgets.QMessageBox()
    #     msg_box.setWindowTitle("Insert")
    #     msg_box.setText("Click OK to insert into the TakeOff sheet and click Refresh to show.")
    #
    #     # Add button icon with relative path
    #     icon_path = os.path.join(os.path.dirname(__file__), "images", "exclamation.png")
    #     icon_pixmap = QtGui.QPixmap(icon_path)
    #     msg_box.setIconPixmap(icon_pixmap)
    #
    #     msg_box.setStandardButtons(
    #         QtWidgets.QMessageBox.StandardButton.Ok | QtWidgets.QMessageBox.StandardButton.Cancel
    #     )
    #     result = msg_box.exec()
    #
    #     if result == QtWidgets.QMessageBox.StandardButton.Ok:
    #         # Perform the insertion into the TakeOff sheet
    #         self.save_table_data()
    #         self.load_table_data()
    #         self.save_takeOff_database()
    #
    #     else:
    #         # User clicked Cancel, do nothing or perform any desired action
    #         pass
    #
    # # def load_table_data(self):
    # #     take_off_sheet = TakeOffSheet_Widget()  # Create an instance of TakeOffSheet_Widget
    # #     take_off_sheet.load_table_data()  # Call the method to load data from table
    #
    # # def save_takeOff_database(self):
    # #     take_off_sheet = TakeOffSheet_Widget()  # Create an instance of TakeOffSheet_Widget
    # #     take_off_sheet.save_takeOff_database()  # Call the method to save data from table
