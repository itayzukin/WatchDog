from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout
from admin.admin_main_window import AdminMainWindow
from user.user_setup_window import UserSetupWindow
from base_window import BaseWindow

class InitialSetupWindow(BaseWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Initial Setup")

        self.admin_button = QPushButton("Setup as Admin")
        self.user_button = QPushButton("Setup as User")

        self.admin_button.clicked.connect(self.open_admin)
        self.user_button.clicked.connect(self.open_user)

        self.content_layout.addWidget(self.admin_button)
        self.content_layout.addWidget(self.user_button)

    def open_admin(self):
        self.admin_window = AdminMainWindow()
        self.admin_window.show()
        self.close()

    def open_user(self):
        self.user_setup = UserSetupWindow()
        self.user_setup.show()
        self.close()