from windows.base_window import BaseWindow
from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton
from admin.auth_client_thread import AuthClientThread
import thread_handler as th

class AdminDefaultPage(BaseWindow):
    def __init__(self, parent_window):
        super().__init__()
        self.parent_window = parent_window

        self.ip_input = QLineEdit()
        self.port_input = QLineEdit()
        self.pass_input = QLineEdit()
        self.error_label = QLabel("")

        self.ip_input.setPlaceholderText("IP Address")
        self.port_input.setPlaceholderText("Port")
        self.pass_input.setPlaceholderText("Password")
        self.pass_input.setEchoMode(QLineEdit.EchoMode.Password)

        btn_connect = QPushButton("Connect")
        btn_connect.clicked.connect(self.try_connect)

        for w in (self.ip_input, self.port_input, self.pass_input, btn_connect, self.error_label):
            self.content_layout.addWidget(w)

    def try_connect(self):
        attempt_login = AuthClientThread(self.ip_input.text(), self.port_input.text(), self.pass_input.text())
        attempt_login.start()

        answer = attempt_login.join()

        match answer:
            case "ACCEPTED":
                th.enable_admin_threads()
                self.parent_window.go_to_admin_panel()
            case "INCORRECT":
                self.error_label.setText("The password you've entered is incorrect")
            case "BLOCKED":
                self.error_label.setText("Due to many attemptes, you've been blocked")
            case "INPUT_ERR":
                self.error_label.setText("Please enter valid credentials")
            case _:
                self.error_label.setText("Unknown error")

        del attempt_login