import pyaudio
import socket
import threading
import admin.stream_client.global_vars as gv

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

SERVER_PORT = 16600


class AudioUDPStreamTransmit(threading.Thread):
    """
    Threaded class to receive audio data via UDP and play it through the microphone input.
    """

    def __init__(self):
        super().__init__(daemon=True)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.stream = None
        self.p = None

    def run(self):
        """
        Continuously receives and plays audio data from the UDP socket.
        """
        self.server_socket.bind(("0.0.0.0", SERVER_PORT))
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            frames_per_buffer=CHUNK
        )

        print("Receiving audio...")

        try:
            while True:
                data, _ = self.server_socket.recvfrom(CHUNK * 2)
                self.stream.write(data)
        except Exception as e:
            print(f"Reception stopped. Reason: {e}")

    def join(self):
        """
        Cleans up audio stream and socket resources on thread termination.
        """
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
        self.server_socket.close()
