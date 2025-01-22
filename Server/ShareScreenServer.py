import socket

LOCAL_IP = '127.0.0.1'
PORT = 15500
LISTEN = 1


class ShareScreenServer:

    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((LOCAL_IP, PORT))
        self.server_socket.listen(LISTEN)
    
    def accept_client(self):
        client_socket, address = self.server_socket.accept()
        print("Connection established with:", address)