from windows.base_window import BaseWindow
from PyQt6.QtWidgets import QPushButton
import thread_handler as th
import configparser


class InitialSetupPage(BaseWindow):
    """
    Initial setup page to choose account type: Admin or User,
    and start respective threads accordingly.
    """

    def __init__(self, parent_window):
        super().__init__()
        self.parent_window = parent_window
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

        btn_admin = QPushButton("Admin")
        btn_user = QPushButton("User")

        for btn in (btn_admin, btn_user):
            btn.setMinimumHeight(40)

        btn_admin.clicked.connect(self.setup_as_admin)
        btn_user.clicked.connect(self.setup_as_user)

        self.content_layout.addWidget(btn_admin)
        self.content_layout.addWidget(btn_user)

    def setup_as_admin(self):
        """Set account type to Admin, enable admin threads, and navigate to admin default page."""
        self.set_account_type('Admin')
        th.enable_admin_threads()
        self.parent_window.go_to_admin_default()

    def setup_as_user(self):
        """Set account type to User and navigate to user setup page."""
        self.set_account_type('User')
        self.parent_window.go_to_user_setup()

    def set_account_type(self, value):
        """Set the account type in the config file."""
        self.config.set('Initialisation', 'account_type', value)
        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)
