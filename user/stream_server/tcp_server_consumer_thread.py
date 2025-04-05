import socket
import threading
import global_vars as gv

CHUNK_SIZE = 8192
TCP_PORT = 15500
TCP_IP = '127.0.0.1'

class TCPServerConsumerThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((TCP_IP, TCP_PORT))
        self.server_socket.listen(1)

    def run(self):
        print(f"Starting server on port: {TCP_PORT}")
        client_socket, address = self.server_socket.accept()
        gv.client_socket_list.append(client_socket)

        while True:
            with gv.condition:
                while not gv.buffered_image:
                    gv.condition.wait()
                image_data = gv.buffered_image
            self.send_screenshot(image_data)

    def send_everyone(self, data):
        """ Sends data to all clients"""
        for client_socket in gv.client_socket_list:
            try:
                client_socket.sendall(data)
            except:
                gv.client_socket_list.remove(client_socket)

    def send_screenshot(self, image_data):
        """ Sends compressed image with checksum to clients """
        self.send_everyone(b'SOF')
        while image_data:
            chunk = image_data[:CHUNK_SIZE]
            self.send_everyone(chunk)
            image_data = image_data[CHUNK_SIZE:]
        self.send_everyone(b'EOF')

        print("Image sent to clients")