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
    def __init__(self, windowName):
        super().__init__()
        self.setWindowTitle(windowName)
        #self.setFixedSize(QSize(400, 150))

        mainLayout = QVBoxLayout()
        buttonLayout = QHBoxLayout()

        mainLayout.addWidget(QLabel('Welcome!'))
        mainLayout.addWidget(QLabel('Are you setting this computer as an admin or a user?'))

        buttonLayout.addWidget(QPushButton('Admin'))
        buttonLayout.addWidget(QPushButton('User'))

        mainLayout.addLayout(buttonLayout)

        widget = QWidget()
        widget.setLayout(mainLayout)

        self.setCentralWidget(widget)
        self.show()