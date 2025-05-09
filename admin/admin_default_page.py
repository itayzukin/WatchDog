from windows.base_window import BaseWindow
from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton

class AdminDefaultPage(BaseWindow):
    def __init__(self, parent_window):
        super().__init__()
        self.parent_window = parent_window

        self.ip_input = QLineEdit()
        self.port_input = QLineEdit()
        self.pass_input = QLineEdit()

        self.ip_input.setPlaceholderText("IP Address")
        self.port_input.setPlaceholderText("Port")
        self.pass_input.setPlaceholderText("Password")
        self.pass_input.setEchoMode(QLineEdit.EchoMode.Password)

        btn_connect = QPushButton("Connect")
        btn_connect.clicked.connect(self.try_connect)

        for w in (self.ip_input, self.port_input, self.pass_input, btn_connect):
            self.content_layout.addWidget(w)

    def try_connect(self):
        # Placeholder check - replace with real logic
        if self.pass_input.text() == "admin":
            self.parent_window.go_to_admin_panel()
