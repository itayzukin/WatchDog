from windows.base_window import BaseWindow
from PyQt6.QtWidgets import QLabel, QPushButton, QHBoxLayout


class AdminPanelPage(BaseWindow):
    """
    Admin panel page containing toggle settings and a delete button.
    """

    def __init__(self, parent_window):
        super().__init__()

        label = QLabel("Admin Panel Settings")
        label.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.content_layout.addWidget(label)

        toggle_buttons = ["Monitor On/Off", "Notifications", "Tracking"]

        for name in toggle_buttons:
            row = QHBoxLayout()
            row.addWidget(QLabel(name))
            btn = QPushButton("Toggle")
            row.addWidget(btn)
            self.content_layout.addLayout(row)

        btn_delete = QPushButton("Delete All")
        btn_delete.setStyleSheet("background-color: red; color: white;")
        self.content_layout.addWidget(btn_delete)
