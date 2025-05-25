from PyQt6.QtCore import pyqtSignal, QObject

class SignalEmitter(QObject):
    new_text = pyqtSignal(str)