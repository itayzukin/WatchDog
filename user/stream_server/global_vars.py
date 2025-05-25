import threading

"""
Global variables and synchronization primitives used for
image streaming and input handling between producer and consumer threads.
"""

# Contains prepared image to send to client
buffered_image = None

# Condition for stream images producer & consumer synchronization
condition = threading.Condition()

# List of client sockets receiving images
client_socket_list = []
