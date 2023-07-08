from PyQt6.QtPrintSupport import QPrinter, QPrintDialog
from PyQt6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem

if __name__ == '__main__':
    app = QApplication([])

    table = QTableWidget(10, 10)

    # Populate the table with data
    for row in range(10):
        for column in range(10):
            item = QTableWidgetItem(f"Row {row}, Col {column}")
            table.setItem(row, column, item)

    printer = QPrinter()
    dialog = QPrintDialog(printer)
    if dialog.exec() == QPrintDialog.DialogCode.Accepted:
        table.render(printer)

    app.exec()

    # def handlePrint(self):
    #     dialog = QtPrintSupport.QPrintDialog()
    #     if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
    #         self.handlePaintRequest(dialog.printer())