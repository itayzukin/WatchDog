import socket
import threading
import admin.stream_client.global_vars as gv
from pynput import mouse, keyboard

SERVER_PORT = 16600

class InputListenerThread(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):
        self.sock.connect((gv.server_ip, SERVER_PORT))
        print("Connected to server")

        def send(msg: str):
            try:
                self.sock.sendall((msg + '\n').encode())
            except Exception as e:
                print("[Client] Send error:", e)

        def on_move(x, y):
            send(f"MOUSE {x} {y}")

        def on_click(x, y, button, pressed):
            btn = button.name.upper()
            state = 'down' if pressed else 'up'
            send(f"CLICK {x} {y} {btn} {state}")

        def on_scroll(x, y, dx, dy):
            send(f"SCROLL {dx} {dy}")

        def on_press(key):
            try:
                send(f"KEYBOARD {key.char} down")
            except AttributeError:
                send(f"KEYBOARD {str(key).replace('Key.', '').upper()} down")

        def on_release(key):
            try:
                send(f"KEYBOARD {key.char} up")
            except AttributeError:
                send(f"KEYBOARD {str(key).replace('Key.', '').upper()} up")

        with mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll), \
             keyboard.Listener(on_press=on_press, on_release=on_release):
            print("[Client] Listening to local input events...")
            keyboard.Listener.join()
