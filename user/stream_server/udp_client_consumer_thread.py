import socket
import threading
import hashlib
import global_vars as gv

CHUNK_SIZE = 4096

class UDPClientConsumerThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    def run(self):
        while True:
            if len(gv.addresses_list) != 0:
                with gv.condition:
                    if not gv.buffered_image:
                        gv.condition.wait()
                    self.send_screenshot()
                    gv.buffered_image = None

    def send_everyone(self, data):
        """ Sends data to all clients"""
        for address in gv.addresses_list:
            self.server_socket.sendto(data, address)

    def send_screenshot(self):
        """ Sends compressed image with checksum to clients """
        checksum = hashlib.md5(gv.buffered_image).hexdigest().encode()
        self.send_everyone(b'CHECKSUM:' + checksum)

        image_data = gv.buffered_image
        self.send_everyone(b'SOF')  # Start of File
        while image_data:
            chunk = image_data[:CHUNK_SIZE]
            self.send_everyone(chunk)
            image_data = image_data[CHUNK_SIZE:]
        self.send_everyone(b'EOF')  # End of File 
        print("Image sent with checksum:", checksum.decode())