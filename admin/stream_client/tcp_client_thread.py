import socket
import threading
import global_vars as gv

CHUNK_SIZE = 8192
SERVER_IP = '127.0.0.1'
SERVER_PORT = 15500

class TCPClientThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        

    def run(self):
        self.client_socket.connect((SERVER_IP, SERVER_PORT))

        while True:
            data = self.client_socket.recv(CHUNK_SIZE)
            print(data)

            if data == b'SOF':
                self.recv_screenshot()
                break
    
    def recv_screenshot(self):
        """ Receive image data over TCP """
        received_data = b""

        while True:
            data = self.client_socket.recv(CHUNK_SIZE)
            
            if data == b'EOF':
                print(data)
                break

            received_data += data

        gv.buffered_image = received_data
        print("Image received successfully!")