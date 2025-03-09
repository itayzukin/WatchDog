from time import sleep
from mss import mss
from PIL import Image
from global_vars import buffered_image
import threading
import io

class ScreenshotThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self, daemon=False)

    def run(self):
        global buffered_image

        while True:
            sleep(1/24)
            buffered_image = self.capture_and_compress()

    def capture_and_compress(self):
        """ Capture monitor, compress and save to variable"""

        with mss() as sct:
            screenshot = sct.grab(sct.monitors[1])  # Capture first monitor

            # Convert raw screenshot data to a PIL Image
            img = Image.frombytes("RGB", screenshot.size, screenshot.rgb)

            # Store compressed image in memory using BytesIO
            img_buffer = io.BytesIO()
            img.save(img_buffer, format="JPEG", quality=20, optimize=True)

            compressed_img_bytes = img_buffer.getvalue()  # Get the compressed image as bytes

            return compressed_img_bytes