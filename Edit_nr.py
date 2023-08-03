import os.path
import sqlite3
from PyQt6 import QtCore, QtGui, QtWidgets


class Edit_nr_Dialog(object):
    def __init__(self, entered_code):  # entered_code is initialized as an argument

        self.entered_code = entered_code  # Initialize the class attributes
        # print("Entered code from TakeOff Sheet is : " + entered_code)  # test to see if it works.

    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
        Dialog.resize(770, 520)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        Dialog.setFont(font)

        self.groupBox_nr = QtWidgets.QGroupBox(parent=Dialog)
        self.groupBox_nr.setGeometry(QtCore.QRect(10, 10, 751, 501))
        self.groupBox_nr.setObjectName("groupBox_nr")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_nr)
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

        self.pushButton_nr_add = QtWidgets.QPushButton(parent=Dialog)

        # Add button icon with relative path
        icon1 = QtGui.QIcon()
        image_path_to_icon1 = os.path.join(os.path.dirname(__file__), "images", "plus.png")
        icon1.addPixmap(QtGui.QPixmap(image_path_to_icon1), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_nr_add.setIcon(icon1)

        self.pushButton_nr_add.setObjectName("pushButton_nr_add")

        # Connect signal
        self.pushButton_nr_add.clicked.connect(self.add_row)

        self.horizontalLayout_10.addWidget(self.pushButton_nr_add)
        self.pushButton_nr_ddt = QtWidgets.QPushButton(parent=Dialog)

        # Deduct button icon with relative path
        icon2 = QtGui.QIcon()
        image_path_to_icon2 = os.path.join(os.path.dirname(__file__), "images", "minus.png")
        icon2.addPixmap(QtGui.QPixmap(image_path_to_icon2), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_nr_ddt.setIcon(icon2)

        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.pushButton_nr_ddt.setFont(font)
        self.pushButton_nr_ddt.setObjectName("pushButton_nr_ddt")

        # Connect signal
        self.pushButton_nr_ddt.clicked.connect(self.ddt_row)
        self.pushButton_nr_ddt.setStyleSheet("color: red")

        self.horizontalLayout_10.addWidget(self.pushButton_nr_ddt)
        self.pushButton_nr_del = QtWidgets.QPushButton(parent=Dialog)

        # Delete button icon with relative path
        icon3 = QtGui.QIcon()
        image_path_to_icon3 = os.path.join(os.path.dirname(__file__), "images", "cross.png")
        icon3.addPixmap(QtGui.QPixmap(image_path_to_icon3), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_nr_del.setIcon(icon3)

        self.pushButton_nr_del.setObjectName("pushButton_nr_del")

        # Connect signal
        self.pushButton_nr_del.clicked.connect(self.delete_row)

        self.horizontalLayout_10.addWidget(self.pushButton_nr_del)

        self.pushButton_nr_sqr = QtWidgets.QPushButton(parent=Dialog)

        # Square button icon with relative path
        icon4 = QtGui.QIcon()
        image_path_to_icon4 = os.path.join(os.path.dirname(__file__), "images", "calculator.png")
        icon4.addPixmap(QtGui.QPixmap(image_path_to_icon4), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_nr_sqr.setIcon(icon4)

        self.pushButton_nr_sqr.setObjectName("pushButton_nr_sqr")

        # Connect signal
        self.pushButton_nr_sqr.clicked.connect(self.square)

        self.horizontalLayout_10.addWidget(self.pushButton_nr_sqr)

        self.pushButton_nr_destroy = QtWidgets.QPushButton(parent=Dialog)

        # Add button icon with relative path
        icon7 = QtGui.QIcon()
        image_path_to_icon7 = os.path.join(os.path.dirname(__file__), "images", "exit.png")
        icon7.addPixmap(QtGui.QPixmap(image_path_to_icon7), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_nr_destroy.setIcon(icon7)

        self.pushButton_nr_destroy.setObjectName("pushButton_nr_destroy")

        # Connect signal
        self.pushButton_nr_destroy.clicked.connect(self.destroy_code)

        self.horizontalLayout_10.addWidget(self.pushButton_nr_destroy)

        # Horizontal spacer
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)

        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.tableWidget_nr = QtWidgets.QTableWidget(parent=Dialog)
        self.tableWidget_nr.setObjectName("tableWidget_nr")

        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.tableWidget_nr.setFont(font)

        self.tableWidget_nr.setColumnCount(9)
        self.tableWidget_nr.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_nr.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_nr.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_nr.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_nr.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_nr.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_nr.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_nr.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_nr.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_nr.setHorizontalHeaderItem(8, item)
        self.verticalLayout.addWidget(self.tableWidget_nr)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")

        # Horizontal spacer
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem3)

        self.pushButton_nr_clear = QtWidgets.QPushButton(parent=Dialog)

        # Clear button icon with relative path
        icon5 = QtGui.QIcon()
        image_path_to_icon5 = os.path.join(os.path.dirname(__file__), "images", "application-blue.png")
        icon5.addPixmap(QtGui.QPixmap(image_path_to_icon5), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_nr_clear.setIcon(icon5)

        self.pushButton_nr_clear.setObjectName("pushButton_nr_clear")

        # Connect signal
        self.pushButton_nr_clear.clicked.connect(self.clear_table)

        self.horizontalLayout_11.addWidget(self.pushButton_nr_clear)
        self.pushButton_nr_update = QtWidgets.QPushButton(parent=Dialog)

        # Insert button icon with relative path
        icon6 = QtGui.QIcon()
        image_path_to_icon6 = os.path.join(os.path.dirname(__file__), "images", "disk.png")
        icon6.addPixmap(QtGui.QPixmap(image_path_to_icon6), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_nr_update.setIcon(icon6)

        self.pushButton_nr_update.setObjectName("pushButton_nr_update")

        # Connect signals
        self.pushButton_nr_update.clicked.connect(self.update_msmt)

        self.horizontalLayout_11.addWidget(self.pushButton_nr_update)

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
        current_row = self.tableWidget_nr.currentRow()  # Get the current row index

        unit_nr = "nr"  # Set the unit
        unit_nr_cell = QtWidgets.QTableWidgetItem(unit_nr)

        new_row = self.tableWidget_nr.rowCount()  # Insert one new row at the end of the table
        self.tableWidget_nr.insertRow(new_row)

        flags = unit_nr_cell.flags()  # Freeze cell
        flags &= ~QtCore.Qt.ItemFlag.ItemIsEditable  # set the cell as read-only
        flags &= ~QtCore.Qt.ItemFlag.ItemIsSelectable  # disable cell selection
        unit_nr_cell.setFlags(flags)

        self.tableWidget_nr.setItem(0, 7, unit_nr_cell)  # set the unit

        # Copy the formatting and logic from the previous row to the new row
        for column in range(self.tableWidget_nr.columnCount()):
            item = self.tableWidget_nr.item(current_row, column)
            if item is not None:
                new_item = QtWidgets.QTableWidgetItem(item.text())
                flags = item.flags()
                new_item.setFlags(flags)
                self.tableWidget_nr.setItem(new_row, column, new_item)

    def ddt_row(self):
        current_row = self.tableWidget_nr.rowCount() - 1  # Get the current row index

        unit_nr = "nr"  # Set the unit
        unit_nr_cell = QtWidgets.QTableWidgetItem(unit_nr)
        unit_nr_cell.setForeground(QtGui.QColor("red"))  # Set the text color to red

        new_row = self.tableWidget_nr.rowCount()  # Insert one new row at the end of the table
        self.tableWidget_nr.insertRow(new_row)

        flags = unit_nr_cell.flags()  # Freeze cell
        flags &= ~QtCore.Qt.ItemFlag.ItemIsEditable  # set the cell as read-only
        flags &= ~QtCore.Qt.ItemFlag.ItemIsSelectable  # disable cell selection
        unit_nr_cell.setFlags(flags)

        self.tableWidget_nr.setItem(new_row, 7, unit_nr_cell)  # set the unit

        # Copy the formatting and logic from the previous row to the new row
        for column in range(self.tableWidget_nr.columnCount()):
            item = self.tableWidget_nr.item(current_row, column)
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

                self.tableWidget_nr.setItem(new_row, column, new_item)

    def delete_row(self):
        current_row = self.tableWidget_nr.currentRow()
        self.tableWidget_nr.removeRow(current_row)

    def square(self):
        try:
            for row in range(self.tableWidget_nr.rowCount()):
                times_item = self.tableWidget_nr.item(row, 4)
                times_value = times_item.text()

                # Check if times value is empty
                if times_value.strip() == "":
                    times_item.setText("1.00 /")  # Set default value of "1.00 /"
                else:
                    times = float(times_value.rstrip(" /"))
                    times_item.setText("{:,.2f} /".format(times))

                dims_item = self.tableWidget_nr.item(row, 5)
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
                self.tableWidget_nr.setItem(row, 6, item)

            # Add a new row at the end
            last_row = self.tableWidget_nr.rowCount()
            self.tableWidget_nr.insertRow(last_row)

            # Insert sum_code
            sum_code = self.code()
            sum_code_item = QtWidgets.QTableWidgetItem(sum_code)
            self.tableWidget_nr.setItem(last_row, 0, sum_code_item)

            # Insert Trade letter
            trade_letter = self.code()[3]  # indexing to the 4th letter of the code.
            trade_letter_item = QtWidgets.QTableWidgetItem(trade_letter)
            self.tableWidget_nr.setItem(last_row, 1, trade_letter_item)

            # Set unit column as 'm' for the last row
            unit_item = QtWidgets.QTableWidgetItem("nr")
            flags = unit_item.flags()
            flags &= ~QtCore.Qt.ItemFlag.ItemIsEditable
            flags &= ~QtCore.Qt.ItemFlag.ItemIsSelectable
            unit_item.setFlags(flags)
            self.tableWidget_nr.setItem(last_row, 7, unit_item)

            # Set description column as 'sum' for the last row
            desc_item = QtWidgets.QTableWidgetItem("SUM")
            flags = desc_item.flags()
            flags &= ~QtCore.Qt.ItemFlag.ItemIsEditable
            flags &= ~QtCore.Qt.ItemFlag.ItemIsSelectable
            desc_item.setFlags(flags)
            self.tableWidget_nr.setItem(last_row, 8, desc_item)

            # Sum the numbers in the square column
            total_square = 0.0
            for row in range(self.tableWidget_nr.rowCount() - 1):
                square_item = self.tableWidget_nr.item(row, 6)
                square_value = square_item.text().replace(",", "")
                total_square += float(square_value)

            # Set the total square in the last row's square column
            total_item = QtWidgets.QTableWidgetItem("{:,.2f}".format(total_square))
            flags = total_item.flags()
            flags &= ~QtCore.Qt.ItemFlag.ItemIsEditable
            flags &= ~QtCore.Qt.ItemFlag.ItemIsSelectable
            total_item.setFlags(flags)
            self.tableWidget_nr.setItem(last_row, 6, total_item)


        except ValueError:
            return
        except AttributeError:
            return
        except UnboundLocalError:
            return

    def clear_table(self):
        self.tableWidget_nr.clearContents()
        self.tableWidget_nr.setRowCount(0)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", self.entered_code))  # entered_code shows here
        self.groupBox_nr.setTitle(_translate("Dialog", "Edit number measurement"))
        self.label_6.setText(_translate("Dialog", "Code :"))
        self.label_code.setText(_translate("Dialog", self.entered_code))  # entered_code shows here
        self.pushButton_nr_add.setText(_translate("Dialog", "Add"))
        self.pushButton_nr_ddt.setText(_translate("Dialog", "Deduct"))
        self.pushButton_nr_del.setText(_translate("Dialog", "Delete"))
        self.pushButton_nr_sqr.setText(_translate("Dialog", "Square"))
        self.pushButton_nr_destroy.setText(_translate("Dialog", "Destroy"))
        item = self.tableWidget_nr.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "code"))
        self.tableWidget_nr.setColumnWidth(0, 60)
        item = self.tableWidget_nr.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "trade"))
        self.tableWidget_nr.setColumnWidth(1, 40)
        item = self.tableWidget_nr.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "desc"))
        self.tableWidget_nr.setColumnWidth(2, 250)
        item = self.tableWidget_nr.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "ref"))
        self.tableWidget_nr.setColumnWidth(3, 60)
        item = self.tableWidget_nr.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "times"))
        self.tableWidget_nr.setColumnWidth(4, 60)
        item = self.tableWidget_nr.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "dims"))
        self.tableWidget_nr.setColumnWidth(5, 60)
        item = self.tableWidget_nr.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "square"))
        self.tableWidget_nr.setColumnWidth(6, 60)
        item = self.tableWidget_nr.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "unit"))
        self.tableWidget_nr.setColumnWidth(7, 30)
        item = self.tableWidget_nr.horizontalHeaderItem(8)
        item.setText(_translate("Dialog", "sign post"))
        self.tableWidget_nr.setColumnWidth(8, 100)

        self.pushButton_nr_clear.setText(_translate("Dialog", "Clear"))
        self.pushButton_nr_update.setText(_translate("Dialog", "Update"))

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
        self.tableWidget_nr.setRowCount(len(all_data))
        self.tableWidget_nr.setColumnCount(9)  # Column count set to 9

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

                self.tableWidget_nr.setItem(row_num, col_num - 1, item)  # Adjust column index

                if col_num == 9:  # "sign_post" column is at index 9
                    sign_post_value = str(col_data)  # Store the value of the sign_post column

            # Check if square value is negative and set row color to red
            if square_value < 0:
                for col in range(self.tableWidget_nr.columnCount()):
                    cell_item = self.tableWidget_nr.item(row_num, col)
                    cell_item.setForeground(QtGui.QColor('red'))

            # Check if sign_post_value == "SUM", set row foreground to blue
            if sign_post_value == "SUM":
                for col in range(self.tableWidget_nr.columnCount()):
                    cell_item = self.tableWidget_nr.item(row_num, col)
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
        num_rows = self.tableWidget_nr.rowCount()
        num_columns = self.tableWidget_nr.columnCount()

        # Iterate over each row in the table widget and insert the data into the database
        for row in range(num_rows):
            data = []
            for col in range(num_columns):
                item = self.tableWidget_nr.item(row, col)
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
        icon_path = os.path.join(os.path.dirname(__file__), "images", "info.png")
        icon_pixmap = QtGui.QPixmap(icon_path)
        msg_box.setIconPixmap(icon_pixmap)

        # Set the window modality to ApplicationModal
        msg_box.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)

        # Set the WindowStaysOnTopHint flag
        msg_box.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint)

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

            # Set the window modality to ApplicationModal
            msg_box.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)

            # Set the WindowStaysOnTopHint flag
            msg_box.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint)

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
