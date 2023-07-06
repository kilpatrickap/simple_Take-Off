from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QFont, QPainter
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog

def create_pdf():
    printer = QPrinter(QPrinter.HighResolution)
    printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
    printer.setOutputFileName("tables.pdf")
    printer.setPageSize(QPrinter.PageSize.Letter)

    painter = QPainter(printer)
    painter.setFont(QFont("Arial", 10))

    print_dialog = QPrintDialog(printer)
    if print_dialog.exec() == QPrintDialog.PrintDialogResult.Accepted:
        print_preview(painter)

def print_preview(painter):
    # Create and populate the first table widget
    table1 = QTableWidget()
    table1.setColumnCount(3)
    table1.setRowCount(3)
    for row in range(3):
        for column in range(3):
            item = QTableWidgetItem(f"Table 1: Row {row}, Column {column}")
            table1.setItem(row, column, item)

    # Create and populate the second table widget
    table2 = QTableWidget()
    table2.setColumnCount(2)
    table2.setRowCount(4)
    for row in range(4):
        for column in range(2):
            item = QTableWidgetItem(f"Table 2: Row {row}, Column {column}")
            table2.setItem(row, column, item)

    # Set the sizes and positions of the table widgets
    table1.setGeometry(50, 50, 300, 200)
    table2.setGeometry(50, 300, 200, 150)

    # Render the table widgets on the printer
    table1.render(painter, QPoint(50, 50), table1.rect(), Qt.ItemSelectionMode.DontSelect)
    painter.drawText(50, 260, "Table 1")

    painter.drawText(50, 300, "Table 2")
    table2.render(painter, QPoint(50, 320), table2.rect(), Qt.ItemSelectionMode.DontSelect)

if __name__ == '__main__':
    app = QApplication([])
    window = QMainWindow()

    # Show the main window and execute the application event loop
    window.show()
    app.exec()

    # Generate the PDF file with the table widgets
    create_pdf()
