import socket
import threading
import global_vars as gv

FPS = 60
CHUNK_SIZE = 4096

class UDPClientConsumerThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self, daemon=False)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    def run(self):
        while True:
            if len(gv.addresses_list) != 0:
                gv.condition.acquire()
                if not gv.buffered_image:
                    gv.condition.wait()
                self.send_screenshot()
                gv.condition.release()
    
    def send_everyone(self, data):
        """ Sends data to all clients"""
        for address in gv.addresses_list:
            self.server_socket.sendto(data, address)

    def send_screenshot(self):
        image_data = gv.buffered_image

        self.send_everyone(b'SOF')   
        while image_data:
            chunk = image_data[:CHUNK_SIZE]  # Take first CHUNK_SIZE bytes
            self.send_everyone(chunk)  # Send the chunk
            image_data = image_data[CHUNK_SIZE:]  # Remove sent chunk
        self.send_everyone(b'EOF')  
        print("FILE SENT")