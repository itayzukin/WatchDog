import threading
import global_vars as gv

SOF_FLAG = b'SOF'
EOF_FLAG = b'EOF'

class ImageHandlerConsumerThread(threading.Thread):
    def __init__ (self):
        threading.Thread.__init__ (self)

    def run (self):
        image = b''

        while True:
            with gv.condition:
                if gv.queue.empty():
                    gv.condition.wait()
                
                data = gv.queue.get()
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