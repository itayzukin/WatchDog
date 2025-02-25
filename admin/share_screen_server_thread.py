import socket
import os
import threading

UDP_LOCAL_IP = '127.0.0.1'
UDP_PORT = 15500
RECV_SIZE = 4096


class ShareScreenServer:

    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind((UDP_LOCAL_IP, UDP_PORT))
        
    
    def recv_images(self):
        """ Open img and insert recieved data """
        file = open('queued-image.png', 'wb') 
        while True:
            data, _server = self.server_socket.recvfrom(4096) 
            if data == b'EOF':
                break
            file.write(data) 
        file.close()

        try:
            os.remove("curr-image.png")
        except OSError:
            pass
        os.rename("queued-image.png","curr-image.png")
        print("REC")


class ShareScreenServerThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self, daemon=False)
        self.server = ShareScreenServer()

    def run(self):
        while True:
            self.server.recv_images()


if __name__ == '__main__':
    thread = ShareScreenServerThread()
    thread.start()