from base_window import BaseWindow
from PyQt6.QtWidgets import QPushButton

class InitialSetupPage(BaseWindow):
    def __init__(self, parent_window):
        super().__init__()
        self.parent_window = parent_window

        btn_admin = QPushButton("Setup as Admin")
        btn_user = QPushButton("Setup as User")

        for btn in (btn_admin, btn_user):
            btn.setMinimumHeight(40)

        btn_admin.clicked.connect(self.parent_window.go_to_admin_default)
        btn_user.clicked.connect(self.parent_window.go_to_user_setup)

        self.content_layout.addWidget(btn_admin)
        self.content_layout.addWidget(btn_user)
