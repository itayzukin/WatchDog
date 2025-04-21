from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton
from admin.admin_panel_window import AdminPanelWindow
from base_window import BaseWindow

class AdminMainWindow(BaseWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Admin Login")

        self.ip_input = QLineEdit()
        self.ip_input.setPlaceholderText("Enter IP Address")

        self.port_input = QLineEdit()
        self.port_input.setPlaceholderText("Enter Port")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.connect_button = QPushButton("Connect")
        self.connect_button.clicked.connect(self.connect_to_panel)

        self.content_layout.addWidget(self.ip_input)
        self.content_layout.addWidget(self.port_input)
        self.content_layout.addWidget(self.password_input)
        self.content_layout.addWidget(self.connect_button)

    def connect_to_panel(self):
        self.panel = AdminPanelWindow()
        self.panel.show()
        self.close()
