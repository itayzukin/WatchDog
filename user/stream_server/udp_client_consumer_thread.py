import socket
import threading
from global_vars import buffered_image, condition, addresses_list

FPS = 60
CHUNK_SIZE = 2048

class UDPClientConsumerThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self, daemon=False)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    def run(self):
        global buffered_image
        global condition
        
        while True:
            if len(addresses_list) != 0:
                condition.acquire()
                if not buffered_image:
                    condition.wait()
                self.send_screenshot()
                condition.release()

                print(buffered_image)
    
    def send_everyone(self, data):
        """ Sends data to all clients"""
        for address in addresses_list:
            self.server_socket.sendto(data, address)

    def send_screenshot(self):
        image_data = buffered_image

        self.send_everyone(b'SOF')   
        while image_data:
            chunk = image_data[:CHUNK_SIZE]  # Take first CHUNK_SIZE bytes
            self.send_everyone(chunk)  # Send the chunk
            image_data = image_data[CHUNK_SIZE:]  # Remove sent chunk
        self.send_everyone(b'EOF')  
        print("FILE SENT")