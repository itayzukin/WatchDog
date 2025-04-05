import socket
import threading
import global_vars as gv

CHUNK_SIZE = 8192
SERVER_IP = '127.0.0.1'
SERVER_PORT = 15500

class TCPClientThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((SERVER_IP, SERVER_PORT))

    def run(self):
        print(f"Connected to TCP server on port: {SERVER_PORT}")
        image = b''

        while True:
            while True:
                data = self.client_socket.recv(CHUNK_SIZE)
                if not data:
                    break

                image += data

            gv.buffered_image = image