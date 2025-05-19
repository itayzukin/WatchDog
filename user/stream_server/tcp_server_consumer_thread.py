import socket
import threading
import user.stream_server.global_vars as gv

SOF_FLAG = b'SOF'
EOF_FLAG = b'EOF'
TCP_PORT = 15500
TCP_IP = '192.168.1.112'

class TCPServerConsumerThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((TCP_IP, TCP_PORT))
        self.server_socket.listen(5)

    def run(self):
        print(f"Starting server on port: {TCP_PORT}")
        client_socket, _address = self.server_socket.accept()
        gv.client_socket_list.append(client_socket)

        while True:
            with gv.condition:
                while not gv.buffered_image:
                    gv.condition.wait()
                image_data = gv.buffered_image
            self.send_clients(SOF_FLAG + image_data + EOF_FLAG)
            print("Image sent to client")

    def send_clients(self, data):
        """ Sends data to all clients"""
        for socket in gv.client_socket_list:
            try:
                socket.sendall(data)
            except:
                gv.client_socket_list.remove(socket)