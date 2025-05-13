import socket
import threading
import hashlib
import configparser
from addresses import addresses

TCP_PORT = 2121
TCP_IP = '192.168.1.112'
RECV = 1024

class AuthAdminServerThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((TCP_IP, TCP_PORT))
        self.server_socket.listen(1)

    def run(self):
        print(f"Starting server on port: {TCP_PORT}")
        while True:
            client_socket, address = self.server_socket.accept()

            data = client_socket.recv(RECV).decode()
            args = data.split()

            match args[0]:
                case "CONNECTION":
                    if self.check_password(args[1]):
                        addresses[address] = True
                        client_socket.send('ACCEPTED')
                        client_socket.close()
                        break
                    else:
                        if address in addresses:
                            if addresses[address] == False:
                                client_socket.send('BLOCKED')
                                client_socket.close()
                                break
                            elif addresses[address] == 3:
                                addresses[address] = False
                            else:
                                addresses[address] = addresses[address] + 1
                        else:
                            addresses[address] = 1
                        client_socket.send('INCORRECT')
                        client_socket.close()
                    break
                case _:
                    break

    def check_password(self, password):
        encrypted_recv = hashlib.md5(password.encode()).hexdigest()
        encrypted_password = self.config.get('Account','password')

        if encrypted_password == encrypted_recv:
            return True
        return False
