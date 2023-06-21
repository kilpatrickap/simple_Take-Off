import sqlite3

from PyQt6 import QtGui
from PyQt6.QtWidgets import QTableWidgetItem, QTableWidget


def load_table_data():
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

    # Check if the all_data list is empty
    if not all_data:
        return None

    # Create an instance of QTableWidget
    table_widget = QTableWidget()

    # Set the number of rows and columns in the QTableWidget
    table_widget.setRowCount(len(all_data))
    table_widget.setColumnCount(len(all_data[9]) - 1)  # Exclude ID

    # Populate the QTableWidget with the retrieved data
    for row_num, row_data in enumerate(all_data):
        square_value = 0.0  # Initialize square_value
        sign_post_value = None  # Initialize sign_post_value

        for col_num, col_data in enumerate(row_data):
            if col_num == 0:  # Exclude ID column
                continue

            item = QTableWidgetItem()

            if col_num == 7:  # "square" column is at index 7
                try:
                    square_value = float(col_data)
                    formatted_value = '{:,.2f}'.format(square_value)
                except ValueError:
                    formatted_value = str(col_data)
            else:
                formatted_value = str(col_data)

            item.setText(formatted_value)
            table_widget.setItem(row_num, col_num - 1, item)  # Adjust column index

            if col_num == 9:  # "sign_post" column is at index 9
                sign_post_value = str(col_data)  # Store the value of the sign_post column

        # Check if square value is negative and set row color to red
        if square_value < 0:
            for col in range(table_widget.columnCount()):
                cell_item = table_widget.item(row_num, col)
                cell_item.setForeground(QtGui.QColor('red'))

        # Check if sign_post_value == "SUM", set row foreground to blue
        if sign_post_value == "SUM":
            for col in range(table_widget.columnCount()):
                cell_item = table_widget.item(row_num, col)
                cell_item.setForeground(QtGui.QColor('blue'))

    # Close the database connection
    conn.close()

    return table_widget
