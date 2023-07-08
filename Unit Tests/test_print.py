from PyQt6.QtPrintSupport import QPrinter, QPrintDialog
from PyQt6.QtGui import QPageSize
from PyQt6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem

if __name__ == '__main__':
    app = QApplication([])

    table = QTableWidget(10, 10)
    table.setMinimumSize(500, 500)

    # Populate the table with data
    for row in range(10):
        for column in range(10):
            item = QTableWidgetItem(f"Row {row}, Col {column}")
            table.setItem(row, column, item)

    # Resize columns and rows to fit contents
    table.resizeColumnsToContents()
    table.resizeRowsToContents()

    # Set printer properties for A4 landscape
    printer = QPrinter()
    printer.setPageSize(QPageSize(QPageSize.PageSizeId.A4))
    printer.setOrientation(QPrinter.Orientation.Landscape)

    dialog = QPrintDialog(printer)
    if dialog.exec() == QPrintDialog.DialogCode.Accepted:
        table.render(printer)

    app.exec()
