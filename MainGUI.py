import os
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1650, 900)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        MainWindow.setFont(font)

        # Icon with relative path
        icon1 = QtGui.QIcon()
        image_path_to_icon1 = os.path.join(os.path.dirname(__file__), "images", "TakeOffList.png")
        icon1.addPixmap(QtGui.QPixmap(image_path_to_icon1), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon1)

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #---TAB_M WIDGET STARTS HERE---
        self.tabWidget = QtWidgets.QTabWidget(parent=self)
        self.tabWidget.setGeometry(QtCore.QRect(10, 327, 800, 561))
        self.tabWidget.setObjectName("tabWidget")
        # #---TAB_M WIDGET ENDS HERE---

        # Current working directory label
        self.label_cwd = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_cwd.setObjectName("label_cwd")
        self.label_cwd.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)  # Align the label to the left
        size_policy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.MinimumExpanding,
            QtWidgets.QSizePolicy.Policy.Preferred
        )
        self.label_cwd.setSizePolicy(size_policy)  # Set the size policy

        # --- Setup Vert layout to contain TakeOff sheet here ---
        self.layoutWidget_takeOffSheet = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget_takeOffSheet.setGeometry(QtCore.QRect(0, 10, 1800, 900))
        self.layoutWidget_takeOffSheet.setObjectName("layoutWidget_takeOffSheet")

        self.verticalLayout_1 = QtWidgets.QVBoxLayout(self.layoutWidget_takeOffSheet)
        self.verticalLayout_1.setObjectName("verticalLayout_1")

        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 771, 261))
        self.layoutWidget.setObjectName("layoutWidget")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1650, 17))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(parent=self.menubar)
        self.menuAbout.setObjectName("menuAbout")

        # Connect signal
        self.menuAbout.triggered.connect(self.about)

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(parent=MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.actionNew = QtGui.QAction(parent=MainWindow)
        icon2 = QtGui.QIcon()
        image_path_to_icon2 = os.path.join(os.path.dirname(__file__), "images", "blue-folder--plus.png")
        icon2.addPixmap(QtGui.QPixmap(image_path_to_icon2), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionNew.setIcon(icon2)
        self.actionNew.setObjectName("actionNew")

        self.actionOpen = QtGui.QAction(parent=MainWindow)
        icon3 = QtGui.QIcon()
        image_path_to_icon3 = os.path.join(os.path.dirname(__file__), "images", "blue-folder-open-table.png")
        icon3.addPixmap(QtGui.QPixmap(image_path_to_icon3), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionOpen.setIcon(icon3)
        self.actionOpen.setObjectName("actionOpen")

        self.actionClose = QtGui.QAction(parent=MainWindow)
        icon6 = QtGui.QIcon()
        image_path_to_icon6 = os.path.join(os.path.dirname(__file__), "images", "blue-folder--minus.png")
        icon6.addPixmap(QtGui.QPixmap(image_path_to_icon6), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionClose.setIcon(icon6)
        self.actionClose.setObjectName("actionClose")

        self.actionExit = QtGui.QAction(parent=MainWindow)
        icon4 = QtGui.QIcon()
        image_path_to_icon4 = os.path.join(os.path.dirname(__file__), "images", "exit.png")
        icon4.addPixmap(QtGui.QPixmap(image_path_to_icon4), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionExit.setIcon(icon4)
        self.actionExit.setObjectName("actionExit")

        self.actionAbout = QtGui.QAction(parent=MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addSeparator()
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionClose)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simple Take-Off"))

        self.label_cwd.setText(_translate("MainWindow", f"    {os.getcwd()}"))

        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionClose.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

    def about(self):
        dialog = QtWidgets.QMessageBox()
        dialog.setWindowTitle("About")

        icon5 = QtGui.QIcon()
        image_path_to_icon5 = os.path.join(os.path.dirname(__file__), "images", "MetiQs.png")
        icon5.addPixmap(QtGui.QPixmap(image_path_to_icon5), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        dialog.setIconPixmap(icon5.pixmap(64, 64))  # Set the icon pixmap
        dialog.setText("Simple Take-Off\n\n"
                       "Simply and quickly perform taking-off measurments for building projects. \n\n"
                       "www.metiqs.com"
                       )
        dialog.addButton(QtWidgets.QMessageBox.StandardButton.Close)
        dialog.exec()

    def update_cwd_label(self, cwd):
        # Set the full text of the cwd in the label
        self.label_cwd.setText(cwd)

        # Resize the label to accommodate the full text
        self.label_cwd.adjustSize()
