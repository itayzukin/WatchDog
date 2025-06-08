import socket
import threading
import admin.stream_client.global_vars as gv

SERVER_PORT = 17700

class ReceiverThread(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):
        try:
            self.socket.connect((gv.server_ip, SERVER_PORT))
            while True:
                data = self.socket.recv(1024)
                if not data:
                    break
                gv.signal_emitter.new_text.emit(data.decode())
        except:
            print("Unable to connect to input server.")