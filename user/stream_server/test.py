from screenshot_producer_thread import ScreenshotProducerThread
from udp_client_consumer_thread import UDPClientConsumerThread

thread1 = ScreenshotProducerThread()
thread2 = UDPClientConsumerThread()

thread1.start()
thread2.start()