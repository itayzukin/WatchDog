from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QHBoxLayout,
    QPushButton,
)
from PyQt6.QtGui import QPixmap, QImage
from windows.base_window import BaseWindow
import admin.stream_client.global_vars as gv
from admin.stream_client.signel_emitter import SignalEmitter

FPS = 60


class AdminPanelPage(BaseWindow):
    """
    Admin panel page UI showing control buttons and a live image feed.

    This class displays buttons for toggling audio and takeover,
    and shows a live feed image updated at a fixed FPS.
    """

    def __init__(self, parent_window):
        super().__init__()
        self.parent_window = parent_window

        main_layout = QVBoxLayout()

        # QLabel for displaying the live feed
        self.image_widget = QLabel()
        self.image_widget.setPixmap(QPixmap())
        self.image_widget.setScaledContents(False)
        self.image_widget.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.image_widget)

        btn_back = QPushButton("Return to connetion panel")
        btn_back.clicked.connect(self.return_admin_default)

        self.label = QLabel("Waiting for key input...")
        self.label.setStyleSheet("font-size: 24px;")
        main_layout.addWidget(self.label)

        self.signal_emitter = SignalEmitter()
        self.signal_emitter.new_text.connect(self.update_label)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.content_layout.addWidget(widget)

        # Set up a timer to refresh the QLabel every 1000/FPS milliseconds
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_image)
        self.timer.start(1000 // FPS)

        self.show()
    
    def return_admin_default(self):
        self.parent_window.go_to_admin_default()

    def update_image(self):
        """
        Update the QLabel with the latest image from the global buffer.

        Checks if new image data is available in the global buffer and
        updates the displayed pixmap while maintaining aspect ratio.
        """
        if gv.buffered_image:  # If new image data is available
            image = QImage.fromData(gv.buffered_image)
            if not image.isNull():  # Ensure image is valid before updating
                pixmap = QPixmap.fromImage(image)
                scaled_pixmap = pixmap.scaled(
                    self.image_widget.size(), 
                    Qt.AspectRatioMode.KeepAspectRatio, 
                    Qt.TransformationMode.SmoothTransformation
                )
                self.image_widget.setPixmap(scaled_pixmap)
        elif gv.buffered_image == None:
            self.image_widget.setText("Stream is Offline")

    def update_label(self, text):
        self.label.setText(f"Last key: {text}")
