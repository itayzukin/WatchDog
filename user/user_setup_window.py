from base_window import BaseWindow
from PyQt6.QtWidgets import QLineEdit, QPushButton, QLabel
from user.user_main_window import UserMainWindow

class UserSetupWindow(BaseWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("User Setup")

        self.info_label = QLabel("Create your password:")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.signup_button = QPushButton("Sign Up")
        self.signup_button.setMinimumHeight(40)
        self.signup_button.clicked.connect(self.go_to_user_main)

        self.content_layout.addWidget(self.info_label)
        self.content_layout.addWidget(self.password_input)
        self.content_layout.addWidget(self.signup_button)

    def go_to_user_main(self):
        self.user_main = UserMainWindow()
        self.user_main.show()
        self.close()