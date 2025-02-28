import socket
import os
import threading

UDP_LOCAL_IP = '127.0.0.1'
UDP_PORT = 15500
RECV_SIZE = 2096


class ShareScreenServer:

    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind((UDP_LOCAL_IP, UDP_PORT))
        
    
    def recv_images(self):
        """ Receive image and save it """
        temp_file = "queued-image.png"
        final_file = "curr-image.png"

        file = open(temp_file, 'wb') 
        while True:
            data, server = self.server_socket.recvfrom(RECV_SIZE) 
            if data == b'EOF':
                server.send('ACK'.encode())
                break
            file.write(data) 
        file.close()

        try:
            os.remove(final_file)
        except Exception as e:
            print("EX", e)
            pass
        os.rename(temp_file, final_file)
        print("REC")


class ShareScreenServerThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self, daemon=False)
        self.server = ShareScreenServer()

    def run(self):
        #while True:
        self.server.recv_images()


if __name__ == '__main__':
    thread = ShareScreenServerThread()
    thread.start()