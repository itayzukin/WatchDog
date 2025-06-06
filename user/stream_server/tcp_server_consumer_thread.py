import socket
import threading
import user.stream_server.global_vars as gv

SOF_FLAG = b'SOF'
EOF_FLAG = b'EOF'
TCP_PORT = 15500
TCP_IP = "0.0.0.0"


class TCPServerConsumerThread(threading.Thread):
    """
    TCP server thread that accepts client connections and
    sends buffered image data framed by SOF and EOF flags.
    """

    def __init__(self):
        super().__init__(daemon=True)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((TCP_IP, TCP_PORT))
        self.server_socket.listen(5)

    def run(self):
        """
        Accept clients and continuously send them the buffered image data
        when available.
        """
        print(f"Starting server on port: {TCP_PORT}")
        accept_thread = threading.Thread(target = accept_clients, args=(self.server_socket,))
        accept_thread.start()

        while True:
            while gv.client_socket_list:
                with gv.condition:
                    while not gv.buffered_image:
                        gv.condition.wait()
                    image_data = gv.buffered_image
                self.send_clients(SOF_FLAG + image_data + EOF_FLAG)

    def send_clients(self, data):
        """
        Send data to all connected clients, removing any clients that fail.
        """
        for sock in gv.client_socket_list:
            try:
                sock.sendall(data)
            except Exception:
                gv.client_socket_list.remove(sock)

def accept_clients(server_socket):
        while True:
            client_socket, _address = server_socket.accept()
            gv.client_socket_list.append(client_socket)
            print("Client connected")
