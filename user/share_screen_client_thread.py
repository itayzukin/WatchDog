import socket
import os
import threading

RECV = 1024

class ShareScreenClient:

    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    def recv_images(self):
        data, server = self.server_socket.recvfrom(RECV)
        try:
            os.remove('rec-image.png')
        finally:
            file = open('rec-image.png', 'wb')
            file.write(data)


class ShareScreenClientThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self, daemon=False)
        self.client = ShareScreenClient()

    def run(self):
        while True:
            self.client.recv_images()

    def join(self):
        threading.Thread.join(self)

