import socket
import threading
import admin.stream_client.global_vars as gv

SERVER_PORT = 15500
BUFFER_SIZE = 8192

class TCPClientProducerThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):
        self.client_socket.connect((gv.server_ip, SERVER_PORT))
        print(f"Connected to TCP server on port: {SERVER_PORT}")

        try:
            while True:
                data = self.client_socket.recv(BUFFER_SIZE)
                with gv.condition:
                    gv.queue.put(data)
                    gv.condition.notify()
        except:
            pass
