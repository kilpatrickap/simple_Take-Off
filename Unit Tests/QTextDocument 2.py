import printer as printer
from PyQt6 import QtPrintSupport
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QTextDocument, QTextCursor, QTextTableFormat, QPageSize, QPainter
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog
from PyQt6.QtWidgets import QApplication, QTableWidget

if __name__ == '__main__':
    app = QApplication([])

    # Create a QTextDocument
    document = QTextDocument()

    # Create a QTextCursor to manipulate the document
    cursor = QTextCursor(document)

    # Create a QTextTableFormat to format the table
    table_format = QTextTableFormat()
    table_format.setAlignment(Qt.AlignmentFlag.AlignLeft)
    table_format.setCellPadding(4)
    table_format.setCellSpacing(0)

    # # Create the table
    table = cursor.insertTable(10, 10, table_format)

    # Populate the table with data
    for row in range(10):
        for col in range(10):
            # Get the cell at the current row and column
            cell = table.cellAt(row, col)
            # Set the text content of the cell
            cellCursor = cell.firstCursorPosition()
            cellCursor.insertText(f"Row {row+1}, Col {col+1}")

    printer = QPrinter()

    # Set the output format and file name for the printer
    printer.setOutputFormat(QtPrintSupport.QPrinter.OutputFormat.PdfFormat)

    # Set printer properties for A4 landscape
    printer = QPrinter()
    printer.setPageSize(QPageSize(QPageSize.PageSizeId.A3))

    dialog = QPrintDialog(printer)
    if dialog.exec() == QPrintDialog.DialogCode.Accepted:
        document.print(printer)

    app.exec()
