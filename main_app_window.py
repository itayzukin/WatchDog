from PyQt6.QtWidgets import QMainWindow, QStackedWidget
from initial_setup_page import InitialSetupPage
from user.user_setup_page import UserSetupPage
from user.user_default_page import UserDefaultPage
from admin.admin_default_page import AdminDefaultPage
from user.admin_panel_page import AdminPanelPage

class MainAppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WatchDog")
        self.setMinimumSize(600, 400)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # Pages
        self.initial_setup = InitialSetupPage(self)
        self.user_setup = UserSetupPage(self)
        self.user_main = UserDefaultPage(self)
        self.admin_default = AdminDefaultPage(self)
        self.admin_panel = AdminPanelPage(self)

        # Add to stack
        self.stack.addWidget(self.initial_setup)
        self.stack.addWidget(self.user_setup)
        self.stack.addWidget(self.user_main)
        self.stack.addWidget(self.admin_default)
        self.stack.addWidget(self.admin_panel)

        self.stack.setCurrentWidget(self.initial_setup)

    def go_to_user_setup(self):
        self.stack.setCurrentWidget(self.user_setup)

    def go_to_user_main(self):
        self.stack.setCurrentWidget(self.user_main)

    def go_to_admin_default(self):
        self.stack.setCurrentWidget(self.admin_default)

    def go_to_admin_panel(self):
        self.stack.setCurrentWidget(self.admin_panel)
