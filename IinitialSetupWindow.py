from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (
    QMainWindow, 
    QWidget, 
    QVBoxLayout, 
    QHBoxLayout,
    QLabel,
    QPushButton
)

class IinitialSetupWindow(QMainWindow):
    def __init__(self, window_name):
        super().__init__()
        self.setWindowTitle(window_name)
        self.setFixedSize(QSize(400, 150))

        maint_layout = QVBoxLayout()
        button_layout = QHBoxLayout()

        maint_layout.addWidget() # add color
        maint_layout.addWidget(QLabel('Welcome!'))
        maint_layout.addWidget(QLabel('Are you setting this computer as an admin or a user?'))

        button_layout.addWidget(QPushButton('Admin'))
        button_layout.addWidget(QPushButton('User'))

        maint_layout.addLayout(button_layout)

        widget = QWidget()
        widget.setLayout(maint_layout)

        self.setCentralWidget(widget)
        self.show()