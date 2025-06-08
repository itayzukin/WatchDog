import socket
import threading
import hashlib
import configparser
import user.stream_server.global_vars as gv

TCP_PORT = 2121
TCP_IP = "0.0.0.0"
RECV = 1024


class AuthServerThread(threading.Thread):
    """
    Threaded TCP server that handles authentication requests.
    """

    def __init__(self):
        super().__init__(daemon=True)
        self.config = configparser.ConfigParser()
        self.config.read("config.ini")
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((TCP_IP, TCP_PORT))
        self.server_socket.listen(1)
        self.addresses = {}

    def run(self):
        """
        Run the server loop, accept client connections,
        and handle authentication messages.
        """
        print(f"Starting server on port: {TCP_PORT}")
        while True:
            client_socket, address = self.server_socket.accept()
            print("Client connected:", address)
            threading.Thread(target=self.handle_client, args=(client_socket, address), daemon=True).start()
        
            
    def handle_client(self, client_socket, address):
        data = client_socket.recv(RECV).decode()
        args = data.split()

        match args[0]:
            case "CONNECTION":
                if self.check_password(args[1]):
                    self.addresses[address] = True
                    client_socket.send("ACCEPTED".encode())
                    client_socket.close()
                    gv.admin_ip = address
                    print(address, "ACCEPTED")
                else:
                    if address in self.addresses:
                        if self.addresses[address] is False:
                            client_socket.send("BLOCKED".encode())
                            client_socket.close()
                        elif self.addresses[address] == 3:
                            self.addresses[address] = False
                        else:
                            self.addresses[address] += 1
                    else:
                        self.addresses[address] = 1
                    client_socket.send("INCORRECT".encode())
                    client_socket.close()
            case _:
                pass

    def check_password(self, password):
        """
        Check the received password against the stored hash.
        """
        encrypted_password = self.config.get("Account", "password")

        return encrypted_password == password
