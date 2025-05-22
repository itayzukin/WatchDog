import threading

# Contains prepared image to send to client
buffered_image = None

# Stream Images Producer & Consumer condition
condition = threading.Condition()

# Condition for producer & consumer - inputs
input_condition = threading.Condition()

# all the sockets of clients receiving images
client_socket_list = []

# queue for inputs
input_queue = []