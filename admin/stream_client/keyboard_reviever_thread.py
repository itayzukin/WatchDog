import socket
import threading

class ReceiverThread(threading.Thread):
    def __init__(self, signal_emitter, server_ip, server_port):
        super().__init__(daemon=True)
        self.server_ip = server_ip
        self.server_port = server_port
        self.signal_emitter = signal_emitter

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            while True:
                data = s.recv(1024)
                if not data:
                    break
                self.signal_emitter.new_text.emit(data.decode())