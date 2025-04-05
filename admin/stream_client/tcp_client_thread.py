import socket
import threading
import global_vars as gv

SOF_FLAG = b'SOF'
EOF_FLAG = b'EOF'
BUFFER_SIZE = 8192
SERVER_IP = '192.168.1.112'
SERVER_PORT = 15500

class TCPClientThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((SERVER_IP, SERVER_PORT))

    def run(self):
        print(f"Connected to TCP server on port: {SERVER_PORT}")
        image = b''

        while True:
            data = self.client_socket.recv(BUFFER_SIZE)
            print(data)

            if SOF_FLAG in data:
                splitted = data.split(SOF_FLAG)
                
                if EOF_FLAG in splitted[0]:
                    image += splitted[0].split(EOF_FLAG)[0]
                    gv.buffered_image = image

                image = splitted[-1]

            elif EOF_FLAG in splitted[-1]:
                image += splitted[0].split(EOF_FLAG)[0]
                gv.buffered_image = image
                image = b''

            else:
                image += data