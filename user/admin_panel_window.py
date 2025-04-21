from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from base_window import BaseWindow

class UserAdminPanelWindow(BaseWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("User Admin Panel")

        self.setting1 = QPushButton("Toggle Setting 1")
        self.setting2 = QPushButton("Toggle Setting 2")
        self.setting3 = QPushButton("Toggle Setting 3")
        self.delete_button = QPushButton("Completely Delete")

        self.content_layout.addWidget(self.setting1)
        self.content_layout.addWidget(self.setting2)
        self.content_layout.addWidget(self.setting3)
        self.content_layout.addWidget(self.delete_button)