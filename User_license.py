import os
import random

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import pyqtSignal


class User_license(QtCore.QObject):

    # Define the custom signal here using the pyqtSignal decorator
    cancelClicked = pyqtSignal()

    def __init__(self, Dialog):
        super().__init__()
        self.Dialog = Dialog

        # Load credentials on initialization
        self.load_credentials()

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
        self.pushButton_validate.clicked.connect(self._validate)

        self.verticalLayout.addWidget(self.pushButton_validate)
        self.label_verify = QtWidgets.QLabel(parent=Dialog)
        self.label_verify.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_verify.setObjectName("label_verify")
        self.verticalLayout.addWidget(self.label_verify)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Days Remaining
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

        # Position
        self.label_position = QtWidgets.QLabel(parent=Dialog)
        self.label_position.setObjectName("position")
        self.horizontalLayout.addWidget(self.label_position)

        self.label_positionText = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        self.label_positionText.setFont(font)
        self.label_positionText.setObjectName("label_positionText")
        self.horizontalLayout.addWidget(self.label_positionText)

        # Count
        self.label_count = QtWidgets.QLabel(parent=Dialog)
        self.label_count.setObjectName("count")
        self.horizontalLayout.addWidget(self.label_count)

        self.label_countText = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        self.label_countText.setFont(font)
        self.label_positionText.setObjectName("label_countText")
        self.horizontalLayout.addWidget(self.label_countText)







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

        # De-activate when app loads
        self.pushButton_proceed.setEnabled(False)

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
        self.label_daysRemainingText.setText(_translate("Dialog", "0"))

        self.label_position.setText(_translate("Dialog", "Position : "))
        self.label_positionText.setText(_translate("Dialog", "1"))

        self.label_count.setText(_translate("Dialog", "Count : "))
        self.label_countText.setText(_translate("Dialog", "1"))

        self.label_expiry_notice.setText(_translate("Dialog", "Upon License expiry, contact 0541193598 for re-activation."))
        self.pushButton_proceed.setText(_translate("Dialog", "Proceed"))
        self.pushButton_Cancel.setText(_translate("Dialog", "Cancel"))

        # Retrieve the credentials
        email, license_key = self.load_credentials()
        if email and license_key:
            self.lineEdit_email.setText(email)
            print(f"Email: {email}")

            self.lineEdit_key.setText(license_key)
            print(f"License Key: {license_key}")
        else:
            print("No saved credentials found.")

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
        
        
    def _validate(self):
        # Get the entered license key
        license_key = self.lineEdit_key.text()

        if not license_key:
            # If the license key is empty, display a message
            self.label_verify.setText("Please enter your email and license key")
            return

        # Verify the license key
        if self._verify(key=license_key):
            # Key is verified
            self.label_verify.setText("License key is VALID, proceed.")

            # Activate proceed button
            self.pushButton_proceed.setEnabled(True)
        else:
            self.label_verify.setText("INVALID License key!")

            # Deactivate proceed button
            self.pushButton_proceed.setEnabled(False)

    def random_number(self):
        # If label_daysRemaining is 0 (license has expired) , generate random number.
        if self.label_daysRemainingText.text() == '0':

            # Deactivate validate button
            self.pushButton_validate.setEnabled(False)
            self.pushButton_validate.setText("License expired")

            # Generate a random number from 0 <= 4
            rand_nr = int(random.randint(0, 4))
            print(rand_nr)
            self.label_positionText.setText(str(rand_nr))

            return rand_nr

        else:
            return 3
        
    def _verify(self, key):
        
        global score
        score = 0

        # Get the random check digit
        check_digit = key[self.random_number()]    # Say 3rd digit
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

    def load_credentials(self):
        # Get the current working directory
        current_directory = os.getcwd()

        # Create the file path to 'credentials.txt' in the current working directory
        file_path = os.path.join(current_directory, "credentials.txt")

        if not os.path.exists(file_path):
            # If 'credentials.txt' does not exist, return without loading credentials
            return

        # Read the credentials from the file
        with open(file_path, "r") as file:
            credentials = file.read()

        # Extract email and license key from credentials
        email = ""
        license_key = ""
        lines = credentials.splitlines()
        for line in lines:
            if line.startswith("Email:"):
                email = line.split(":", 1)[1].strip()
                # print(email)
            elif line.startswith("License Key:"):
                license_key = line.split(":", 1)[1].strip()
                # print(license_key)

        return email, license_key

    def proceed(self):
        self.Dialog.close()

    def onCancelClicked(self):
        # Emit the custom signal when the "Cancel" button is clicked
        self.cancelClicked.emit()
