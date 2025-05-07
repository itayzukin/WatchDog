from base_window import BaseWindow
from PyQt6.QtWidgets import QPushButton
import configparser

class InitialSetupPage(BaseWindow):
    def __init__(self, parent_window):
        super().__init__()
        self.parent_window = parent_window
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

        btn_admin = QPushButton("Setup as Admin")
        btn_user = QPushButton("Setup as User")

        for btn in (btn_admin, btn_user):
            btn.setMinimumHeight(40)

        btn_admin.clicked.connect(self.setup_as_admin)
        btn_user.clicked.connect(self.setup_as_user)

        self.content_layout.addWidget(btn_admin)
        self.content_layout.addWidget(btn_user)

    def setup_as_admin(self):
        self.disable_setup()
        self.set_account_type('Admin')
        self.parent_window.go_to_admin_default()
    
    def setup_as_user(self):
        self.set_account_type('User')
        self.parent_window.go_to_user_setup()
    
    def disable_setup(self):
        self.config.set('Initialisation','setup', 'True')

    def set_account_type(self, value):
        self.config.set('Initialisation','account_type',value)
        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)