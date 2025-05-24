from user.auth_server_thread import AuthServerThread
from user.stream_server.screenshot_producer_thread import ScreenshotProducerThread
from user.stream_server.tcp_server_consumer_thread import TCPServerConsumerThread
from user.stream_server.input_reciever_server_producer_thread import InputRevieverServerProducerThread
from admin.stream_client.tcp_client_producer_thread import TCPClientProducerThread
from admin.stream_client.image_handler_consumer_thread import ImageHandlerConsumerThread

def enable_user_threads():
    auth_server = AuthServerThread()
    thread1 = TCPServerConsumerThread()
    thread2 = ScreenshotProducerThread()
    thread3 = InputRevieverServerProducerThread()
    
    auth_server.start()
    thread1.start()
    thread2.start()
    thread3.start()

def enable_admin_threads():
    thread1 = TCPClientProducerThread()
    thread2 = ImageHandlerConsumerThread()

    thread1.start()
    thread2.start()