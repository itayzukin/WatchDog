from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (
    QMainWindow, 
    QWidget, 
    QVBoxLayout,
    QLabel,
    QApplication
)
from PyQt6.QtGui import QPixmap
from mss import mss

class ClientWindow(QMainWindow):
    def __init__(self, windowName):
        super().__init__()
        self.setWindowTitle(windowName)
        #self.setFixedSize(QSize(400, 150))

        mainLayout = QVBoxLayout()

        mainLayout.addWidget(QLabel('Live Screen Share'))

        imageWidget = QLabel()
        with mss() as sct:
            imageWidget.setPixmap(QPixmap(sct.shot()))

        mainLayout.addWidget(imageWidget)


        widget = QWidget()
        widget.setLayout(mainLayout)

        self.setCentralWidget(widget)
        self.show()

if __name__ == '__main__':
    app = QApplication([])
    window = ClientWindow('WatchDog')
    app.exec()