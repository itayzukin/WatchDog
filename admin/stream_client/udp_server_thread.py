import socket
import threading
import global_vars as gv

FPS = 60
UDP_IP = '127.0.0.1'
UDP_PORT = 15500
CHUNK_SIZE = 4096

class UDPServerThread(threading.Thread):

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
        """ Receive image data over UDP """
        image_chunks = {}
        image_data = b''
        total_chunks = 0
        not_done = False

        while True:
            data, _ = self.server_socket.recvfrom(CHUNK_SIZE)

            if data == b'EOF':
                break
            
            try:
                chunk_index = int(data[:4].decode())
                chunk_data = data[4:]
                
                if chunk_index not in image_chunks:
                    image_chunks[chunk_index] = chunk_data
                    total_chunks = max(total_chunks, chunk_index)

            except ValueError:
                print("Invalid packet received, skipping...")
                continue

        for i in range(total_chunks + 1):
            if i in image_chunks:  
                image_data += image_chunks[i]
            else:
                image_data += b'\x00' * (CHUNK_SIZE - 4)
        
        gv.buffered_image = image_data