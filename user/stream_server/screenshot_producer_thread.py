from mss import mss
from PIL import Image
import user.stream_server.global_vars as gv
import threading
import io


class ScreenshotProducerThread(threading.Thread):
    """
    Thread that continuously captures the screen,
    compresses the image, and updates the shared buffered image.
    """

    def __init__(self):
        super().__init__(daemon=True)

    def run(self):
        """
        Capture the screen repeatedly and notify consumers
        when a new compressed image is available.
        """
        while True:
            gv.buffered_image = self.save_image()
            with gv.condition:
                gv.condition.notify()

    def save_image(self):
        """
        Capture the primary monitor screen and compress it.
        """
        with mss() as sct:
            screenshot = sct.grab(sct.monitors[1])
            compressed_screenshot = self.compress_image(screenshot)
            compressed_screenshot_bytes = compressed_screenshot.getvalue()
            return compressed_screenshot_bytes

    def compress_image(self, image, quality=40):
        """
        Compress the given raw image using JPEG compression.
        """
        img = Image.frombytes("RGB", image.size, image.rgb)
        img_buffer = io.BytesIO()
        img.save(img_buffer, "JPEG", quality=quality, optimize=True)
        return img_buffer
