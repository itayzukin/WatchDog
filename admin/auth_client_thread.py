import socket
import threading
import hashlib
import configparser

BUFFER_SIZE = 1024


class AuthClientThread(threading.Thread):
    """
    Thread to handle authentication with a server by connecting,
    sending credentials, and receiving a response.
    """

    def __init__(self, server_ip, server_port, password):
        super().__init__()
        self.server_ip = server_ip
        self.server_port = server_port
        self.password = password
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._return = None

    def run(self):
        """
        Connect to the server, send authentication data, 
        and store the server response.
        """
        try:
            self.client_socket.connect((self.server_ip, int(self.server_port)))
            self.client_socket.send(f"CONNECTION {self.password}".encode())
            self._return = self.client_socket.recv(BUFFER_SIZE).decode()
        except TypeError:
            self._return = "INPUT_ERR"

    def join(self):
        super().join()
        return self._return
