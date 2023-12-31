from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFileDialog
from ProjectTreeWidget import Project_Widget
import json
import os


class NewProject_Dialog(object):
    def setupUi(self, Dialog):
        current_dir = os.getcwd()  # Get the current working directory

        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
        Dialog.resize(530, 360)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        Dialog.setFont(font)

        # Icon with relative path
        icon1 = QtGui.QIcon()
        image_path_to_icon1 = os.path.join(os.path.dirname(__file__), "images", "STO_IconPix.png")
        icon1.addPixmap(QtGui.QPixmap(image_path_to_icon1), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog.setWindowIcon(icon1)

        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 131, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 131, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit_prjtName = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_prjtName.setGeometry(QtCore.QRect(140, 10, 341, 22))
        self.lineEdit_prjtName.setObjectName("lineEdit_prjtName")
        self.lineEdit_prjtFolder = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_prjtFolder.setGeometry(QtCore.QRect(140, 40, 341, 22))
        self.lineEdit_prjtFolder.setObjectName("lineEdit_prjtFolder")

        self.lineEdit_prjtFolder.setText(current_dir)  # set the text of the cwd

        self.toolButton_openFolder = QtWidgets.QToolButton(parent=Dialog)
        self.toolButton_openFolder.setGeometry(QtCore.QRect(490, 40, 31, 21))
        icon = QtGui.QIcon()    # TODO Relative path to icon
        icon.addPixmap(QtGui.QPixmap("images\open.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_openFolder.setIcon(icon)
        self.toolButton_openFolder.setAutoRaise(True)
        self.toolButton_openFolder.setObjectName("toolButton_openFolder")

        # Connect signal
        self.toolButton_openFolder.clicked.connect(self.open_folder_dialog)

        self.checkBox = QtWidgets.QCheckBox(parent=Dialog)
        self.checkBox.setGeometry(QtCore.QRect(140, 70, 231, 21))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.groupBox = QtWidgets.QGroupBox(parent=Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 110, 481, 201))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(False)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.plainTextEdit_prjtScope = QtWidgets.QPlainTextEdit(parent=self.groupBox)
        self.plainTextEdit_prjtScope.setGeometry(QtCore.QRect(130, 63, 341, 51))
        self.plainTextEdit_prjtScope.setObjectName("plainTextEdit_prjtScope")
        self.radioButton_NRM2 = QtWidgets.QRadioButton(parent=self.groupBox)
        self.radioButton_NRM2.setGeometry(QtCore.QRect(230, 130, 61, 21))
        self.radioButton_NRM2.setObjectName("radioButton_NRM2")
        self.radioButton_SMM7 = QtWidgets.QRadioButton(parent=self.groupBox)
        self.radioButton_SMM7.setGeometry(QtCore.QRect(300, 130, 61, 21))
        self.radioButton_SMM7.setObjectName("radioButton_SMM7")

        # Activate SMM7 as default
        self.radioButton_SMM7.setChecked(True)

        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 101, 21))
        self.label_3.setObjectName("label_3")
        self.lineEdit_prjtTitle = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_prjtTitle.setGeometry(QtCore.QRect(140, 130, 341, 22))
        self.lineEdit_prjtTitle.setObjectName("lineEdit_prjtTitle")
        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 170, 101, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 240, 131, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 280, 101, 21))
        self.label_6.setObjectName("label_6")
        self.lineEdit_msdBy = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_msdBy.setGeometry(QtCore.QRect(140, 280, 341, 22))
        self.lineEdit_msdBy.setObjectName("lineEdit_msdBy")
        self.pushButton_OK = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_OK.setGeometry(QtCore.QRect(320, 320, 80, 26))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(False)
        self.pushButton_OK.setFont(font)
        self.pushButton_OK.setAutoDefault(False)
        self.pushButton_OK.setDefault(False)
        self.pushButton_OK.setObjectName("pushButton_OK")

        # Connect signal
        self.pushButton_OK.clicked.connect(lambda: self.save_project_details(Dialog))

        self.pushButton_cancel = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_cancel.setGeometry(QtCore.QRect(410, 320, 80, 26))
        self.pushButton_cancel.setObjectName("pushButton_cancel")

        # Connect signal
        self.pushButton_cancel.clicked.connect(lambda: self.cancel_project_setup(Dialog))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    # When OK button is clicked, save the input data into a dictionary
    def get_project_details(self):
        """
        Retrieves project details from UI elements and returns them as a dictionary.

        :return: A dictionary containing the project details.
        """
        project_name = self.lineEdit_prjtName.text()
        project_folder = self.lineEdit_prjtFolder.text()
        create_new_folder = self.checkBox.isChecked()
        project_scope = self.plainTextEdit_prjtScope.toPlainText()
        project_title = self.lineEdit_prjtTitle.text()
        smm_version = "NRM2" if self.radioButton_NRM2.isChecked() else "SMM7"
        measured_by = self.lineEdit_msdBy.text()

        project_details = {
            "Project Name": project_name,
            "Project Folder": project_folder,
            "Create New Folder": create_new_folder,
            "Project Scope": project_scope,
            "Project Title": project_title,
            "SMM Version": smm_version,
            "Measured By": measured_by
        }

        return project_details

    def save_project_details(self, Dialog):
        """
        Saves the project details to a JSON file and updates the Project_Widget to display the new folder.

        It retrieves project details using the get_project_details method, extracts relevant information, and creates
        a new folder if specified. The project details are converted to JSON and saved in the chosen file path or in
        a new folder. The method also updates UI elements, closes the dialog window, and updates the Project_Widget.

        :param Dialog: The dialog window object that needs to be closed after saving.

        :return: None
        """

        # Set the window flags to make the dialog stay on top
        Dialog.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)

        project_details = self.get_project_details()

        project_folder = project_details['Project Folder']
        create_new_folder = project_details['Create New Folder']
        project_name = project_details['Project Name']

        # Create a new folder if the checkbox is checked
        if create_new_folder:
            new_folder_name = project_details['Project Name']
            new_folder_path = os.path.join(project_folder, new_folder_name)

            try:
                os.makedirs(new_folder_path)
                print("New folder created:", new_folder_path)
            except OSError as e:
                print("Failed to create new folder:", e)
                return

            # Update the folder path with the new folder path
            project_details['Project Folder'] = new_folder_path

        json_data = json.dumps(project_details, indent=4)

        if create_new_folder:
            # Save the project details JSON file into the new folder
            file_path = os.path.join(new_folder_path, f"{project_name}.json")
        else:
            file_path, _ = QtWidgets.QFileDialog.getSaveFileName(
                parent=self.pushButton_OK,
                caption="Save Project Details",
                directory=f"{project_name}.json",
                filter="JSON Files (*.json)"
            )

        if file_path:
            with open(file_path, "w") as file:
                file.write(json_data)

        self.pushButton_OK.setText("Ok")  # Update the button text after saving

        Dialog.close()  # Close the dialog window

        # Update the Project_Widget to display the new folder
        project_widget = Project_Widget()
        project_widget.update_displayed_folder(new_folder_path)

    def open_folder_dialog(self):
        """
        Opens a folder dialog to select the Jobs directory.

        :return: None
        """
        current_dir = os.getcwd()  # Get the current working directory
        folder_path = os.path.join(current_dir, "Data", "Storages", "Local", "Jobs") # append path Jobs folder
        self.lineEdit_prjtFolder.setText(folder_path)

    def cancel_project_setup(self, Dialog):
        Dialog.close()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Create a New Project"))
        self.label.setText(_translate("Dialog", "Project Name :"))
        self.label_2.setText(_translate("Dialog", "Project Folder :"))
        self.toolButton_openFolder.setText(_translate("Dialog", "..."))
        self.checkBox.setText(_translate("Dialog", "Create new folder for this job."))
        self.groupBox.setTitle(_translate("Dialog", "Project Details"))
        self.radioButton_NRM2.setText(_translate("Dialog", "NRM2"))
        self.radioButton_SMM7.setText(_translate("Dialog", "SMM7"))
        self.label_3.setText(_translate("Dialog", "Project Title :"))
        self.label_4.setText(_translate("Dialog", "Project Scope :"))
        self.label_5.setText(_translate("Dialog", "Select SMM version :"))
        self.label_6.setText(_translate("Dialog", "Measured by :"))
        self.pushButton_OK.setText(_translate("Dialog", "OK"))
        self.pushButton_cancel.setText(_translate("Dialog", "Cancel"))
