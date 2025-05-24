import pyaudio
import socket
import threading

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

SERVER_IP = '192.168.1.112'
SERVER_PORT = 16600

class AudioUDPStreamTransmit(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address = None
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=FORMAT, channels=CHANNELS, 
                                  rate=RATE, input=True, frames_per_buffer=CHUNK)

    def run(self):
        print("Streaming audio...")

        try:
            while True:
                data = self.stream.read(CHUNK)
                self.server_socket.sendto(data, self.server_address)
        except:
            print("Streaming stopped.")

    def join(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
        self.server_socket.close()