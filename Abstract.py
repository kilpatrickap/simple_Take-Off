import os
from PyQt6 import QtCore, QtGui, QtWidgets


class Abstract_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1011, 788)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton_sort = QtWidgets.QPushButton(parent=Dialog)

        # icon with relative path
        icon1 = QtGui.QIcon()
        image_path_to_icon1 = os.path.join(os.path.dirname(__file__), "images", "sort-alphabet.png")
        icon1.addPixmap(QtGui.QPixmap(image_path_to_icon1), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_sort.setIcon(icon1)
        self.pushButton_sort.setObjectName("pushButton_sort")
        self.horizontalLayout_2.addWidget(self.pushButton_sort)

        # icon with relative path
        self.pushButton_exportToExcel = QtWidgets.QPushButton(parent=Dialog)
        icon2 = QtGui.QIcon()
        image_path_to_icon2 = os.path.join(os.path.dirname(__file__), "images", "table-excel.png")
        icon2.addPixmap(QtGui.QPixmap(image_path_to_icon2), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_exportToExcel.setIcon(icon2)
        self.pushButton_exportToExcel.setObjectName("pushButton_exportToExcel")
        self.horizontalLayout_2.addWidget(self.pushButton_exportToExcel)

        # icon with relative path
        self.pushButton_exportToPdf = QtWidgets.QPushButton(parent=Dialog)
        icon3 = QtGui.QIcon()
        image_path_to_icon3 = os.path.join(os.path.dirname(__file__), "images", "pdf.png")
        icon3.addPixmap(QtGui.QPixmap(image_path_to_icon3), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_exportToPdf.setIcon(icon3)
        self.pushButton_exportToPdf.setObjectName("pushButton_exportToPdf")
        self.horizontalLayout_2.addWidget(self.pushButton_exportToPdf)

        # icon with relative path
        self.pushButton_printPreview = QtWidgets.QPushButton(parent=Dialog)
        icon4 = QtGui.QIcon()
        image_path_to_icon4 = os.path.join(os.path.dirname(__file__), "images", "printprev.png")
        icon4.addPixmap(QtGui.QPixmap(image_path_to_icon4), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_printPreview.setIcon(icon4)
        self.pushButton_printPreview.setObjectName("pushButton_printPreview")
        self.horizontalLayout_2.addWidget(self.pushButton_printPreview)

        # icon with relative path
        self.pushButton_print = QtWidgets.QPushButton(parent=Dialog)
        icon5 = QtGui.QIcon()
        image_path_to_icon5 = os.path.join(os.path.dirname(__file__), "images", "print.png")
        icon5.addPixmap(QtGui.QPixmap(image_path_to_icon5), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_print.setIcon(icon5)
        self.pushButton_print.setObjectName("pushButton_print")
        self.horizontalLayout_2.addWidget(self.pushButton_print)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.tableWidget_takeOff = QtWidgets.QTableWidget(parent=Dialog)
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
        self.verticalLayout.addWidget(self.tableWidget_takeOff)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)

        # icon with relative path
        self.pushButton_cancel = QtWidgets.QPushButton(parent=Dialog)
        icon6 = QtGui.QIcon()
        image_path_to_icon6 = os.path.join(os.path.dirname(__file__), "images", "x-circle-duotone.png")
        icon6.addPixmap(QtGui.QPixmap(image_path_to_icon6), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_cancel.setIcon(icon6)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout.addWidget(self.pushButton_cancel)

        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_sort.setText(_translate("Dialog", "Sort"))
        self.pushButton_exportToExcel.setText(_translate("Dialog", "Export to Excel"))
        self.pushButton_exportToPdf.setText(_translate("Dialog", "Export to Pdf"))
        self.pushButton_printPreview.setText(_translate("Dialog", "Print Preview"))
        self.pushButton_print.setText(_translate("Dialog", "Print"))
        item = self.tableWidget_takeOff.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "code"))
        item = self.tableWidget_takeOff.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "trade"))
        item = self.tableWidget_takeOff.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "desc"))
        item = self.tableWidget_takeOff.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "ref"))
        item = self.tableWidget_takeOff.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "times"))
        item = self.tableWidget_takeOff.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "dims"))
        item = self.tableWidget_takeOff.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "square"))
        item = self.tableWidget_takeOff.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "unit"))
        item = self.tableWidget_takeOff.horizontalHeaderItem(8)
        item.setText(_translate("Dialog", "sign post"))
        self.pushButton_cancel.setText(_translate("Dialog", "Cancel"))
