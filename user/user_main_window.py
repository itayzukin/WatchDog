from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (
    QMainWindow, 
    QWidget, 
    QVBoxLayout, 
    QHBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QApplication
)

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.init_ui()

    def init_ui(self):
        # Label and password input
        label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        # Login button
        login_button = QPushButton("Login")
        login_button.clicked.connect(self.handle_login)

        # Horizontal layout for input and button
        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(self.password_input)
        h_layout.addWidget(login_button)

        # Set the layout to the window
        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        self.setLayout(v_layout)

    def handle_login(self):
        password = self.password_input.text()
        print("Password entered:", password)  # Placeholder for actual logic

if __name__ == "__main__":
    app = QApplication([])
    window = LoginWindow()
    window.show()
    app.exec()