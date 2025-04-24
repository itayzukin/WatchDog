import os
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import (
    QMainWindow, 
    QWidget, 
    QVBoxLayout,
    QLabel,
    QApplication
)
from PyQt6.QtGui import QPixmap, QImage
import stream_client.global_vars as gv
from stream_client.tcp_client_producer_thread import TCPClientProducerThread
from stream_client.image_handler_consumer_thread import ImageHandlerConsumerThread

FPS = 60

class AdminWindow(QMainWindow):
    def __init__(self, window_name):
        super().__init__()
        self.setWindowTitle(window_name)
        #self.setFixedSize(QSize(400, 150))

        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('Live Screen Share'))

        # QLabel for dislaying the live feed
        self.image_widget = QLabel()
        self.image_widget.setPixmap(QPixmap())
        self.image_widget.setScaledContents(True)
        main_layout.addWidget(self.image_widget)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)
        
        # Set up a timer to refresh the QLabel every 100ms (check this code later)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_image)
        self.timer.start(1000 // FPS)

        self.thread1 = TCPClientProducerThread()
        self.thread2 = ImageHandlerConsumerThread()

        self.thread1.start()
        self.thread2.start()

        self.show()

    def update_image(self):
        """ Check for new image data and update QLabel """
        if gv.buffered_image:  # If new image data is available
            image = QImage.fromData(gv.buffered_image)
            if not image.isNull():  # Ensure image is valid before updating
                pixmap = QPixmap.fromImage(image)
                scaled_pixmap = pixmap.scaled(
                    self.image_widget.size(), 
                    Qt.AspectRatioMode.KeepAspectRatioByExpanding, 
                    Qt.TransformationMode.SmoothTransformation
                )
                self.image_widget.setPixmap(scaled_pixmap)


if __name__ == '__main__':
    app = QApplication([])
    window = AdminWindow('WatchDog')
    app.exec()