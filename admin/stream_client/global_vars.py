import threading

# Contains the most recently received image
buffered_image = None

# Queue for producer-consumer communication
queue = []

# Condition variable for synchronizing producer and consumer
condition = threading.Condition()

# Server credentials (to be set externally)
server_ip = None
server_port = None
