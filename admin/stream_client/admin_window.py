import os
from PyQt6.QtCore import QSize, Qt, QTimer
from PyQt6.QtWidgets import (
    QMainWindow, 
    QWidget, 
    QVBoxLayout,
    QLabel,
    QApplication
)
from PyQt6.QtGui import QPixmap, QImage
from global_vars import buffered_image
import udp_thread
import math

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
        self.timer.start(math.floor(1/FPS))
        
        self.show()

    def update_image(self):
        """ Check for new image data and update QLabel """
        global buffered_image

        if buffered_image:  # If new image data is available
            try:
                image = QImage.fromData(buffered_image)
                if not image.isNull():  # Ensure image is valid before updating
                    self.image_widget.setPixmap(QPixmap.fromImage(image))
            except Exception as e:
                print(f"Error loading image: {e}")


if __name__ == '__main__':
    app = QApplication([])
    thread = udp_thread.UDPThread()
    thread.start()
    window = AdminWindow('WatchDog')
    app.exec()