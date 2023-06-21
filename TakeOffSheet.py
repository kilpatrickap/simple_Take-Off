import os
import sqlite3
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QTableWidgetItem, QTableWidget, QVBoxLayout


class TakeOffSheet_Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setupUi()

    def setupUi(self):
        # self.setObjectName("self")
        self.setObjectName("TakeOffSheet_Widget")

        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(779, 0, 851, 830))
        self.groupBox.setObjectName("groupBox")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_code = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_code.setObjectName("lineEdit_code")
        self.horizontalLayout_2.addWidget(self.lineEdit_code)

        self.pushButton_search = QtWidgets.QPushButton(parent=self.groupBox)

        # Add button icon with relative path
        icon1 = QtGui.QIcon()
        image_path_to_icon1 = os.path.join(os.path.dirname(__file__), "images", "magnifier-left.png")
        icon1.addPixmap(QtGui.QPixmap(image_path_to_icon1), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_search.setIcon(icon1)

        self.pushButton_search.setObjectName("pushButton_search")

        # Connect signal
        # self.pushButton_search.clicked.connect(self.search_code)

        self.horizontalLayout_2.addWidget(self.pushButton_search)

        self.pushButton_edit = QtWidgets.QPushButton(parent=self.groupBox)

        # Add button icon with relative path
        icon2 = QtGui.QIcon()
        image_path_to_icon2 = os.path.join(os.path.dirname(__file__), "images", "pencil.png")
        icon2.addPixmap(QtGui.QPixmap(image_path_to_icon2), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_edit.setIcon(icon2)

        self.pushButton_edit.setObjectName("pushButton_edit")

        # Connect signal
        # self.pushButton_edit.clicked.connect(self.edit_code)

        self.horizontalLayout_2.addWidget(self.pushButton_edit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)

        self.pushButton_abstract = QtWidgets.QPushButton(parent=self.groupBox)

        # Add button icon with relative path
        icon3 = QtGui.QIcon()
        image_path_to_icon3 = os.path.join(os.path.dirname(__file__), "images", "notebook.png")
        icon3.addPixmap(QtGui.QPixmap(image_path_to_icon3), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_abstract.setIcon(icon3)

        self.pushButton_abstract.setObjectName("pushButton_abstract")
        self.horizontalLayout_2.addWidget(self.pushButton_abstract)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.tableWidget_takeOff = QtWidgets.QTableWidget(parent=self.groupBox)
        self.tableWidget_takeOff.setObjectName("tableWidget_takeOff")
        self.tableWidget_takeOff.setColumnCount(9)
        self.tableWidget_takeOff.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_takeOff.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_takeOff.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_takeOff.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_takeOff.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_takeOff.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_takeOff.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_takeOff.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_takeOff.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_takeOff.setHorizontalHeaderItem(8, item)
        self.verticalLayout_2.addWidget(self.tableWidget_takeOff)

        # #---TAKE OFF SHEET ENDS HERE---
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("groupBox", "groupBox"))

        self.groupBox.setTitle(_translate("groupBox", "Take Off sheet"))

        self.lineEdit_code.setPlaceholderText(_translate("groupBox", "Enter code"))
        self.pushButton_search.setText(_translate("groupBox", "Search"))
        self.pushButton_edit.setText(_translate("groupBox", "Edit"))
        self.pushButton_abstract.setText(_translate("groupBox", "Abstract"))

        item = self.tableWidget_takeOff.horizontalHeaderItem(0)
        item.setText(_translate("groupBox", "code"))
        self.tableWidget_takeOff.setColumnWidth(0, 60)
        item = self.tableWidget_takeOff.horizontalHeaderItem(1)
        item.setText(_translate("groupBox", "trade"))
        self.tableWidget_takeOff.setColumnWidth(1, 60)
        item = self.tableWidget_takeOff.horizontalHeaderItem(2)
        item.setText(_translate("groupBox", "desc"))
        self.tableWidget_takeOff.setColumnWidth(2, 300)
        item = self.tableWidget_takeOff.horizontalHeaderItem(3)
        item.setText(_translate("groupBox", "ref"))
        self.tableWidget_takeOff.setColumnWidth(3, 60)
        item = self.tableWidget_takeOff.horizontalHeaderItem(4)
        item.setText(_translate("groupBox", "times"))
        self.tableWidget_takeOff.setColumnWidth(4, 60)
        item = self.tableWidget_takeOff.horizontalHeaderItem(5)
        item.setText(_translate("groupBox", "dims"))
        self.tableWidget_takeOff.setColumnWidth(5, 60)
        item = self.tableWidget_takeOff.horizontalHeaderItem(6)
        item.setText(_translate("groupBox", "square"))
        self.tableWidget_takeOff.setColumnWidth(6, 60)
        item = self.tableWidget_takeOff.horizontalHeaderItem(7)
        item.setText(_translate("groupBox", "unit"))
        self.tableWidget_takeOff.setColumnWidth(7, 30)
        item = self.tableWidget_takeOff.horizontalHeaderItem(8)
        item.setText(_translate("groupBox", "sign post"))
        self.tableWidget_takeOff.setColumnWidth(8, 160)

        # Run method
        self.load_table_data()

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
        self.tableWidget_takeOff.setColumnCount(len(all_data[9]) - 1)

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




    # def save_takeOff_database(self):
    #     conn = sqlite3.connect('takeOff.db')  # Create or connect to the "takeOff.db" database
    #     cursor = conn.cursor()
    #
    #     # Create the "takeOff" table if it doesn't exist
    #     cursor.execute("""
    #         CREATE TABLE IF NOT EXISTS takeOff (
    #             id     INTEGER PRIMARY KEY AUTOINCREMENT,
    #             code   TEXT,
    #             trade  TEXT,
    #             desc   TEXT,
    #             ref    TEXT,
    #             times  TEXT,
    #             dims   TEXT,
    #             square INTEGER,
    #             unit   TEXT,
    #             sign_post TEXT,
    #             UNIQUE(id)
    #         )
    #     """)
    #
    #     rows = self.tableWidget_takeOff.rowCount()
    #     for row in range(rows):
    #         code = self.tableWidget_takeOff.item(row, 0).text()
    #         trade = self.tableWidget_takeOff.item(row, 1).text()
    #         desc = self.tableWidget_takeOff.item(row, 2).text()
    #         ref = self.tableWidget_takeOff.item(row, 3).text()
    #         times = self.tableWidget_takeOff.item(row, 4).text()
    #         dims = self.tableWidget_takeOff.item(row, 5).text()
    #         square = self.tableWidget_takeOff.item(row, 6).text()
    #         unit = self.tableWidget_takeOff.item(row, 7).text()
    #         sign_post = self.tableWidget_takeOff.item(row, 8).text()
    #
    #         # Check if the row already exists in the table
    #         cursor.execute("""
    #             SELECT * FROM takeOff WHERE code = ? AND trade = ? AND desc = ? AND ref = ? AND times = ? AND dims = ?
    #             AND square = ? AND unit = ? AND sign_post = ?
    #         """, (code, trade, desc, ref, times, dims, square, unit, sign_post))
    #
    #         existing_row = cursor.fetchone()
    #         if existing_row is None:
    #             # Row does not exist, insert it into the table
    #             cursor.execute("""
    #                 INSERT INTO takeOff (code, trade, desc, ref, times, dims, square, unit, sign_post)
    #                 VALUES (?,?,?,?,?,?,?,?,?)
    #             """, (code, trade, desc, ref, times, dims, square, unit, sign_post))
    #
    #     conn.commit()  # Save the changes
    #     conn.close()  # Close the connection
    #
    #     print("Data is saved to takeOff.db")
    #
    # def search_code(self):
    #     entered_code = self.lineEdit_code.text()
    #     print(entered_code)
    #
    #     conn = sqlite3.connect('takeOff.db')  # Connect to the "takeOff.db" database
    #     cursor = conn.cursor()
    #
    #     # Execute a query to search for the entered code in all the columns of the 'takeOff' table
    #     cursor.execute("SELECT * FROM takeOff WHERE code=?", (entered_code,))
    #     rows = cursor.fetchall()
    #
    #     # Slice the id column returned from the takeOff.db using list comprehension. [1:] starts from 2nd element
    #     rows = [row[1:] for row in rows]
    #
    #     # Clear the existing data in the tableWidget_takeOff
    #     self.tableWidget_takeOff.clearContents()
    #     self.tableWidget_takeOff.setRowCount(0)
    #
    #     if rows:
    #         print("Matching rows:")
    #         for row in rows:
    #             print(row)
    #             # Add a new row to the tableWidget_takeOff
    #             self.tableWidget_takeOff.insertRow(self.tableWidget_takeOff.rowCount())
    #
    #             # # Populate the cells of the new row with the fetched data
    #             for column, value in enumerate(row):
    #                 item = QTableWidgetItem(str(value))
    #                 self.tableWidget_takeOff.setItem(self.tableWidget_takeOff.rowCount() - 1, column, item)
    #     else:
    #         print("No matching rows")
    #
    #     conn.close()
    #
    #
    # def edit_code(self):  # TODO edit_code() should be in a separate tableWidget window
    #     entered_code = self.lineEdit_code.text()
    #     print("Entered code:", entered_code)
    #
    #     # Connect to the 'takeOff.db' database
    #     conn = sqlite3.connect('takeOff.db')  # TODO only edit tables in (m_data, m2_data, m3_data, item_data etc)
    #     cursor = conn.cursor()
    #
    #     # Execute a query to search for the entered code in the 'takeOff' table
    #     cursor.execute("SELECT * FROM takeOff WHERE code=?", (entered_code,))
    #     rows = cursor.fetchall()
    #
    #     # Slice the id column returned from the takeOff.db using list comprehension. [1:] starts from 2nd element
    #     rows = [row[1:] for row in rows]
    #
    #     if rows:
    #         print(f"Code '{entered_code}' found:")
    #
    #         # Set the label_code text to the entered code
    #         self.label_code.setText(entered_code)
    #
    #         for row in rows:
    #             print(row)
    #             # Add a new row to the tableWidget_m
    #             self.tableWidget_m.insertRow(self.tableWidget_m.rowCount())
    #
    #             # Populate the cells of the new row with the fetched data
    #             for column, value in enumerate(row):
    #                 item = QTableWidgetItem(str(value))
    #                 self.tableWidget_m.setItem(self.tableWidget_m.rowCount() - 1, column, item)
    #     else:
    #         print(f"Code '{entered_code}' not found")
    #
    #         # Clear the label_code text
    #         self.label_code.setText(f"'{entered_code}' not found!")
    #
    #     conn.close()
    #
