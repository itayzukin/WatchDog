import pyaudio
import socket
import threading

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

class AudioUDPStreamTransmit(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address = ('192.168.1.112', 14400)
        self.server_socket.bind(self.server_address)
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=FORMAT, channels=CHANNELS, 
                                  rate=RATE, input=True, frames_per_buffer=CHUNK)

    def run(self):
        print("Receiving audio...")

        try:
            while True:
                data, _addr = self.sock.recvfrom(CHUNK * 2)
                self.stream.write(data)
        except:
            print("Reception stopped.")

    def join(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
        self.server_socket.close()