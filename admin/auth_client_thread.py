import socket
import threading
import hashlib
import configparser

TCP_PORT = 2121
TCP_IP = '127.0.0.1'
RECV = 1024

class AuthClientThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((TCP_IP, TCP_PORT))

    def run(self):
        print(f"Starting server on port: {TCP_PORT}")