import threading
import admin.stream_client.global_vars as gv

SOF_FLAG = b'SOF'
EOF_FLAG = b'EOF'


class ImageHandlerConsumerThread(threading.Thread):
    """
    Consumer thread that assembles image data from chunks in a shared queue.
    It waits for SOF/EOF byte flags to reconstruct a complete image.
    """

    def __init__(self):
        super().__init__(daemon=True)

    def run(self):
        """
        Continuously monitors the shared queue for new data chunks, processes
        and reconstructs complete images, and updates the global image buffer.
        """
        image = b''

        while True:
            with gv.condition:
                if len(gv.queue) == 0:
                    gv.condition.wait()

                data = gv.queue.pop(0)
                splitted = data.split(SOF_FLAG)

                if SOF_FLAG in data:
                    if EOF_FLAG in splitted[0]:
                        image += splitted[0].split(EOF_FLAG)[0]
                        gv.buffered_image = image

                    image = splitted[-1]

                elif EOF_FLAG in splitted[-1]:
                    image += splitted[0].split(EOF_FLAG)[0]
                    gv.buffered_image = image
                    image = b''

                else:
                    image += data
