from user.auth_server_thread import AuthServerThread
from user.stream_server.screenshot_producer_thread import ScreenshotProducerThread
from user.stream_server.tcp_server_consumer_thread import TCPServerConsumerThread
from user.stream_server.input_reciever_server_producer_thread import InputRevieverServerProducerThread
from admin.stream_client.tcp_client_producer_thread import TCPClientProducerThread
from admin.stream_client.image_handler_consumer_thread import ImageHandlerConsumerThread

def enable_user_threads():
    """Start all necessary threads for user mode."""
    auth_thread = AuthServerThread()
    tcp_server_thread = TCPServerConsumerThread()
    screenshot_thread = ScreenshotProducerThread()
    input_receiver_thread = InputRevieverServerProducerThread()
    
    auth_thread.start()
    tcp_server_thread.start()
    screenshot_thread.start()
    input_receiver_thread.start()

    # Optionally return threads if you want to manage them later
    return auth_thread, tcp_server_thread, screenshot_thread, input_receiver_thread

def enable_admin_threads():
    """Start all necessary threads for admin mode."""
    tcp_client_thread = TCPClientProducerThread()
    image_handler_thread = ImageHandlerConsumerThread()

    tcp_client_thread.start()
    image_handler_thread.start()

    return tcp_client_thread, image_handler_thread
