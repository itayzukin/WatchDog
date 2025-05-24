import pyaudio
import socket
import threading
import admin.stream_client.global_vars as gv

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

SERVER_IP = gv.server_ip
SERVER_PORT = 16600

class AudioUDPStreamTransmit(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address = (SERVER_IP, SERVER_PORT)
        self.server_socket.bind(self.server_address)
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=FORMAT, channels=CHANNELS, 
                                  rate=RATE, input=True, frames_per_buffer=CHUNK)

    def run(self):
        print("Receiving audio...")

        try:
            while True:
                data, _addr = self.server_socket.recvfrom(CHUNK * 2)
                self.stream.write(data)
        except:
            print("Reception stopped.")

    def join(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
        self.server_socket.close()