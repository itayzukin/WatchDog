import threading

"""
Global variables and synchronization primitives used for
image streaming and input handling between producer and consumer threads.
"""

# Contains prepared image to send to client
buffered_image = None

# Condition for stream images producer & consumer synchronization
condition = threading.Condition()

# Condition for producer & consumer synchronization - inputs
input_condition = threading.Condition()

# List of client sockets receiving images
client_socket_list = []

# Queue for inputs
input_queue = []

# Admin IP address (to be set)
admin_ip = ""
