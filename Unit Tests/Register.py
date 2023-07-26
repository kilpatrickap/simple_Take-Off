from PyQt6 import QtCore, QtGui, QtWidgets
import random

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_generate = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_generate.setObjectName("pushButton_generate")

        # Connect signal
        self.pushButton_generate.clicked.connect(self.generate)

        self.verticalLayout.addWidget(self.pushButton_generate)
        self.lineEdit_key = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_key.setObjectName("lineEdit_key")
        self.verticalLayout.addWidget(self.lineEdit_key)
        self.label_verify = QtWidgets.QLabel(parent=Dialog)
        self.label_verify.setObjectName("label_verify")
        self.verticalLayout.addWidget(self.label_verify)
        self.label_score = QtWidgets.QLabel(parent=Dialog)
        self.label_score.setObjectName("label_score")
        self.verticalLayout.addWidget(self.label_score)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Register"))
        self.pushButton_generate.setText(_translate("Dialog", "Generate Key"))
        self.label_verify.setText(_translate("Dialog", "Waiting..."))
        self.label_score.setText(_translate("Dialog", "Score:"))

    def generate(self):
        # Clear the lineEdit_key
        self.lineEdit_key.clear()
        self.label_verify.setText("")

        # Set some defaults
        key = ''
        section = ''
        check_digit_count = 0
        alphabet = 'abcdefghijklmnopqrstuvwxyz1234567890'
        
        # key = aaaa-bbbb-cccc-dddd-1111 (5 sets of 4 or 24 chars)

        while len(key) < 25:
            # Randomly pick digit from alphabet
            char = random.choice(alphabet)
            # Add random choice to key
            key += char
            # Add random choice to the section blob
            section += char

            # Add in the hyphens
            if len(section) == 4:
                # Add in a hyphen
                key += '-'
                # Reset section to nothing
                section = ''

        # Set key to all but the last digit
        key = key[:-1]   # Everything up to the last digit

        # Output the key
        self.lineEdit_key.insert(key)








if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
