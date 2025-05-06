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
        self.write_to_config('admin')
        self.parent_window.go_to_admin_default()
    
    def setup_as_user(self):
        self.write_to_config('user')
        self.parent_window.go_to_user_setup()
    
    def write_to_config(self, value):
        self.config.set('Initialisation','account_type',value)
        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)


