import threading

# Contains prepared image to send to client
buffered_image = None

# Producer & Consumer condition
condition = threading.Condition()

# all the sockets of clients receiving images
client_socket_list = []