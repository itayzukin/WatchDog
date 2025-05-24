from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton
from windows.base_window import BaseWindow
from admin.auth_client_thread import AuthClientThread
import thread_handler as th
import admin.stream_client.global_vars as gv


class AdminDefaultPage(BaseWindow):
    """
    GUI window for admin login. Allows input of server IP, port, and password,
    and attempts to authenticate with the server.
    """

    def __init__(self, parent_window):
        """
        Initializes the login form with input fields and a connect button.

        Args:
            parent_window (QWidget): Reference to the main application window for navigation.
        """
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

        for widget in (
            self.ip_input,
            self.port_input,
            self.pass_input,
            btn_connect,
            self.error_label,
        ):
            self.content_layout.addWidget(widget)

    def try_connect(self):
        """
        Attempts to authenticate with the server using the provided credentials.
        Navigates to the admin panel if successful, otherwise displays an error message.
        """
        attempt_login = AuthClientThread(
            self.ip_input.text(),
            self.port_input.text(),
            self.pass_input.text()
        )
        attempt_login.start()

        answer = attempt_login.join()

        match answer:
            case "ACCEPTED":
                gv.server_ip = self.ip_input.text()
                gv.server_port = int(self.port_input.text())
                th.enable_admin_threads()
                self.parent_window.go_to_admin_panel()
            case "INCORRECT":
                self.error_label.setText("The password you've entered is incorrect")
            case "BLOCKED":
                self.error_label.setText("Due to many attempts, you've been blocked")
            case "INPUT_ERR":
                self.error_label.setText("Please enter valid credentials")
            case _:
                self.error_label.setText("Unknown error")

        del attempt_login
