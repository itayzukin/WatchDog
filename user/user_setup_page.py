from base_window import BaseWindow
from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton

class UserSetupPage(BaseWindow):
    def __init__(self, parent_window):
        super().__init__()
        self.parent_window = parent_window

        label = QLabel("Create a password:")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        btn_signup = QPushButton("Sign Up")
        btn_signup.setMinimumHeight(40)
        btn_signup.clicked.connect(self.parent_window.go_to_user_main)

        self.content_layout.addWidget(label)
        self.content_layout.addWidget(self.password_input)
        self.content_layout.addWidget(btn_signup)