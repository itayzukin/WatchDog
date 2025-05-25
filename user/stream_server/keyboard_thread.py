import socket
import threading
from pynput import keyboard

SERVER_IP = '0.0.0.0'
SERVER_PORT = 17700

class KeyboardServer(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.clients = []
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):
        self.server_socket.bind((SERVER_IP, SERVER_PORT))
        self.server_socket.listen(5)
        print(f"Server listening on port {SERVER_PORT}")

        threading.Thread(target=self.listen_to_keyboard, daemon=True).start()

        while True:
            client_socket, address = self.server_socket.accept()
            print(f"Client connected: {address}")
            self.clients.append(client_socket)

    def send_all(self, message):
        for socket in self.clients[]:
            try:
                socket.sendall(message.encode())
            except:
                self.clients.remove(socket)

    def listen_to_keyboard(self):
        def on_press(key):
            try:
                self.send_all(key.char)
            except AttributeError:
                self.send_all(f"[{key.name}]")
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()