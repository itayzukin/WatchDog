import socket

UDP_LOCAL_IP = '127.0.0.1'
UDP_PORT = 15500
RECV = 1024


class ShareScreenClient:

    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    def recv_images(self):

        while True:
            data = self.server_socket.recvfrom(RECV)