import socket
import threading
import user.stream_server.global_vars as gv
from user.addresses import addresses

TCP_PORT = 14400
TCP_IP = '192.168.1.112'
BUFFER_SIZE = 1024

class InputRevieverServerProducerThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((TCP_IP, TCP_PORT))
        self.server_socket.listen(1)

    def run(self):
        print(f"Starting server on port: {TCP_PORT}")
        while True:
            client_socket, _address = self.server_socket.accept()
            if _address in addresses:
                while True:
                    data = client_socket.recv(BUFFER_SIZE)
                    gv.input_queue.append(data.decode())
                    with gv.condition:
                        gv.condition.notify()
            client_socket.close()
