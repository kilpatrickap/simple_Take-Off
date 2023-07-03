import os.path
import sqlite3
from PyQt6 import QtCore, QtGui, QtWidgets


class Edit_m2_Dialog(object):
    def __init__(self, entered_code):  # entered_code is initialized as an argument

        self.entered_code = entered_code  # Initialize the class attributes
        print("Entered code from TakeOff Sheet is : " + entered_code)  # test to see if it works.

    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
        Dialog.resize(770, 520)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        Dialog.setFont(font)

        self.groupBox_m2 = QtWidgets.QGroupBox(parent=Dialog)
        self.groupBox_m2.setGeometry(QtCore.QRect(10, 10, 751, 501))
        self.groupBox_m2.setObjectName("groupBox_m2")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_m2)
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

        self.pushButton_m2_add = QtWidgets.QPushButton(parent=Dialog)

        # Add button icon with relative path
        icon1 = QtGui.QIcon()
        image_path_to_icon1 = os.path.join(os.path.dirname(__file__), "images", "plus.png")
        icon1.addPixmap(QtGui.QPixmap(image_path_to_icon1), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_m2_add.setIcon(icon1)

        self.pushButton_m2_add.setObjectName("pushButton_m2_add")

        # Connect signal
        self.pushButton_m2_add.clicked.connect(self.add_row)

        self.horizontalLayout_10.addWidget(self.pushButton_m2_add)
        self.pushButton_m2_ddt = QtWidgets.QPushButton(parent=Dialog)

        # Deduct button icon with relative path
        icon2 = QtGui.QIcon()
        image_path_to_icon2 = os.path.join(os.path.dirname(__file__), "images", "minus.png")
        icon2.addPixmap(QtGui.QPixmap(image_path_to_icon2), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_m2_ddt.setIcon(icon2)

        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.pushButton_m2_ddt.setFont(font)
        self.pushButton_m2_ddt.setObjectName("pushButton_m2_ddt")

        # Connect signal
        self.pushButton_m2_ddt.clicked.connect(self.ddt_row)
        self.pushButton_m2_ddt.setStyleSheet("color: red")

        self.horizontalLayout_10.addWidget(self.pushButton_m2_ddt)
        self.pushButton_m2_del = QtWidgets.QPushButton(parent=Dialog)

        # Delete button icon with relative path
        icon3 = QtGui.QIcon()
        image_path_to_icon3 = os.path.join(os.path.dirname(__file__), "images", "cross.png")
        icon3.addPixmap(QtGui.QPixmap(image_path_to_icon3), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_m2_del.setIcon(icon3)

        self.pushButton_m2_del.setObjectName("pushButton_m2_del")

        # Connect signal
        self.pushButton_m2_del.clicked.connect(self.delete_row)

        self.horizontalLayout_10.addWidget(self.pushButton_m2_del)

        self.pushButton_m2_sqr = QtWidgets.QPushButton(parent=Dialog)

        # Square button icon with relative path
        icon4 = QtGui.QIcon()
        image_path_to_icon4 = os.path.join(os.path.dirname(__file__), "images", "calculator.png")
        icon4.addPixmap(QtGui.QPixmap(image_path_to_icon4), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_m2_sqr.setIcon(icon4)

        self.pushButton_m2_sqr.setObjectName("pushButton_m2_sqr")

        # Connect signal
        self.pushButton_m2_sqr.clicked.connect(self.square)

        self.horizontalLayout_10.addWidget(self.pushButton_m2_sqr)

        self.pushButton_m2_destroy = QtWidgets.QPushButton(parent=Dialog)

        # Add button icon with relative path
        icon7 = QtGui.QIcon()
        image_path_to_icon7 = os.path.join(os.path.dirname(__file__), "images", "exit.png")
        icon7.addPixmap(QtGui.QPixmap(image_path_to_icon7), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_m2_destroy.setIcon(icon7)

        self.pushButton_m2_destroy.setObjectName("pushButton_m2_destroy")

        # Connect signal
        self.pushButton_m2_destroy.clicked.connect(self.destroy_code)

        self.horizontalLayout_10.addWidget(self.pushButton_m2_destroy)

        # Horizontal spacer
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)

        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.tableWidget_m2 = QtWidgets.QTableWidget(parent=Dialog)
        self.tableWidget_m2.setObjectName("tableWidget_m2")
        self.tableWidget_m2.setColumnCount(9)
        self.tableWidget_m2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_m2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_m2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_m2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_m2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_m2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_m2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_m2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_m2.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_m2.setHorizontalHeaderItem(8, item)
        self.verticalLayout.addWidget(self.tableWidget_m2)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")

        # Horizontal spacer
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem3)

        self.pushButton_m2_clear = QtWidgets.QPushButton(parent=Dialog)

        # Clear button icon with relative path
        icon5 = QtGui.QIcon()
        image_path_to_icon5 = os.path.join(os.path.dirname(__file__), "images", "application-blue.png")
        icon5.addPixmap(QtGui.QPixmap(image_path_to_icon5), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_m2_clear.setIcon(icon5)

        self.pushButton_m2_clear.setObjectName("pushButton_m2_clear")

        # Connect signal
        self.pushButton_m2_clear.clicked.connect(self.clear_table)

        self.horizontalLayout_11.addWidget(self.pushButton_m2_clear)
        self.pushButton_m2_update = QtWidgets.QPushButton(parent=Dialog)

        # Insert button icon with relative path
        icon6 = QtGui.QIcon()
        image_path_to_icon6 = os.path.join(os.path.dirname(__file__), "images", "disk.png")
        icon6.addPixmap(QtGui.QPixmap(image_path_to_icon6), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_m2_update.setIcon(icon6)

        self.pushButton_m2_update.setObjectName("pushButton_m2_update")

        # Connect signals
        self.pushButton_m2_update.clicked.connect(self.update_msmt)

        self.horizontalLayout_11.addWidget(self.pushButton_m2_update)

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
        """
        Adds new rows to the table and copies data from existing rows.

        This method adds two new rows at the end of the table and copies data from the second-to-last row to the new
        rows. It also copies the content of the last row for the first 9 columns to the new rows. Additionally,
        it sets a special unit (m2) value in one of the cells of the second newly inserted row.

        :parameter: None

        :return: None
        """
        unit_m2 = "m2"  # Set the unit

        last_row = self.tableWidget_m2.rowCount() - 1

        if last_row >= 1:
            for i in range(2):  # Set number of rows to be added (m2 = 2; m3 = 3)
                source_row = last_row - 1 + i
                destination_row = last_row + i + 1

                for column in range(self.tableWidget_m2.columnCount()):
                    item = self.tableWidget_m2.item(source_row, column)
                    if item is not None:
                        new_item = QtWidgets.QTableWidgetItem(item.text())
                        flags = item.flags()
                        new_item.setFlags(flags)
                        self.tableWidget_m2.setItem(destination_row, column, new_item)

        self.tableWidget_m2.insertRow(last_row + 1)
        self.tableWidget_m2.insertRow(last_row + 2)

        # Copy items in the 1st to 9th columns to the new rows
        for column in range(9):
            item = self.tableWidget_m2.item(last_row - 1, column)
            if item is not None:
                new_item1 = QtWidgets.QTableWidgetItem(item.text())
                flags = item.flags()
                new_item1.setFlags(flags)
                self.tableWidget_m2.setItem(last_row + 1, column, new_item1)

                item2 = self.tableWidget_m2.item(last_row, column)
                if item2 is not None:
                    new_item2 = QtWidgets.QTableWidgetItem(item2.text())
                    new_item2.setFlags(flags)
                    self.tableWidget_m2.setItem(last_row + 2, column, new_item2)

        # Set the unit in the new rows
        unit_m2_item = QtWidgets.QTableWidgetItem(unit_m2)
        flags = unit_m2_item.flags()
        flags &= ~QtCore.Qt.ItemFlag.ItemIsEditable  # Set the cell as read-only
        flags &= ~QtCore.Qt.ItemFlag.ItemIsSelectable  # Disable cell selection
        unit_m2_item.setFlags(flags)

        self.tableWidget_m2.setItem(last_row + 2, 7, unit_m2_item)  # Set the unit item on the second newly inserted row

    def ddt_row(self):
        """
        Adds new rows to the table widget and sets the text color of the new rows to red.

        This method is responsible for duplicating the last row of the table widget and appending the duplicated rows at
        the end. It also updates certain values and sets the text color of the new rows to red.

        :parameter: None

        :return: None
        """

        unit_m2 = "m2"  # Set the unit

        last_row = self.tableWidget_m2.rowCount() - 1

        if last_row >= 1:
            for i in range(2):  # Set number of rows to be added (m2 = 2; m3 = 3)
                source_row = last_row - 1 + i
                destination_row = last_row + i + 1

                for column in range(self.tableWidget_m2.columnCount()):
                    item = self.tableWidget_m2.item(source_row, column)
                    if item is not None:
                        new_item = QtWidgets.QTableWidgetItem(item.text())
                        flags = item.flags()
                        new_item.setFlags(flags)
                        self.tableWidget_m2.setItem(destination_row, column, new_item)

        # Insert the new rows at the end of the table
        self.tableWidget_m2.insertRow(last_row + 1)
        self.tableWidget_m2.insertRow(last_row + 2)

        # Copy items in the 1st to 9th columns to the new rows
        for column in range(9):
            item = self.tableWidget_m2.item(last_row - 1, column)
            if item is not None:
                new_item1 = QtWidgets.QTableWidgetItem(item.text())
                flags = item.flags()
                new_item1.setFlags(flags)
                self.tableWidget_m2.setItem(last_row + 1, column, new_item1)
                new_item1.setForeground(QtGui.QColor("red"))  # Set the text color to red

                item2 = self.tableWidget_m2.item(last_row, column)
                if item2 is not None:
                    new_item2 = QtWidgets.QTableWidgetItem(item2.text())
                    new_item2.setFlags(flags)
                    self.tableWidget_m2.setItem(last_row + 2, column, new_item2)
                    new_item2.setForeground(QtGui.QColor("red"))  # Set the text color to red

        # Set the unit in the new rows
        unit_m2_item = QtWidgets.QTableWidgetItem(unit_m2)
        flags = unit_m2_item.flags()
        flags &= ~QtCore.Qt.ItemFlag.ItemIsEditable  # Set the cell as read-only
        flags &= ~QtCore.Qt.ItemFlag.ItemIsSelectable  # Disable cell selection
        unit_m2_item.setFlags(flags)
        unit_m2_item.setForeground(QtGui.QColor("red"))  # Set the text color to red

        self.tableWidget_m2.setItem(last_row + 2, 7, unit_m2_item)  # Set the unit item on the second newly inserted row

    def delete_row(self):
        current_row = self.tableWidget_m2.currentRow()
        self.tableWidget_m2.removeRow(current_row)

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
            if start_row >= self.tableWidget_m2.rowCount():

                # Add a new row at the end of the table
                last_row = self.tableWidget_m2.rowCount()
                self.tableWidget_m2.insertRow(last_row)

                # Insert sum_code
                sum_code = self.code()
                sum_code_item = QtWidgets.QTableWidgetItem(sum_code)
                self.tableWidget_m2.setItem(last_row, 0, sum_code_item)

                # Set unit column as 'm2' for the last row
                unit_item = QtWidgets.QTableWidgetItem("m2")
                flags = unit_item.flags()
                flags &= ~QtCore.Qt.ItemFlag.ItemIsEditable
                flags &= ~QtCore.Qt.ItemFlag.ItemIsSelectable
                unit_item.setFlags(flags)
                self.tableWidget_m2.setItem(last_row, 7, unit_item)

                # Set sign_post column as 'sum' for the last row
                desc_item = QtWidgets.QTableWidgetItem("SUM")
                flags = desc_item.flags()
                flags &= ~QtCore.Qt.ItemFlag.ItemIsEditable
                flags &= ~QtCore.Qt.ItemFlag.ItemIsSelectable
                desc_item.setFlags(flags)
                self.tableWidget_m2.setItem(last_row, 8, desc_item)

                # Sum the numbers in the square column
                total_square = 0.0
                for row in range(self.tableWidget_m2.rowCount()):
                    square_item = self.tableWidget_m2.item(row, 6)
                    if square_item is not None:
                        square_value = square_item.text().replace(",", "")
                        if square_value.strip() != "":
                            total_square += float(square_value)

                # print(total_square)

                # Set the total square in the last row's square column
                total_item = QtWidgets.QTableWidgetItem("{:,.2f}".format(total_square))
                flags = total_item.flags()
                flags &= ~QtCore.Qt.ItemFlag.ItemIsEditable
                flags &= ~QtCore.Qt.ItemFlag.ItemIsSelectable
                total_item.setFlags(flags)
                self.tableWidget_m2.setItem(last_row, 6, total_item)

                return  # Base case: stop recursion when all rows have been processed

            times_item = self.tableWidget_m2.item(start_row, 4)
            times_value = times_item.text()

            # Check if times value is empty
            if times_value.strip() == "":
                times_item.setText("1.00 /")  # Set default value of "1.00 /"
            else:
                times = float(times_value.rstrip(" /"))
                times_item.setText("{:,.2f} /".format(times))

            dims_m2_len_item = self.tableWidget_m2.item(start_row, 5)
            dims_m2_len = float(dims_m2_len_item.text())
            dims_m2_len_item.setText("{:,.2f}".format(dims_m2_len))

            # Add 1 to row for width_row increment
            width_row = start_row + 1

            dims_m2_width_item = self.tableWidget_m2.item(width_row, 5)  # width_row increments by 1
            dims_m2_width = float(dims_m2_width_item.text())
            dims_m2_width_item.setText("{:,.2f}".format(dims_m2_width))

            # Calculate square
            square = round(times * dims_m2_len * dims_m2_width, 2)

            # Check if times and dims values are colored red
            if times_item.foreground().color().name() == "#ff0000" \
                    and dims_m2_len_item.foreground().color().name() == "#ff0000" \
                    and dims_m2_width_item.foreground().color().name() == "#ff0000":

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
            self.tableWidget_m2.setItem(width_row, 6, item)

            # Recursive call to process the next set of rows
            self.square(start_row + 2)

        except ValueError:
            return
        except AttributeError:
            return
        except UnboundLocalError:
            return

    def clear_table(self):
        self.tableWidget_m2.clearContents()
        self.tableWidget_m2.setRowCount(0)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", self.entered_code))  # entered_code shows here
        self.groupBox_m2.setTitle(_translate("Dialog", "Edit Area measurement"))
        self.label_6.setText(_translate("Dialog", "Code :"))
        self.label_code.setText(_translate("Dialog", self.entered_code))  # entered_code shows here
        self.pushButton_m2_add.setText(_translate("Dialog", "Add"))
        self.pushButton_m2_ddt.setText(_translate("Dialog", "Deduct"))
        self.pushButton_m2_del.setText(_translate("Dialog", "Delete"))
        self.pushButton_m2_sqr.setText(_translate("Dialog", "Square"))
        self.pushButton_m2_destroy.setText(_translate("Dialog", "Destroy"))
        item = self.tableWidget_m2.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "code"))
        self.tableWidget_m2.setColumnWidth(0, 60)
        item = self.tableWidget_m2.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "trade"))
        self.tableWidget_m2.setColumnWidth(1, 40)
        item = self.tableWidget_m2.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "desc"))
        self.tableWidget_m2.setColumnWidth(2, 250)
        item = self.tableWidget_m2.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "ref"))
        self.tableWidget_m2.setColumnWidth(3, 60)
        item = self.tableWidget_m2.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "times"))
        self.tableWidget_m2.setColumnWidth(4, 60)
        item = self.tableWidget_m2.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "dims"))
        self.tableWidget_m2.setColumnWidth(5, 60)
        item = self.tableWidget_m2.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "square"))
        self.tableWidget_m2.setColumnWidth(6, 60)
        item = self.tableWidget_m2.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "unit"))
        self.tableWidget_m2.setColumnWidth(7, 30)
        item = self.tableWidget_m2.horizontalHeaderItem(8)
        item.setText(_translate("Dialog", "sign post"))
        self.tableWidget_m2.setColumnWidth(8, 100)

        self.pushButton_m2_clear.setText(_translate("Dialog", "Clear"))
        self.pushButton_m2_update.setText(_translate("Dialog", "Update"))

    def code(self):
        code = self.entered_code
        return code

    def load_entered_code_data(self):
        # Connect to the SQLite database
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()

        # Check if the 'self.entered_code' table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (self.entered_code,))
        if cursor.fetchone() is None:
            conn.close()
            return

        # Retrieve the data from the 'self.entered_code' table
        cursor.execute(f'SELECT * FROM {self.entered_code}')
        all_data = cursor.fetchall()

        # Check if the retrieved data is empty
        if not all_data:
            conn.close()
            return

        # Set the number of rows and columns in the QTableWidget
        self.tableWidget_m2.setRowCount(len(all_data))
        self.tableWidget_m2.setColumnCount(9)  # Column count set to 9

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

                if col_num == 1:  # Freeze the code column (index 1)
                    flags = item.flags()
                    flags &= ~QtCore.Qt.ItemFlag.ItemIsEditable
                    item.setFlags(flags)

                if col_num == 2:  # Freeze the trade column (index 2)
                    flags = item.flags()
                    flags &= ~QtCore.Qt.ItemFlag.ItemIsEditable
                    item.setFlags(flags)

                self.tableWidget_m2.setItem(row_num, col_num - 1, item)  # Adjust column index

                if col_num == 9:  # "sign_post" column is at index 9
                    sign_post_value = str(col_data)  # Store the value of the sign_post column

            # Check if square value is negative and set row color to red
            if square_value < 0:
                for col in range(self.tableWidget_m2.columnCount()):
                    cell_item = self.tableWidget_m2.item(row_num, col)
                    cell_item.setForeground(QtGui.QColor('red'))

            # Check if sign_post_value == "SUM", set row foreground to blue
            if sign_post_value == "SUM":
                for col in range(self.tableWidget_m2.columnCount()):
                    cell_item = self.tableWidget_m2.item(row_num, col)
                    cell_item.setForeground(QtGui.QColor('blue'))

        # Close the database connection
        conn.close()

    def save_table_data(self):
        code_string = self.code()  # TakeOff sheet entered_code appears here

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

        # Delete all existing rows from the table
        cursor.execute(f'DELETE FROM {code_string}')

        # Get the number of rows and columns in the table widget
        num_rows = self.tableWidget_m2.rowCount()
        num_columns = self.tableWidget_m2.columnCount()

        # Iterate over each row in the table widget and insert the data into the database
        for row in range(num_rows):
            data = []
            for col in range(num_columns):
                item = self.tableWidget_m2.item(row, col)
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

    def update_msmt(self):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("Insert")
        msg_box.setText("Click OK to update the Take Off sheet and click Refresh to show.")

        # Add button icon with relative path
        icon_path = os.path.join(os.path.dirname(__file__), "images", "exclamation-circle.png")
        icon_pixmap = QtGui.QPixmap(icon_path)
        msg_box.setIconPixmap(icon_pixmap)

        msg_box.setStandardButtons(
            QtWidgets.QMessageBox.StandardButton.Ok | QtWidgets.QMessageBox.StandardButton.Cancel
        )
        result = msg_box.exec()

        if result == QtWidgets.QMessageBox.StandardButton.Ok:
            # Perform the insertion into the TakeOff sheet
            self.save_table_data()

        else:
            # User clicked Cancel, do nothing or perform any desired action
            pass

    def destroy_code(self):
        # Find the entered_code and delete it from 'data.db'
        entered_code = self.entered_code

        # Connect to the SQLite database
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()

        # Check if the table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (entered_code,))
        table_exists = cursor.fetchone()

        if table_exists:

            # Show a messageBox warning
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle("Destroy")
            msg_box.setText("Click OK to PERMANENTLY DELETE the measurement.")

            # Add button icon with relative path
            icon_path = os.path.join(os.path.dirname(__file__), "images", "exclamation-red.png")
            icon_pixmap = QtGui.QPixmap(icon_path)
            msg_box.setIconPixmap(icon_pixmap)

            msg_box.setStandardButtons(
                QtWidgets.QMessageBox.StandardButton.Ok | QtWidgets.QMessageBox.StandardButton.Cancel
            )
            result = msg_box.exec()

            if result == QtWidgets.QMessageBox.StandardButton.Ok:
                # Delete the table if it exists
                cursor.execute(f"DROP TABLE {entered_code}")
                print(f"Table '{entered_code}' deleted successfully.")
            else:
                print(f"Table '{entered_code}' does not exist.")

        # Commit the changes and close the connection
        conn.commit()
        conn.close()
