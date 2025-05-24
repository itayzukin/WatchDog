import threading
import queue

# Contains received image
buffered_image = None

# Queue for producer & consumer
queue = queue.Queue()

# Consumer & Producer condition
condition = threading.Condition()

# server credentials
server_ip = None
server_port = None