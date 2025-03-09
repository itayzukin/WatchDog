import socket
from mss import mss
from time import sleep
import threading

FPS = 24
RECV_SIZE = 2096


class ShareScreenClient:

    def __init__(self, target_IP, target_port):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.address = (target_IP, target_port)
    
    def send_screenshot(self):
        """ Take a screenshot and send it """

        with mss() as sct:
            image_file_name = sct.shot(output = 'monitor.png')

        image_file = open(image_file_name, 'rb')
        file_part = image_file.read(RECV_SIZE)
        while file_part:
            self.server_socket.sendto(file_part, self.address)
            file_part = image_file.read(RECV_SIZE)
        self.server_socket.sendto(b'EOF', self.address)    
        print("END")


class ShareScreenClientThread(threading.Thread):

    def __init__(self, target_IP, target_port):
        threading.Thread.__init__(self, daemon=False)
        self.server = ShareScreenClient(target_IP, target_port)

    def run(self):
        while True:
            sleep(1.0 / FPS)
            self.server.send_screenshot()


# TEMP MAIN METHOD - DO NOT RUN INDEPENDENT ON THE FUTURE
thread = ShareScreenClientThread("127.0.0.1",15500)
thread.start()