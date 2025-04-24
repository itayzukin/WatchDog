from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QFrame
from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtCore import Qt

class BaseWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(600, 300)

        # Top header with logo
        self.header = QFrame()
        self.header.setFixedHeight(60)
        self.header.setStyleSheet("background-color: #28a745;")

        self.logo_label = QLabel("LOGO")
        self.logo_label.setStyleSheet("font-weight: bold; color: black; margin-left: 15px;")
        self.logo_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        header_layout = QHBoxLayout()
        header_layout.addWidget(self.logo_label)
        header_layout.addStretch()
        self.header.setLayout(header_layout)

        # Main content area
        self.content = QFrame()
        self.content_layout = QVBoxLayout()
        self.content.setLayout(self.content_layout)

        # Combine header and content
        self.main_layout = QVBoxLayout(self)
        self.main_layout.addWidget(self.header)
        self.main_layout.addWidget(self.content)
