from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QFrame
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class BaseWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(600, 400)

        self.header = QFrame()
        self.header.setFixedHeight(60)
        self.header.setStyleSheet("background-color: #b8ddac;")
        # Light - #b8ddac
        # Dark - #52995f

        self.logo_label = QLabel()
        pixmap = QPixmap("logo.png")
        self.logo_label.setPixmap(pixmap.scaledToHeight(40, Qt.TransformationMode.SmoothTransformation))
        self.logo_label.setContentsMargins(15, 0, 0, 0)
        self.logo_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        header_layout = QHBoxLayout()
        header_layout.addWidget(self.logo_label)
        header_layout.addStretch()
        self.header.setLayout(header_layout)

        self.content = QFrame()
        self.content_layout = QVBoxLayout()
        self.content_layout.setContentsMargins(20, 20, 20, 20)
        self.content_layout.setSpacing(15)
        self.content.setLayout(self.content_layout)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.header)
        main_layout.addWidget(self.content)