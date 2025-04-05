from screenshot_producer_thread import ScreenshotProducerThread
from tcp_server_consumer_thread import TCPServerConsumerThread

thread1 = ScreenshotProducerThread()
thread2 = TCPServerConsumerThread()

thread1.start()
thread2.start()

thread1.join()
thread2.join()