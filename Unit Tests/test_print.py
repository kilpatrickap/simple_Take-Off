from PyQt6.QtPrintSupport import QPrinter, QPrintDialog
from PyQt6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem

if __name__ == '__main__':
    app = QApplication([])

    table = QTableWidget(10, 10)
    table.setMinimumSize(500, 500)

    # Populate the table with data
    for row in range(10):
        for column in range(10):
            item = QTableWidgetItem(f"Row{row}, Col {column}")
            table.setItem(row, column, item)

    printer = QPrinter()
    dialog = QPrintDialog(printer)
    if dialog.exec() == QPrintDialog.DialogCode.Accepted:
        table.render(printer)

    app.exec()