import pyaudio
import socket
import threading
import user.stream_server.global_vars as gv

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

SERVER_PORT = 16600


class AudioUDPStreamTransmit(threading.Thread):
    """
    Thread that captures audio from the microphone and streams it via UDP
    to a specified server address.
    """

    def __init__(self):
        super().__init__(daemon=True)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.p = None
        self.stream = None

    def run(self):
        """
        Open the audio stream and continuously read audio chunks,
        sending each chunk via UDP to the server.
        """
        self.server_address = (gv.admin_ip, SERVER_PORT)
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            frames_per_buffer=CHUNK,
        )

        print("Streaming audio...")

        try:
            while True:
                data = self.stream.read(CHUNK)
                self.server_socket.sendto(data, self.server_address)
        except Exception:
            print("Streaming stopped.")

    def join(self):
        if self.stream is not None:
            self.stream.stop_stream()
            self.stream.close()
        if self.p is not None:
            self.p.terminate()
        self.server_socket.close()
        super().join()
