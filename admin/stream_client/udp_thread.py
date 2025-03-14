import socket
import threading
import global_vars as gv

FPS = 60
UDP_IP = '127.0.0.1'
UDP_PORT = 15500
CHUNK_SIZE = 4096

class UDPThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self, daemon=False)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind((UDP_IP, UDP_PORT))
    
    def run(self):
        while True:
            data, _ = self.server_socket.recvfrom(CHUNK_SIZE)

            if data == b'SOF':
                self.receive_screenshot()

    def receive_screenshot(self):
        image_data = b''
        while True:
            data, _ = self.server_socket.recvfrom(CHUNK_SIZE)
            if data == b'EOF':
                break
            image_data += data

        gv.buffered_image = image_data