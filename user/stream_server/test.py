from udp_thread import UDPThread
from screenshot_thread import ScreenshotThread

thread1 = ScreenshotThread()
thread2 = UDPThread()

thread1.start()
thread2.start()