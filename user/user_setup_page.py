from windows.base_window import BaseWindow
from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton
import configparser
import hashlib

class UserSetupPage(BaseWindow):
    def __init__(self, parent_window):
        super().__init__()
        self.parent_window = parent_window
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

        label = QLabel("Create a password:")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        btn_signup = QPushButton("Sign Up")
        btn_signup.setMinimumHeight(40)
        btn_signup.clicked.connect(self.check_password)

        self.content_layout.addWidget(label)
        self.content_layout.addWidget(self.password_input)
        self.content_layout.addWidget(btn_signup)

    def check_password(self):
        password = self.password_input.text()
        encrypted = hashlib.md5(password.encode()).hexdigest()

        self.write_to_config(encrypted)
        self.parent_window.go_to_user_main()

    def write_to_config(self, password):
        self.config['Account'] = {'password': password}
        self.config.set('Initialisation','setup', 'True')
        self.config.set('Initialisation','account_type', 'User')

        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)