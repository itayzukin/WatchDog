import socket

UDP_LOCAL_IP = '127.0.0.1'
UDP_PORT = 15500


class ShareScreenServer:

    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind((UDP_LOCAL_IP, UDP_PORT))
    
    def SendScreenshot():
        pass