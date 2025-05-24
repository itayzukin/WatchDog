from PyQt6.QtWidgets import QMainWindow, QStackedWidget
from windows.initial_setup_page import InitialSetupPage
from user.user_setup_page import UserSetupPage
from user.user_default_page import UserDefaultPage
from admin.admin_default_page import AdminDefaultPage
from user.admin_panel_page import AdminPanelPage as UserAdminPanelPage
from admin.admin_panel_page import AdminPanelPage
import thread_handler as th
import configparser


class MainAppWindow(QMainWindow):
    """
    Main application window managing stacked pages
    and initializing threads based on config setup.
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("WatchDog")

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # Initialize pages
        self.initial_setup = InitialSetupPage(self)
        self.user_setup = UserSetupPage(self)
        self.admin_default = AdminDefaultPage(self)
        self.user_main = UserDefaultPage(self)
        self.user_admin_panel = UserAdminPanelPage(self)
        self.admin_panel = AdminPanelPage(self)

        # Add pages to stack
        for widget in (
            self.initial_setup,
            self.user_setup,
            self.user_main,
            self.admin_default,
            self.user_admin_panel,
            self.admin_panel,
        ):
            self.stack.addWidget(widget)

        # Check setup and show appropriate page
        setup_status = self.setup_check()
        match setup_status:
            case 'Admin':
                self.stack.setCurrentWidget(self.admin_default)
            case 'User':
                th.enable_user_threads()
                self.stack.setCurrentWidget(self.user_main)
            case _:
                self.stack.setCurrentWidget(self.initial_setup)

    def setup_check(self) -> str | None:
        """
        Reads the config.ini to determine if setup was completed
        and returns the account type ('Admin' or 'User').
        Returns None if not set up.
        """
        config = configparser.ConfigParser()
        config.read('config.ini')

        try:
            is_setup = config.getboolean('Initialisation', 'setup')
            account_type = config.get('Initialisation', 'account_type')
        except (configparser.NoSectionError, configparser.NoOptionError):
            return None

        if not is_setup or account_type == 'None':
            return None

        return account_type

    # Navigation helper methods
    def go_to_user_setup(self):
        self.stack.setCurrentWidget(self.user_setup)

    def go_to_user_main(self):
        self.stack.setCurrentWidget(self.user_main)

    def go_to_admin_default(self):
        self.stack.setCurrentWidget(self.admin_default)

    def go_to_user_admin_panel(self):
        self.stack.setCurrentWidget(self.user_admin_panel)

    def go_to_admin_panel(self):
        self.stack.setCurrentWidget(self.admin_panel)
