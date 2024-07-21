import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,
                             QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt

class SignupView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Signup Screen')
        self.setWindowIcon(QIcon('icon.png'))  # Set your window icon here
        
        # Create the title label
        title = QLabel('Signup Screen', self)
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont('Arial', 24))

        # Create username input
        self.usernameInputField = QLineEdit(self)
        self.usernameInputField.setPlaceholderText('Username')
        self.usernameInputField.setFont(QFont('Arial', 14))
        self.usernameInputField.setStyleSheet("padding: 10px; border: 1px solid gray; border-radius: 5px;")

        # Create password input
        self.passwordInputField = QLineEdit(self)
        self.passwordInputField.setPlaceholderText('Password')
        self.passwordInputField.setFont(QFont('Arial', 14))
        self.passwordInputField.setEchoMode(QLineEdit.Password)
        self.passwordInputField.setStyleSheet("padding: 10px; border: 1px solid gray; border-radius: 5px;")
        
        # Create confirm password input
        self.confirmPasswordInputField = QLineEdit(self)
        self.confirmPasswordInputField.setPlaceholderText('Confirm Password')
        self.confirmPasswordInputField.setFont(QFont('Arial', 14))
        self.confirmPasswordInputField.setEchoMode(QLineEdit.Password)
        self.confirmPasswordInputField.setStyleSheet("padding: 10px; border: 1px solid gray; border-radius: 5px;")

        # Create signup button
        self.signupButton = QPushButton('Sign Up', self)
        self.signupButton.setFont(QFont('Arial', 14))
        self.signupButton.setStyleSheet("""
            QPushButton {
                background-color: #008CBA;
                color: white;
                border: none;
                padding: 10px 20px;
                text-align: center;
                text-decoration: none;
                font-size: 16px;
                margin: 4px 2px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #007bb5;
            }
        """)
        self.signupButton.clicked.connect(self.handleSignup)

        # Create a main layout and add widgets
        layout = QVBoxLayout()
        layout.addStretch(1)
        layout.addWidget(title)
        layout.addSpacing(20)
        layout.addWidget(self.usernameInputField)
        layout.addSpacing(10)
        layout.addWidget(self.passwordInputField)
        layout.addSpacing(10)
        layout.addWidget(self.confirmPasswordInputField)
        layout.addSpacing(20)
        layout.addWidget(self.signupButton)
        layout.addStretch(1)
        
        # Set the layout for the main window
        self.setLayout(layout)
        
        # Set the main window size
        self.setGeometry(500, 300, 400, 400)
        self.setStyleSheet("background-color: #f5f5f5;")

    def handleSignup(self):
        username = self.usernameInputField.text()
        password = self.passwordInputField.text()
        confirm_password = self.confirmPasswordInputField.text()
        
        if username and password and confirm_password:
            if password == confirm_password:
                # Placeholder for actual signup logic
                QMessageBox.information(self, 'Success', 'Signed up successfully')
            else:
                QMessageBox.warning(self, 'Error', 'Passwords do not match')
        else:
            QMessageBox.warning(self, 'Error', 'Please fill in all fields')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    signupView = SignupView()
    signupView.show()
    sys.exit(app.exec_())
