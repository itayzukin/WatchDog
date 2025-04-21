from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from user.admin_panel_window import UserAdminPanelWindow
from base_window import BaseWindow

class UserMainWindow(BaseWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("User Monitor")

        self.monitoring_label = QLabel("You are being monitored.")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.login)

        self.content_layout.addWidget(self.monitoring_label)
        self.content_layout.addWidget(self.password_input)
        self.content_layout.addWidget(self.login_button)

    def login(self):
        self.panel = UserAdminPanelWindow()
        self.panel.show()
        self.close()