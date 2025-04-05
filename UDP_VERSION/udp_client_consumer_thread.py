import socket
import threading
import hashlib
import global_vars as gv

#CHUNK_SIZE = 8192
CHUNK_SIZE = 32000

class UDPClientConsumerThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    def run(self):
        while True:
            with gv.condition:
                while not gv.buffered_image:
                    gv.condition.wait()
                image_data = gv.buffered_image
            self.send_screenshot(image_data)

    def send_everyone(self, data):
        """ Sends data to all clients"""
        for address in gv.addresses_list:
            self.server_socket.sendto(data, address)

    def send_screenshot(self, image_data):
        """ Sends compressed image with checksum to clients """
        checksum = hashlib.md5(image_data).hexdigest().encode()
        self.send_everyone(b'CHECKSUM:' + checksum)

        chunk_index = 0
        self.send_everyone(b'SOF')
        while image_data:
            chunk = f"{chunk_index:04d}".encode() + image_data[:CHUNK_SIZE - 4]
            self.send_everyone(chunk)
            image_data = image_data[CHUNK_SIZE - 4:]
            chunk_index += 1
        self.send_everyone(b'EOF')

        print("Image sent with checksum:", checksum.decode())