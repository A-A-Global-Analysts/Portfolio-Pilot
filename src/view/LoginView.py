import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,
                             QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt

class LoginView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Login Screen')
        self.setWindowIcon(QIcon('icon.png'))  # Set your window icon here
        
        # Create the title label
        title = QLabel('Portfolio Pilot Login', self)
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

        # Create login button
        self.logInButton = QPushButton('Log In', self)
        self.logInButton.setFont(QFont('Arial', 14))
        self.logInButton.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
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
                background-color: #45a049;
            }
        """)
        self.logInButton.clicked.connect(self.handleLogin)

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

        # Create a layout for buttons
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.logInButton)
        buttonLayout.addWidget(self.signupButton)
        buttonLayout.setSpacing(20)

        # Create a main layout and add widgets
        layout = QVBoxLayout()
        layout.addStretch(1)
        layout.addWidget(title)
        layout.addSpacing(20)
        layout.addWidget(self.usernameInputField)
        layout.addSpacing(10)
        layout.addWidget(self.passwordInputField)
        layout.addSpacing(20)
        layout.addLayout(buttonLayout)
        layout.addStretch(1)
        
        # Set the layout for the main window
        self.setLayout(layout)
        
        # Set the main window size
        self.setGeometry(500, 300, 400, 300)
        self.setStyleSheet("background-color: #f5f5f5;")

    def handleLogin(self):
        username = self.usernameInputField.text()
        password = self.passwordInputField.text()
        
        if username and password:
            # Placeholder for actual login logic
            QMessageBox.information(self, 'Success', 'Logged in successfully')
        else:
            QMessageBox.warning(self, 'Error', 'Please enter a valid username and password')
    
    def handleSignup(self):
        # Placeholder for actual signup logic
        QMessageBox.information(self, 'Signup', 'Signup process initiated')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    loginView = LoginView()
    loginView.show()
    sys.exit(app.exec_())
