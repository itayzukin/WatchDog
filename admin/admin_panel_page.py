from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import ( 
    QWidget, 
    QVBoxLayout,
    QLabel,
    QHBoxLayout,
    QPushButton
)
from PyQt6.QtGui import QPixmap, QImage
from windows.base_window import BaseWindow
from admin.stream_client.input_listener_thread import InputListenerThread
from admin.stream_client.audio_udp_stream_receiver import AudioUDPStreamTransmit
import admin.stream_client.global_vars as gv

FPS = 60

class AdminPanelPage(BaseWindow):
    def __init__(self, parent_window):
        super().__init__()
        self.parent_window = parent_window

        self.input_listener_toggle = False
        self.audio_strean_toggle = False

        main_layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.audio_button = QPushButton('Toggle Audio')
        self.audio_button.clicked.connect(self.toggle_audio)
        self.takeover_button = QPushButton('Takeover')
        self.takeover_button.clicked.connect(self.takeover)
        button_layout.addWidget(self.audio_button)
        button_layout.addWidget(self.takeover_button)
        main_layout.addLayout(button_layout)

        # QLabel for dislaying the live feed
        self.image_widget = QLabel()
        self.image_widget.setPixmap(QPixmap())
        self.image_widget.setScaledContents(False)
        self.image_widget.setAlignment(Qt.AlignmentFlag.AlignCenter)
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
                    Qt.AspectRatioMode.KeepAspectRatio, 
                    Qt.TransformationMode.SmoothTransformation
                )
                self.image_widget.setPixmap(scaled_pixmap)
    
    def takeover(self):
        if not self.input_listener_toggle:
            self.input_listener = InputListenerThread()
            self.input_listener.start()
            self.input_listener_toggle = True
        else:
            self.input_listener.join()
            self.input_listener_toggle = False


    def toggle_audio(self):
        if not self.audio_strean_toggle:
            self.audio_stream = AudioUDPStreamTransmit()
            self.audio_stream.start()
            self.audio_strean_toggle = True
        else:
            self.audio_stream.join()
            self.audio_strean_toggle = False