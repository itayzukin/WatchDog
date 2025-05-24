from windows.base_window import BaseWindow
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit
import hashlib
import configparser
import os

class UserDefaultPage(BaseWindow):
    """
    User page allowing connection with password verification.
    """

    def __init__(self, parent_window):
        super().__init__()
        self.parent_window = parent_window
        self.config = configparser.ConfigParser()
        self.config.read("config.ini")

        label = QLabel("You're being monitored!")
        label.setStyleSheet("font-size: 18px;")
        label2 = QLabel("Enter admin password and click \"Turn Off\" to stop the program")
        label2.setStyleSheet("font-size: 12px;")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        btn_login = QPushButton("Turn Off")
        btn_login.clicked.connect(self.check_password)

        self.content_layout.addWidget(label)
        self.content_layout.addWidget(label2)
        self.content_layout.addWidget(self.password_input)
        self.content_layout.addWidget(btn_login)

    def check_password(self):
        """
        Check the entered password against the stored hash and
        navigate to the admin panel if it matches.
        """
        password = self.password_input.text()
        encrypted = hashlib.md5(password.encode()).hexdigest()

        if encrypted == self.config.get("Account", "password"):
            os.remove("config.ini")
            exit()
