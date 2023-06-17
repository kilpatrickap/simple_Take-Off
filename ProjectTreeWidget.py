from PyQt6 import QtCore, QtGui, QtWidgets

class ProjectWidgetTree_Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.treeWidget_project = QtWidgets.QTreeWidget(self)
        self.treeWidget_project.setObjectName("treeWidget_project")
        self.treeWidget_project.setHeaderLabels(["Project Folder"])

        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.addWidget(self.treeWidget_project)


        # self.setLayout(self.horizontalLayout)


# from PyQt6 import QtCore, QtGui, QtWidgets
#
# class ProjectWidgetTree_Form(QtWidgets.QWidget):
#     def setupUi(self, Form):
#         Form.setObjectName("Form")
#         Form.resize(791, 281)
#         self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Form)
#         self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
#         self.horizontalLayout_2.setObjectName("horizontalLayout_2")
#         self.treeWidget_project = QtWidgets.QTreeWidget(Form)
#         self.treeWidget_project.setObjectName("treeWidget_project")
#         self.horizontalLayout_2.addWidget(self.treeWidget_project)
#
#         self.retranslateUi(Form)
#         QtCore.QMetaObject.connectSlotsByName(Form)
#
#     def retranslateUi(self, Form):
#         _translate = QtCore.QCoreApplication.translate
#         Form.setWindowTitle(_translate("Form", "Form"))
#         self.treeWidget_project.headerItem().setText(0, _translate("Form", "Project Folder"))
#
# # if __name__ == "__main__":
# #     import sys
# #     app = QtWidgets.QApplication(sys.argv)
# #     Form = QtWidgets.QWidget()
# #     ui = Ui_Form()
# #     ui.setupUi(Form)
# #     Form.show()
# #     sys.exit(app.exec())