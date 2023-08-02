import os
import sqlite3
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QTableWidgetItem


class TakeOffSheet_Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setupUi()

    def setupUi(self):
        # self.setObjectName("self")
        self.setObjectName("TakeOffSheet_Widget")

        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(779, 0, 921, 830))
        self.groupBox.setObjectName("groupBox")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_code = QtWidgets.QLineEdit(parent=self.groupBox)

        self.pushButton_refresh = QtWidgets.QPushButton(parent=self.groupBox)
        # Add button icon with relative path
        icon4 = QtGui.QIcon()
        image_path_to_icon4 = os.path.join(os.path.dirname(__file__), "images", "arrow-circle-double-135.png")
        icon4.addPixmap(QtGui.QPixmap(image_path_to_icon4), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_refresh.setIcon(icon4)

        self.pushButton_refresh.setObjectName("pushButton_refresh")

        # Connect signal
        self.pushButton_refresh.clicked.connect(self.load_table_data)

        self.horizontalLayout_2.addWidget(self.pushButton_refresh)

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
        self.pushButton_search.clicked.connect(self.search_code)

        self.horizontalLayout_2.addWidget(self.pushButton_search)

        self.pushButton_edit = QtWidgets.QPushButton(parent=self.groupBox)

        # Add button icon with relative path
        icon2 = QtGui.QIcon()
        image_path_to_icon2 = os.path.join(os.path.dirname(__file__), "images", "pencil.png")
        icon2.addPixmap(QtGui.QPixmap(image_path_to_icon2), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_edit.setIcon(icon2)

        self.pushButton_edit.setObjectName("pushButton_edit")

        self.horizontalLayout_2.addWidget(self.pushButton_edit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)

        self.pushButton_abstract = QtWidgets.QPushButton(parent=self.groupBox)

        # Add button icon with relative path
        icon3 = QtGui.QIcon()
        image_path_to_icon3 = os.path.join(os.path.dirname(__file__), "images", "wand.png")
        icon3.addPixmap(QtGui.QPixmap(image_path_to_icon3), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_abstract.setIcon(icon3)

        self.pushButton_abstract.setObjectName("pushButton_abstract")
        self.horizontalLayout_2.addWidget(self.pushButton_abstract)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.tableWidget_takeOff = QtWidgets.QTableWidget(parent=self.groupBox)
        self.tableWidget_takeOff.setObjectName("tableWidget_takeOff")

        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.tableWidget_takeOff.setFont(font)

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

        self.pushButton_refresh.setText(_translate("groupBox", "Refresh"))
        self.lineEdit_code.setPlaceholderText(_translate("groupBox", "Enter code"))
        self.pushButton_search.setText(_translate("groupBox", "Search"))
        self.pushButton_edit.setText(_translate("groupBox", "Edit"))
        self.pushButton_abstract.setText(_translate("groupBox", "Abstract"))

        item = self.tableWidget_takeOff.horizontalHeaderItem(0)
        item.setText(_translate("groupBox", "code"))
        self.tableWidget_takeOff.setColumnWidth(0, 60)
        item = self.tableWidget_takeOff.horizontalHeaderItem(1)
        item.setText(_translate("groupBox", "trade"))
        self.tableWidget_takeOff.setColumnWidth(1, 40)
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

    def load_table_data(self):
        # Connect to the SQLite database
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()

        # Get the list of table names from the database
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()

        # Extract table names from the fetched data and store them in a list
        table_list = [table[0] for table in tables if table[0] != 'sqlite_sequence']  # Exclude the 'sqlite_sequence'

        # print(table_list)

        # Initialize an empty list to store all the retrieved data
        all_data = []

        # Iterate over each table in table_list
        for table_name in table_list:
            # Retrieve the data from the table
            cursor.execute(f'SELECT * FROM {table_name}')
            data = cursor.fetchall()

            # Append the retrieved data to the all_data list
            all_data.extend(data)

        # print(all_data)

        # Check if the all_data list is empty
        if not all_data:
            return

        # Set the number of rows and columns in the QTableWidget
        self.tableWidget_takeOff.setRowCount(len(all_data))
        self.tableWidget_takeOff.setColumnCount(9)  # Column count set to 9

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

            # Check if sign_post_value == "SUM", set row foreground to blue
            if sign_post_value == "TONNAGE":
                for col in range(self.tableWidget_takeOff.columnCount()):
                    cell_item = self.tableWidget_takeOff.item(row_num, col)
                    cell_item.setForeground(QtGui.QColor('green'))

        # Close the database connection
        conn.close()

    def search_code(self):
        entered_code = self.lineEdit_code.text()

        conn = sqlite3.connect('data.db')  # Connect to the "data.db" database
        cursor = conn.cursor()

        # Execute a query to search for the entered code in specific tables
        cursor.execute("""
            SELECT name FROM sqlite_master WHERE type='table' AND (
                name LIKE 'm_A%' 
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
                
                OR name LIKE 'm2_A%' 
                OR name LIKE 'm2_C%' 
                OR name LIKE 'm2_D%' 
                OR name LIKE 'm2_E%' 
                OR name LIKE 'm2_F%' 
                OR name LIKE 'm2_G%' 
                OR name LIKE 'm2_H%' 
                OR name LIKE 'm2_J%' 
                OR name LIKE 'm2_K%' 
                OR name LIKE 'm2_L%' 
                OR name LIKE 'm2_M%' 
                OR name LIKE 'm2_N%' 
                OR name LIKE 'm2_P%' 
                OR name LIKE 'm2_Q%' 
                OR name LIKE 'm2_R%' 
                OR name LIKE 'm2_S%' 
                OR name LIKE 'm2_T%' 
                OR name LIKE 'm2_U%' 
                OR name LIKE 'm2_V%' 
                OR name LIKE 'm2_W%' 
                OR name LIKE 'm2_X%'
                
                OR name LIKE 'm3_A%' 
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
                
                OR name LIKE 'nr_A%' 
                OR name LIKE 'nr_C%' 
                OR name LIKE 'nr_D%' 
                OR name LIKE 'nr_E%' 
                OR name LIKE 'nr_F%' 
                OR name LIKE 'nr_G%' 
                OR name LIKE 'nr_H%' 
                OR name LIKE 'nr_J%' 
                OR name LIKE 'nr_K%' 
                OR name LIKE 'nr_L%' 
                OR name LIKE 'nr_M%' 
                OR name LIKE 'nr_N%' 
                OR name LIKE 'nr_P%' 
                OR name LIKE 'nr_Q%' 
                OR name LIKE 'nr_R%' 
                OR name LIKE 'nr_S%' 
                OR name LIKE 'nr_T%' 
                OR name LIKE 'nr_U%' 
                OR name LIKE 'nr_V%' 
                OR name LIKE 'nr_W%' 
                OR name LIKE 'nr_X%'
                
                OR name LIKE 'rft_A%' 
                OR name LIKE 'rft_C%' 
                OR name LIKE 'rft_D%' 
                OR name LIKE 'rft_E%' 
                OR name LIKE 'rft_F%' 
                OR name LIKE 'rft_G%' 
                OR name LIKE 'rft_H%' 
                OR name LIKE 'rft_J%' 
                OR name LIKE 'rft_K%' 
                OR name LIKE 'rft_L%' 
                OR name LIKE 'rft_M%' 
                OR name LIKE 'rft_N%' 
                OR name LIKE 'rft_P%' 
                OR name LIKE 'rft_Q%' 
                OR name LIKE 'rft_R%' 
                OR name LIKE 'rft_S%' 
                OR name LIKE 'rft_T%' 
                OR name LIKE 'rft_U%' 
                OR name LIKE 'rft_V%' 
                OR name LIKE 'rft_W%' 
                OR name LIKE 'rft_X%'
            )
        """)

        tables = cursor.fetchall()

        # Clear the existing data in the tableWidget_takeOff
        self.tableWidget_takeOff.clearContents()
        self.tableWidget_takeOff.setRowCount(0)

        if tables:
            for table in tables:
                table_name = table[0]

                # Execute a query to retrieve rows from the matching table
                cursor.execute("SELECT * FROM {} WHERE code=?".format(table_name), (entered_code,))
                rows = cursor.fetchall()

                for row in rows:
                    # Add a new row to the tableWidget_takeOff
                    self.tableWidget_takeOff.insertRow(self.tableWidget_takeOff.rowCount())

                    # Populate the cells of the new row with the fetched data
                    for column, value in enumerate(row):
                        item = QTableWidgetItem(str(value))
                        self.tableWidget_takeOff.setItem(self.tableWidget_takeOff.rowCount() - 1, column - 1, item)
        else:
            # No matching tables found
            pass

        conn.close()

        return entered_code
