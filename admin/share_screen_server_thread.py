import socket
from mss import mss
from time import sleep
import threading

UDP_LOCAL_IP = '127.0.0.1'
UDP_PORT = 15500
FPS = 24

class ShareScreenServer:

    def __init__(self, target_IP, target_port):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind((UDP_LOCAL_IP, UDP_PORT))
        self.address = (target_IP, target_port)
    
    def send_screenshot(self):
        """ Take a screenshot and send it """

        with mss() as sct:
            image_file_name = sct.shot()
        image_file = open(image_file_name, 'rb')

        self.server_socket.sendto(image_file.read(), self.address)


class ShareScreenServerThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self, daemon=False)
        self.server = ShareScreenServer()

    def run(self):
        while True:
            sleep(1.0 / FPS)
            self.server.send_screenshot()

    def join(self):
        threading.Thread.join(self)


# TEMP MAIN METHOD - DO NOT RUN INDEPENDENT ON THE FUTURE
def main():
    thread = ShareScreenServerThread(UDP_LOCAL_IP)
    thread.start()

if __name__ == '__main__':
    main()