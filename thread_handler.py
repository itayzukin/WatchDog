from user.auth_server_thread import AuthServerThread
from user.stream_server.screenshot_producer_thread import ScreenshotProducerThread
from user.stream_server.tcp_server_consumer_thread import TCPServerConsumerThread
from admin.stream_client.tcp_client_producer_thread import TCPClientProducerThread
from admin.stream_client.image_handler_consumer_thread import ImageHandlerConsumerThread
from user.stream_server.keyboard_thread import KeyboardServer
from admin.stream_client.keyboard_reviever_thread import ReceiverThread

def enable_user_threads():
    """Start all necessary threads for user mode."""
    auth_thread = AuthServerThread()
    tcp_server_thread = TCPServerConsumerThread()
    screenshot_thread = ScreenshotProducerThread()
    keyboard = KeyboardServer()
    
    auth_thread.start()
    tcp_server_thread.start()
    screenshot_thread.start()
    keyboard.start()

def enable_admin_threads():
    """Start all necessary threads for admin mode."""
    tcp_client_thread = TCPClientProducerThread()
    image_handler_thread = ImageHandlerConsumerThread()
    rec_keyboard = ReceiverThread()

    tcp_client_thread.start()
    image_handler_thread.start()
    rec_keyboard.start()
