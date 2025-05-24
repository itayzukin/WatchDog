import socket
import threading
import hashlib
import configparser

BUFFER_SIZE = 1024

class AuthClientThread(threading.Thread):

    def __init__(self, server_ip, server_port, password):
        threading.Thread.__init__(self)
        self.server_ip = server_ip
        self.server_port = server_port
        self.password = password
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._return = None

    def run(self):
        try:
            self.client_socket.connect((self.server_ip, int(self.server_port)))

            self.client_socket.send(f"CONNECTION {self.password}".encode())

            self._return = self.client_socket.recv(BUFFER_SIZE).decode()
        except TypeError as r:
            self._return = "INPUT_ERR"

    def join(self):
        threading.Thread.join(self)
        return self._return