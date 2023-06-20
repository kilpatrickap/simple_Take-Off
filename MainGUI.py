# Form implementation generated from reading ui file 'MainGUI.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QLabel

from ProjectTreeWidget import Project_Widget
from TakeOffList import TakeOffList_Widget
from Tab_m import Tab_m_Widget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1650, 900)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/MetiQs.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)


        #---TAB_M WIDGET STARTS HERE---
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 280, 781, 561))
        self.tabWidget.setObjectName("tabWidget")


        # --- Setup Vert layout to contain TakeOff sheet here ---
        self.layoutWidget_takeOffSheet = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget_takeOffSheet.setGeometry(QtCore.QRect(900, 0, 900, 900))
        self.layoutWidget_takeOffSheet.setObjectName("layoutWidget_takeOffSheet")

        self.verticalLayout_1 = QtWidgets.QVBoxLayout(self.layoutWidget_takeOffSheet)
        self.verticalLayout_1.setObjectName("verticalLayout_1")

        self.label = QtWidgets.QLabel(parent=self.layoutWidget_takeOffSheet)
        self.label.setObjectName("Test6")
        self.label.setText("Testing")

        self.verticalLayout_1.addWidget(self.label)





        #---TAKE OFF SHEET STARTS HERE---
        # self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        # self.groupBox.setGeometry(QtCore.QRect(790, 10, 851, 831))
        # self.groupBox.setObjectName("groupBox")
        # ...
        # #---TAKE OFF SHEET ENDS HERE---






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
        self.menuEdit = QtWidgets.QMenu(parent=self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuAbout = QtWidgets.QMenu(parent=self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(parent=MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.actionNew = QtGui.QAction(parent=MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("images/new.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionNew.setIcon(icon17)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtGui.QAction(parent=MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("images/open.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionOpen.setIcon(icon18)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtGui.QAction(parent=MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("images/save.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionSave.setIcon(icon19)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtGui.QAction(parent=MainWindow)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("images/exit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionExit.setIcon(icon20)
        self.actionExit.setObjectName("actionExit")
        self.actionTake_Off_List = QtGui.QAction(parent=MainWindow)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap("images/TakeOffList.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionTake_Off_List.setIcon(icon21)
        self.actionTake_Off_List.setObjectName("actionTake_Off_List")
        self.actionUndo = QtGui.QAction(parent=MainWindow)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap("images/undo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionUndo.setIcon(icon22)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtGui.QAction(parent=MainWindow)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap("images/redo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionRedo.setIcon(icon23)
        self.actionRedo.setObjectName("actionRedo")
        self.actionAbout = QtGui.QAction(parent=MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionTake_Off_List)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionUndo)
        self.toolBar.addAction(self.actionRedo)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionTake_Off_List)

        self.retranslateUi(MainWindow)
        # self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Traditional Take-Off v1.0"))


        # #---TAKE OFF SHEET STARTS HERE---
        # self.groupBox.setTitle(_translate("MainWindow", "Take Off sheet"))
        # self.lineEdit_takeOff.setPlaceholderText(_translate("MainWindow", "Enter code"))
        #...
        # #---TAKE OFF SHEET ENDS HERE---


        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionTake_Off_List.setText(_translate("MainWindow", "export Take-Off"))
        self.actionTake_Off_List.setShortcut(_translate("MainWindow", "Ctrl+T"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionRedo.setShortcut(_translate("MainWindow", "Ctrl+Y"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
