from mss import mss
from PIL import Image
import user.stream_server.global_vars as gv
import threading
import io

class ScreenshotProducerThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self, daemon=True)

    def run(self):
        while True:
            print('Shot taken')
            gv.buffered_image = self.save_image()
            with gv.condition:
                gv.condition.notify()

    def save_image(self):
        """ Capture monitor and compress to buffered_image"""
        with mss() as sct:
            screenshot = sct.grab(sct.monitors[1])
            compressed_screenshot = self.compress_image(screenshot)
            compressed_screenshot_bytes = compressed_screenshot.getvalue()
            return compressed_screenshot_bytes
        
    def compress_image(self, image, quality=40):
        """Compress given image"""
        img = Image.frombytes("RGB", image.size, image.rgb)
        img_buffer = io.BytesIO()
        img.save(img_buffer, "JPEG", quality=quality, optimize=True)
        return img_buffer