from PyQt6.QtWidgets import QMainWindow, QStackedWidget
from windows.initial_setup_page import InitialSetupPage
from user.user_setup_page import UserSetupPage
from user.user_default_page import UserDefaultPage
from admin.admin_default_page import AdminDefaultPage
from user.admin_panel_page import AdminPanelPage
import configparser

class MainAppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WatchDog")

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.initial_setup = InitialSetupPage(self)
        self.user_setup = UserSetupPage(self)
        self.admin_default = AdminDefaultPage(self)
        self.user_main = UserDefaultPage(self)
        self.admin_panel = AdminPanelPage(self)

        self.stack.addWidget(self.initial_setup)
        self.stack.addWidget(self.user_setup)
        self.stack.addWidget(self.user_main)
        self.stack.addWidget(self.admin_default)
        self.stack.addWidget(self.admin_panel)

        setup_status = self.setup_check()
        match setup_status:
            case 'Admin':   
                self.stack.setCurrentWidget(self.admin_default)
            case 'User':
                self.stack.setCurrentWidget(self.user_main)
            case _:
                self.stack.setCurrentWidget(self.initial_setup)

    def setup_check(self):
        config = configparser.ConfigParser()
        config.read('config.ini')

        is_setup = config.getboolean('Initialisation', 'setup')
        account_type = config.get('Initialisation', 'account_type')

        if not is_setup or account_type == 'None':
            return None
        
        return account_type

    def go_to_user_setup(self):
        self.stack.setCurrentWidget(self.user_setup)

    def go_to_user_main(self):
        self.stack.setCurrentWidget(self.user_main)

    def go_to_admin_default(self):
        self.stack.setCurrentWidget(self.admin_default)

    def go_to_admin_panel(self):
        self.stack.setCurrentWidget(self.admin_panel)