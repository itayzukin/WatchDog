import threading
import queue

# Contains the most recently received image
buffered_image = None

# Queue for producer-consumer communication
queue = queue.Queue()

# Condition variable for synchronizing producer and consumer
condition = threading.Condition()
