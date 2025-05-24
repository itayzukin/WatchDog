import socket
import threading
import admin.stream_client.global_vars as gv

SERVER_PORT = 15500
BUFFER_SIZE = 8192


class TCPClientProducerThread(threading.Thread):
    """
    A producer thread that connects to a TCP server and continuously receives data.
    Received data is placed into a shared queue for consumption.
    """

    def __init__(self):
        super().__init__(daemon=True)
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):
        """
        Connects to the server and continuously reads data from the socket.
        Each received chunk is added to a shared queue and notifies the consumer.
        """
        self.client_socket.connect((gv.server_ip, SERVER_PORT))
        print(f"Connected to TCP server on port: {SERVER_PORT}")

        try:
            while True:
                data = self.client_socket.recv(BUFFER_SIZE)
                with gv.condition:
                    gv.queue.insert(-1,data)
                    gv.condition.notify()
        except:
            pass
