from windows.base_window import BaseWindow
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit
import hashlib
import configparser
import os
import sys
import psutil # to get local ip

class UserDefaultPage(BaseWindow):
    """
    User page allowing connection with password verification.
    """

    def __init__(self, parent_window):
        super().__init__()
        self.parent_window = parent_window
        self.config = configparser.ConfigParser()
        self.config.read("config.ini")

        label = QLabel("You're being monitored!")
        label.setStyleSheet("font-size: 18px;")
        label1 = QLabel(f"IP ADDRESS: {self.get_physical_ethernet_ip()}\nPORT: 2121")
        label1.setStyleSheet("font-size: 16px;")
        label2 = QLabel("Enter admin password and click \"Turn Off\" to stop the program")
        label2.setStyleSheet("font-size: 12px;")
        self.label3 = QLabel("")
        self.label3.setStyleSheet("font-size: 12px;")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        btn_login = QPushButton("Turn Off")
        btn_login.clicked.connect(self.check_password)

        self.content_layout.addWidget(label)
        self.content_layout.addWidget(label1)
        self.content_layout.addWidget(label2)
        self.content_layout.addWidget(self.password_input)
        self.content_layout.addWidget(btn_login)
        self.content_layout.addWidget(self.label3)

    def check_password(self):
        """
        Check the entered password against the stored hash and
        navigate to the admin panel if it matches.
        """
        password = self.password_input.text()
        encrypted = hashlib.md5(password.encode()).hexdigest()

        try:
            if encrypted == self.config.get("Account", "password"):
                os.remove("config.ini")
                sys.exit()
            else:
                self.label3.setText("Password is incorrect")
        except Exception:
            self.label3.setText("Password is incorrect")

    def get_physical_ethernet_ip(self):
        """ Returns the ip of this computer"""
        for iface_name, addrs in psutil.net_if_addrs().items():
            name_lower = iface_name.lower()
            if "ethernet" in name_lower and not name_lower.startswith("vethernet"):
                for addr in addrs:
                    if addr.family.name == "AF_INET":
                        return addr.address
        return None
