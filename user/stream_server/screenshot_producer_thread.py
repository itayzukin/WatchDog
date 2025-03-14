from time import sleep
from mss import mss
from PIL import Image
import global_vars as gv
import threading
import io

class ScreenshotProducerThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self, daemon=False)

    def run(self):

        while True:
            sleep(1/60)
            gv.condition.acquire()
            gv.buffered_image = self.capture_and_compress()
            gv.condition.notify()
            gv.condition.release()

    def capture_and_compress(self):
        """ Capture monitor and compress to buffered_image"""

        with mss() as sct:
            screenshot = sct.grab(sct.monitors[1])

            # Convert raw screenshot data to a PIL Image
            img = Image.frombytes("RGB", screenshot.size, screenshot.rgb)

            # Store compressed image in memory using BytesIO
            img_buffer = io.BytesIO()
            img.save(img_buffer, format="JPEG", quality=40, optimize=True)

            # Get the compressed image as bytes
            compressed_img_bytes = img_buffer.getvalue()
            print("SAVE IMAGE TO BUFFER")
            return compressed_img_bytes