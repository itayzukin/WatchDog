from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (
    QMainWindow, 
    QWidget, 
    QVBoxLayout,
    QLabel,
    QApplication
)
from PyQt6.QtGui import QPixmap


class AdminWindow(QMainWindow):
    def __init__(self, window_name):
        super().__init__()
        self.setWindowTitle(window_name)
        #self.setFixedSize(QSize(400, 150))

        main_layout = QVBoxLayout()

        main_layout.addWidget(QLabel('Live Screen Share'))

        image_widget = QLabel()
        
        
        image_widget.setPixmap(QPixmap())

        main_layout.addWidget(image_widget)


        widget = QWidget()
        widget.setLayout(main_layout)

        self.setCentralWidget(widget)
        self.show()

if __name__ == '__main__':
    app = QApplication([])
    window = AdminWindow('WatchDog')
    app.exec()