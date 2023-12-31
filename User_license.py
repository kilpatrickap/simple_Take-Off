import os
import random
from datetime import datetime, timedelta
import keyboard
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import pyqtSignal, Qt


class User_license(QtWidgets.QDialog):
    # Define the custom signal here using the pyqtSignal decorator
    cancelClicked = pyqtSignal()

    def __init__(self, Dialog):
        super().__init__()
        self.Dialog = Dialog

        # Hide the close button and window frame
        Dialog.setWindowFlags(self.windowFlags() | Qt.WindowType.FramelessWindowHint)

        # Block the escape key to prevent users from closing license Dialog to open app.
        keyboard.block_key("Esc")

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 300)
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
                                                                    "https://www.metiqs.com"))
        self.lineEdit_key.setPlaceholderText(_translate("Dialog", "Enter valid license key to proceed."))
        self.pushButton_validate.setText(_translate("Dialog", "Activate License"))
        self.label_verify.setText(_translate("Dialog", "Your license has expired."))

        self.label_daysRemaining.setText(_translate("Dialog", "Days remaining : "))
        self.label_daysRemainingText.setText(_translate("Dialog", f"{self.count_down()}"))

        self.label_position.setText(_translate("Dialog", "Position : "))
        self.label_positionText.setText(_translate("Dialog", f"{self.position()}"))

        self.label_count.setText(_translate("Dialog", "Count : "))
        self.label_countText.setText(_translate("Dialog", f"{self.count_valid_licenses()}"))

        self.label_expiry_notice.setText(
            _translate("Dialog", "Upon License expiry, contact +233541193598 for re-activation."))
        self.pushButton_proceed.setText(_translate("Dialog", "Proceed"))
        self.pushButton_Cancel.setText(_translate("Dialog", "Cancel"))

    def details(self):
        # Get the email and license key entered by the user from line edits
        email = self.lineEdit_email.text()
        license_key = self.lineEdit_key.text()

        # Call the credentials() method with the captured email and license key
        self.credentials(email, license_key)

    def credentials(self, email, license_key):
        # Set the installation date to the current date
        installation_date = datetime.now()

        # Set the expiration date to 1 day from the current time for testing purposes
        expiration_date = datetime.now() + timedelta(days=30)  # TODO change the expiration_date

        # Calculate the time remaining (in days) between installation and expiration
        time_remaining_days = (expiration_date - installation_date).days

        # Format the dates without milliseconds
        installation_date_str = installation_date.strftime("%Y-%m-%d %H:%M:%S")
        expiration_date_str = expiration_date.strftime("%Y-%m-%d %H:%M:%S")

        # Combine email, license key, installation date, expiration date, and time remaining into a single string
        credentials_str = f"Email: {email}\nLicense Key: {license_key}\n"
        credentials_str += f"Installation Date: {installation_date_str}\nExpiration Date: {expiration_date_str}\n"
        credentials_str += f"Time Remaining (Days): {time_remaining_days}\n"

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

            # Save the valid license key to 'valid_licenses.txt'
            self.save_valid_license(license_key)

            # Activate proceed button
            self.pushButton_proceed.setEnabled(True)
        else:
            self.label_verify.setText("INVALID License key!")

            # Reset time_remaining as 0 in credentials.txt
            self.save_remaining_days(0)

            # Reset count_down to 0.
            self.count_down(zero=True)

            # Deactivate proceed button
            self.pushButton_proceed.setEnabled(False)

    def save_valid_license(self, license_key):
        # Get the current working directory
        current_directory = os.getcwd()

        # Create the file path to 'valid_licenses.txt' in the current working directory
        file_path = os.path.join(current_directory, "licenses.lic")

        # Write the valid license key to the file
        with open(file_path, "a") as file:
            file.write(license_key + "\n")

    def count_valid_licenses(self):
        # Get the current working directory
        current_directory = os.getcwd()

        # Create the file path to 'valid_licenses.txt' in the current working directory
        file_path = os.path.join(current_directory, "licenses.lic")

        # Read the valid licenses from the file
        if not os.path.exists(file_path):
            # If 'valid_licenses.txt' does not exist, return 0
            return 0

        # Read the valid licenses from the file
        with open(file_path, "r") as file:
            valid_licenses = file.read().splitlines()

        return len(valid_licenses)

    def count_down(self, zero=False):
        # Get the installation date, expiration date, and time remaining from credentials.txt
        _, _, installation_date, expiration_date, time_remaining_minutes = self.load_credentials()

        # Calculate the number of minutes remaining until the expiration date
        current_datetime = datetime.now()
        remaining_days = (expiration_date - current_datetime).days

        # If the remaining minutes are less than 1.0, set remaining_minutes to 0 and save it to credentials.txt
        if remaining_days < 1:
            remaining_days = 0

            # Save the remaining_minutes
            self.save_remaining_days(remaining_days)

            # Clear the lineEdit_email field
            self.lineEdit_email.clear()

            # Clear the lineEdit_key field
            self.lineEdit_key.clear()

        if zero:
            # Save the remaining_minutes
            self.save_remaining_days(0)

        return remaining_days

    def save_remaining_days(self, remaining_days):
        # Read the existing credentials from credentials.txt
        email, license_key, installation_date, expiration_date, _ = self.load_credentials()

        # Format the dates without milliseconds
        installation_date_str = installation_date.strftime("%Y-%m-%d %H:%M:%S")
        expiration_date_str = expiration_date.strftime("%Y-%m-%d %H:%M:%S")

        # Combine email, license key, installation date, expiration date, and time remaining into a single string
        credentials_str = f"Email: {email}\nLicense Key: {license_key}\n"
        credentials_str += f"Installation Date: {installation_date_str}\nExpiration Date: {expiration_date_str}\n"
        credentials_str += f"Time Remaining (Days): {remaining_days}\n"

        # Get the current working directory
        current_directory = os.getcwd()

        # Create a file named 'credentials.txt' in the current working directory
        file_path = os.path.join(current_directory, "credentials.txt")

        # Write the credentials to the file
        with open(file_path, "w") as file:
            file.write(credentials_str)

        # Print a message indicating that the credentials have been updated
        print("Remaining days have been updated and saved to 'credentials.txt'.")

    def position(self):
        # Initialize the position
        initial_position = 0

        # Get the installation date, expiration date, and time remaining from credentials.txt
        _, _, _, expiration_date, remaining_days = self.load_credentials()
        print("Remaining days from credentials is:", remaining_days)

        # If remaining_minutes is 0, use the random position as the current_position
        if remaining_days == 0:

            # Clear the email and key fields.
            self.lineEdit_email.clear()
            self.lineEdit_key.clear()

            # Set the file path to the current working directory
            current_directory = os.getcwd()
            random_position_file = os.path.join(current_directory, "random_position.txt")

            if os.path.exists(random_position_file):
                # Generate a random number and write it to the file.
                random_position = random.randint(0, 3)  # Generate a random number
                with open(random_position_file, "w") as file:
                    file.write(str(random_position))

                # If the file exists, read the random position from it.
                with open(random_position_file, "r") as file:
                    random_position = int(file.read())

            # Make the random_position the current_position
            current_position = initial_position + random_position
            print("Random position is:", random_position)
            print("Current position is:", current_position)
            return int(current_position)  # Convert current_position to an integer

        else:
            # Freeze email/key/validate
            self.lineEdit_email.setEnabled(False)
            self.lineEdit_key.setEnabled(False)
            self.pushButton_validate.setEnabled(False)

            # Show the user the license is not expired
            self.label_verify.setText("Your Activated License has not expired")

            # Unfreeze proceed button
            self.pushButton_proceed.setEnabled(True)

            # Set focus policy to StrongFocus
            self.pushButton_proceed.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)

            # Read the random_position from random_position.txt
            current_directory = os.getcwd()
            random_position_file = os.path.join(current_directory, "random_position.txt")
            with open(random_position_file, "r") as file:
                random_position = int(file.read())

                # Make the random_position the initial_position
                initial_position = random_position

            return initial_position

    def _verify(self, key):
        global score
        score = 0

        # Define our check digit
        check_digit = key[self.position()]
        check_digit_count = 0  # Track how many times we see that digit in the key

        # aafa-bbfb-cccc-ddfd-1111
        # separate by hypen
        chunks = key.split('-')

        # Loop through chunks and check
        for chunk in chunks:
            if len(chunk) != 4:  # If chunk is < 4, return false
                return False

            for char in chunk:
                if char == check_digit:
                    check_digit_count += 1  # add 1 to the counter

                # Grab the score of the ANSCII char
                score += ord(char)  # ord() converts the numerical value of a char.

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

        # Extract email, license key, installation date, expiration date, and time remaining from credentials
        email = ""
        license_key = ""
        installation_date_str = ""
        expiration_date_str = ""
        time_remaining_str = ""

        lines = credentials.splitlines()
        for line in lines:
            if line.startswith("Email:"):
                email = line.split(":", 1)[1].strip()
            elif line.startswith("License Key:"):
                license_key = line.split(":", 1)[1].strip()
            elif line.startswith("Installation Date:"):
                installation_date_str = line.split(":", 1)[1].strip()
            elif line.startswith("Expiration Date:"):
                expiration_date_str = line.split(":", 1)[1].strip()
            elif line.startswith("Time Remaining (Days):"):
                time_remaining_str = line.split(":", 1)[1].strip()

        # Convert date strings to datetime objects
        installation_date = datetime.strptime(installation_date_str, "%Y-%m-%d %H:%M:%S")
        expiration_date = datetime.strptime(expiration_date_str, "%Y-%m-%d %H:%M:%S")

        # Convert time remaining to an integer
        try:
            time_remaining_days = int(float(time_remaining_str))
        except ValueError:
            time_remaining_days = 0

        return email, license_key, installation_date, expiration_date, time_remaining_days

    def proceed(self):
        self.Dialog.close()

        # Unblock the escape key.
        keyboard.unblock_key("Esc")

    def onCancelClicked(self):
        # Emit the custom signal when the "Cancel" button is clicked
        self.cancelClicked.emit()
