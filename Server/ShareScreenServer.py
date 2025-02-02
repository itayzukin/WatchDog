import socket
from mss import mss

UDP_LOCAL_IP = '127.0.0.1'
UDP_PORT = 15500


class ShareScreenServer:

    def __init__(self, target_IP, target_port):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind((UDP_LOCAL_IP, UDP_PORT))
        self.address = (target_IP, target_port)
    
    def StartLiveDesktopStream(self):
        pass
    
    def send_screenshot(self):
        """ Take a screenshot and send it """

        with mss() as sct:
            image_file_name = sct.shot()
        image_file = open(image_file_name, 'rb')

        self.server_socket.sendto(image_file.read(), self.address)
