import socket
import os
import threading

UDP_LOCAL_IP = '127.0.0.1'
UDP_PORT = 15500
RECV = 1024

class ShareScreenServer:

    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind((UDP_LOCAL_IP, UDP_PORT))
        
    
    def recv_images(self):
        try:
            os.remove('rec-image.png')
        finally:
            file = open('rec-image.png', 'wb')
            data, server = self.server_socket.recvfrom(RECV)
            
            while data != b'':
                print(data)
                file.write(data)
                data, server = self.server_socket.recvfrom(RECV)

            file.close()
            print("REC")


class ShareScreenServerThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self, daemon=False)
        self.server = ShareScreenServer()

    def run(self):
        while True:
            self.server.recv_images()

    def join(self):
        threading.Thread.join(self)

