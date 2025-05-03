import socket
import threading
import admin.stream_client.global_vars as gv

SERVER_IP = '192.168.1.112'
SERVER_PORT = 15500
BUFFER_SIZE = 8192

class TCPClientProducerThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((SERVER_IP, SERVER_PORT))

    def run(self):
        print(f"Connected to TCP server on port: {SERVER_PORT}")

        while True:
            data = self.client_socket.recv(BUFFER_SIZE)
            with gv.condition:
                gv.queue.put(data)
                gv.condition.notify()