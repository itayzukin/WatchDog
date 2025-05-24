import threading
import queue

# Contains the most recently received image
buffered_image = None

# Queue for producer-consumer communication
frame_queue = queue.Queue()

# Condition variable for synchronizing producer and consumer
condition = threading.Condition()

# Server credentials (to be set externally)
server_ip = None
server_port = None
