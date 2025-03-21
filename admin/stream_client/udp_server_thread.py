import socket
import threading
import hashlib
import global_vars as gv

UDP_IP = '127.0.0.1'
UDP_PORT = 15500
CHUNK_SIZE = 8192

class UDPServerThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind((UDP_IP, UDP_PORT))
    
    def run(self):
        print("Starting server on port: {UDP_PORT}")

        while True:
            data, _ = self.server_socket.recvfrom(CHUNK_SIZE)

            if data.startswith(b'CHECKSUM:'):
                expected_checksum = data.split(b':')[1].decode()
                print("Received checksum:", expected_checksum)
                self.recv_screenshot(expected_checksum)
    
    def recv_screenshot(self, expected_checksum):
        """ Receive image data over UDP """
        received_data = b""

        while True:
            data, _ = self.server_socket.recvfrom(CHUNK_SIZE)

            if data == b'SOF':
                received_data = b""
                continue
            elif data == b'EOF':
                break
            
            received_data += data

        actual_checksum = hashlib.md5(received_data).hexdigest()
        if actual_checksum == expected_checksum:
            gv.buffered_image = received_data
            print("Image received successfully!")
        else:
            print("Checksum mismatch! Image may be corrupted.")