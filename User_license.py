import os

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import pyqtSignal


class User_license(QtCore.QObject):

    # Define the custom signal here using the pyqtSignal decorator
    cancelClicked = pyqtSignal()

    def __init__(self, Dialog):
        super().__init__()
        self.Dialog = Dialog

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        Dialog.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_email = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_email.setObjectName("lineEdit_email")

        # Connect signal
        self.lineEdit_email.returnPressed.connect(self.details)

        self.verticalLayout.addWidget(self.lineEdit_email)
        self.lineEdit_key = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_key.setObjectName("lineEdit_key")

        # Connect signal
        self.lineEdit_key.returnPressed.connect(self.details)

        self.verticalLayout.addWidget(self.lineEdit_key)
        self.pushButton_validate = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_validate.setObjectName("pushButton_validate")

        # Connect signal
        self.pushButton_validate.clicked.connect(self.validate)

        self.verticalLayout.addWidget(self.pushButton_validate)
        self.label_verify = QtWidgets.QLabel(parent=Dialog)
        self.label_verify.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_verify.setObjectName("label_verify")
        self.verticalLayout.addWidget(self.label_verify)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_daysRemaining = QtWidgets.QLabel(parent=Dialog)
        self.label_daysRemaining.setObjectName("label_daysRemaining")
        self.horizontalLayout.addWidget(self.label_daysRemaining)
        self.label_daysRemainingText = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        self.label_daysRemainingText.setFont(font)
        self.label_daysRemainingText.setObjectName("label_daysRemainingText")
        self.horizontalLayout.addWidget(self.label_daysRemainingText)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_expiry_notice = QtWidgets.QLabel(parent=Dialog)
        self.label_expiry_notice.setObjectName("label_expiry_notice")
        self.verticalLayout.addWidget(self.label_expiry_notice)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_proceed = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_proceed.setObjectName("pushButton_proceed")

        # Connect signal
        self.pushButton_proceed.clicked.connect(self.proceed)

        self.horizontalLayout_2.addWidget(self.pushButton_proceed)
        self.pushButton_Cancel = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_Cancel.setObjectName("pushButton_Cancel")

        # Connect signal
        self.pushButton_Cancel.clicked.connect(self.onCancelClicked)

        self.horizontalLayout_2.addWidget(self.pushButton_Cancel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "User License"))
        self.lineEdit_email.setPlaceholderText(_translate("Dialog", "Enter registered e-mail address from "
                                                                    "https://www.metiqs.com."))
        self.lineEdit_key.setPlaceholderText(_translate("Dialog", "Enter valid license keys to proceed."))
        self.pushButton_validate.setText(_translate("Dialog", "Validate License"))
        self.label_verify.setText(_translate("Dialog", "Waiting..."))
        self.label_daysRemaining.setText(_translate("Dialog", "Days remaining : "))
        self.label_daysRemainingText.setText(_translate("Dialog", "1"))
        self.label_expiry_notice.setText(_translate("Dialog", "Upon License expiry, contact 0541193598 for re-activation."))
        self.pushButton_proceed.setText(_translate("Dialog", "Proceed"))
        self.pushButton_Cancel.setText(_translate("Dialog", "Cancel"))

    def details(self):
        # Get the email and license key entered by the user from line edits
        email = self.lineEdit_email.text()
        license_key = self.lineEdit_key.text()

        # Call the credentials() method with the captured email and license key
        self.credentials(email, license_key)

    def credentials(self, email, license_key):
        # Combine email and license key into a single string
        credentials_str = f"Email: {email}\nLicense Key: {license_key}\n"

        # Get the current working directory
        current_directory = os.getcwd()

        # Create a file named 'credentials.txt' in the current working directory
        file_path = os.path.join(current_directory, "credentials.txt")

        # Write the credentials to the file
        with open(file_path, "w") as file:
            file.write(credentials_str)

        # Print a message indicating that the credentials have been saved
        print("Credentials have been saved to 'credentials.txt'.")
        
        
    def validate(self):
        # Verify
        if self.verify(key=self.lineEdit_key.text()):
            # Key is verified
            self.label_verify.setText("License key is VALID, proceed.")
        
    def verify(self, key):
        
        global score
        score = 0

        # Define our check digit
        check_digit = key[2]    # Say 3rd digit
        check_digit_count = 0   # Track how many times we see that digit in the key

        # aafa-bbfb-cccc-ddfd-1111
        # separate by hypen
        chunks = key.split('-')

        # Loop through chunks and check
        for chunk in chunks:
            if len(chunk) != 4:     # If chunk is < 4, return false
                return False

            for char in chunk:
                if char == check_digit:
                    check_digit_count += 1  # add 1 to the counter

                # Grab the score of the ANSCII char
                score += ord(char)      # ord() converts the numerical value of a char.

        # Check for rules
        if 1700 < score < 1800 and check_digit_count == 3:
            return True
        else:
            return False

    def proceed(self):
        self.Dialog.close()

    def onCancelClicked(self):
        # Emit the custom signal when the "Cancel" button is clicked
        self.cancelClicked.emit()
