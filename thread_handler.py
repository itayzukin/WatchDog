from user.auth_server_thread import AuthServerThread
from admin.stream_client.tcp_client_producer_thread import TCPClientProducerThread
from admin.stream_client.image_handler_consumer_thread import ImageHandlerConsumerThread

def enable_user_threads():
    auth_server = AuthServerThread()
    
    auth_server.start()

def enable_admin_threads():
    thread1 = TCPClientProducerThread()
    thread2 = ImageHandlerConsumerThread()

    thread1.start()
    thread2.start()