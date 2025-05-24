# input_producer.py
import socket
import threading
from pynput import mouse, keyboard
import admin.stream_client.global_vars as gv

SERVER_IP = gv.server_ip
SERVER_PORT = 14400

class InputListenerProducerThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((SERVER_IP, SERVER_PORT))

    def run(self):
        mouse_listener = mouse.Listener(on_move=self.on_move, on_click=self.on_click)
        keyboard_listener = keyboard.Listener(on_press=self.on_press)
        
        mouse_listener.start()
        keyboard_listener.start()
        
        mouse_listener.join()
        keyboard_listener.join()

    def send(self, message: str):
        self.client_socket.sendall(message.encode())

    def on_move(self, x, y):
        self.send(f"MOUSE MOVE {x} {y}")

    def on_click(self, x, y, button, pressed):
        if pressed:
            if button.name == 'left':
                self.send("MOUSE LEFT_CLICK")
            elif button.name == 'right':
                self.send("MOUSE RIGHT_CLICK")

    def on_press(self, key):
        try:
            self.send(f"KEYBOARD {key.char}")
        except AttributeError:
            self.send(f"KEYBOARD {key.name}")
