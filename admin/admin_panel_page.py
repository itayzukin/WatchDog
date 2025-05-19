from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import ( 
    QWidget, 
    QVBoxLayout,
    QLabel,
    QApplication
)
from PyQt6.QtGui import QPixmap, QImage
from windows.base_window import BaseWindow
import admin.stream_client.global_vars as gv

FPS = 60

class AdminPanelPage(BaseWindow):
    def __init__(self, parent_window):
        super().__init__()
        self.parent_window = parent_window

        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('Live Screen Share'))

        # QLabel for dislaying the live feed
        self.image_widget = QLabel()
        self.image_widget.setPixmap(QPixmap())
        self.image_widget.setScaledContents(True)
        main_layout.addWidget(self.image_widget)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.content_layout.addWidget(widget)
        
        # Set up a timer to refresh the QLabel every 100ms (check this code later)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_image)
        self.timer.start(1000 // FPS)

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