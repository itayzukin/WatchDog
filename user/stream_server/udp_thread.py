import socket
from mss import mss
from time import sleep
import threading
from global_vars import buffered_image, addresses_list

FPS = 60
CHUNK_SIZE = 2048

class UDPThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self, daemon=False)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.current_image = buffered_image
    
    def run(self):
        while addresses_list:
            sleep(1.0 / FPS)
            if buffered_image != self.current_image:
                self.current_image = buffered_image
                self.server.send_screenshot()
    
    def send_everyone(self, data):
        for address in addresses_list:
            self.server_socket.sendto(data, address)

    def send_screenshot(self):
        image_data = self.current_image

        self.server_socket.send_everyone(b'SOF')   
        while image_data:
            chunk = image_data[:CHUNK_SIZE]  # Take first CHUNK_SIZE bytes
            self.server_socket.send_everyone(chunk)  # Send the chunk
            image_data = image_data[CHUNK_SIZE:]  # Remove sent chunk
        self.server_socket.send_everyone(b'EOF')  
        print("FILE SENT")