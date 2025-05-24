import socket
import threading
import pyautogui

SERVER_PORT = 16600

class InputServerThread(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):
        self.server_socket.bind(('0.0.0.0', SERVER_PORT))
        self.server_socket.listen(5)
        print(f"Starting server on port {SERVER_PORT}")

        while True:
            client_socket, address = self.server_socket.accept()
            self.handle_client(client_socket)

    def handle_client(self, client_socket):
        buffer = ""
        while True:
            try:
                data = client_socket.recv(1024)
                if not data:
                    break
                buffer += data.decode()
                while '\n' in buffer:
                    line, buffer = buffer.split('\n', 1)
                    self.process_command(line.strip())
            except Exception as e:
                print("[Server] Connection error:", e)
                break
        client_socket.close()

    def process_command(self, command):
        parts = str(command).split()

        try:
            if parts[0] == "MOUSE":
                x, y = int(parts[1]), int(parts[2])
                pyautogui.moveTo(x, y)

            elif parts[0] == "CLICK":
                x, y = int(parts[1]), int(parts[2])
                button = parts[3].lower()
                state = parts[4]
                if state == 'down':
                    pyautogui.mouseDown(x, y, button=button)
                else:
                    pyautogui.mouseUp(x, y, button=button)

            elif parts[0] == "SCROLL":
                dx, dy = int(parts[1]), int(parts[2])
                pyautogui.scroll(dy)

            elif parts[0] == "KEYBOARD":
                key = parts[1]
                state = parts[2]
                if state == 'down':
                    pyautogui.keyDown(key)
                else:
                    pyautogui.keyUp(key)

        except Exception as e:
            print(f"Error processing command '{command}': {e}")
