from base_window import BaseWindow
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit

class UserDefaultPage(BaseWindow):
    def __init__(self, parent_window):
        super().__init__()
        self.parent_window = parent_window

        label = QLabel("You are being monitored.")
        label.setStyleSheet("font-size: 18px;")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter Admin Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        btn_login = QPushButton("Login to Admin Panel")
        btn_login.clicked.connect(self.parent_window.go_to_admin_panel)

        self.content_layout.addWidget(label)
        self.content_layout.addWidget(self.password_input)
        self.content_layout.addWidget(btn_login)