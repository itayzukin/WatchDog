import os
from PyQt6.QtCore import QSize, Qt, QTimer
from PyQt6.QtWidgets import (
    QMainWindow, 
    QWidget, 
    QVBoxLayout,
    QLabel,
    QApplication,
    QSizePolicy
)
from PyQt6.QtGui import QPixmap
from share_screen_server_thread import ShareScreenServerThread
import math

FPS = 24

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

        server_thread = ShareScreenServerThread()
        server_thread.start()
        
        # Set up a timer to refresh the QLabel every 100ms (check this code later)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_image)
        self.timer.start(math.floor(1/FPS))
        
        self.show()

    def update_image(self):
        """ Load the latest received image and update QLabel (check this function later) """
        if os.path.exists("curr-image.png"):
            pixmap = QPixmap("curr-image.png")
            if not pixmap.isNull():  # Ensure image is valid before updating
                self.image_widget.setPixmap(QPixmap("curr-image.png"))

if __name__ == '__main__':
    app = QApplication([])
    window = AdminWindow('WatchDog')
    app.exec()