import socket
import threading
import admin.stream_client.global_vars as gv

SERVER_PORT = 17700

class ReceiverThread(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
            socket.connect((gv.server_ip, SERVER_PORT))
            while True:
                data = socket.recv(1024)
                if not data:
                    break
                gv.signal_emitter.new_text.emit(data.decode())